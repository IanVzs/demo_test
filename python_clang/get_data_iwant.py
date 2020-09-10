# -*-coding: utf-8-*-
"""
by: gu
闹钟安排中，涉及的一些规则选项，以及处理返回
医院对接接口中，各种模样的数据规则规整和矫正
"""
import time
import json
import datetime
import xmltodict
import collections


def get_dict_level_value_type(aim_data: dict, __type_tree: dict = {}, __father_key: str = "") -> dict:
    """提取字典结构,只处理是字典的结构 调用时，__type_tree应传入空字典"""
    father_key = __father_key
    if father_key and father_key not in __type_tree.keys():
        __type_tree[father_key] = {}

    if isinstance(aim_data, dict):
        for _k in aim_data.keys():
            get_dict_level_value_type(aim_data[_k], __type_tree[father_key] if father_key else __type_tree, _k)
    else:
        __type_tree[father_key] = aim_data.__class__.__name__
    return __type_tree


def fix_data(data, data_norm):
    """字段修正"""
    data_struct = get_dict_level_value_type(data, {})
    fixed_data = data
    for i in data_norm:
        if data_norm[i] == data[i]:
            # 类型修正
            continue
        else:
            if i == "prescription" and isinstance(data["prescription"], dict):
                fixed_data["prescription"] = [data["prescription"]]
        # 名称修正
        if "name" in fixed_data:
            fixed_data["user_name"] = data["name"]
            del fixed_data["name"]
    return fixed_data


def find_rec(data, data_norm, recorder, status_list):
    """递归查找有效数据"""
    #print(data, data_norm, "\n\n\n")
    if isinstance(data, dict) and data and data_norm:
        if set([_key.lower() for _key in data_norm.keys()]) <= set([_key.lower() for _key in data.keys()]):
            # key值检测
            if set(data_norm.keys()) <= set(data.keys()):
                data = fix_data(data, data_norm)
                recorder.append(data)
            else:
                print(f'find_rec: key is wrong|{set(data.keys())}!={set(data_norm.keys())}')
            return True
        else:
            transfer = {}
            for transfer_key in data.keys():
                if transfer_key in data_norm:
                    transfer[transfer_key] = data[transfer_key]
            for _k in data.keys():
                transfer_value = data[_k]
                transfer_value.update(transfer) if isinstance(transfer_value, dict) else ''
                find_rec(transfer_value, data_norm, recorder, status_list)
    else:
        if isinstance(data, str) and len(data) == 1 and data in '01':
            status_list.append(data)
        elif isinstance(data, int) and (data == 1 or data == 0):
            status_list.append(data)
        elif isinstance(data, list) and len(data) > 0:
            for item_data in data:
                find_rec(item_data, data_norm, recorder, status_list)


def check(data, data_norm):
    """检测"""
    checked = False
    if (isinstance(data_norm, list) and isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict)
            and set([_key.lower() for _key in data_norm[0].keys()]) <= set([_key.lower() for _key in data[0].keys()])):
        data = fix_data(data, data_norm)
        status_list = [0]
    elif isinstance(data_norm, dict) and isinstance(
            data, dict) and set([_key.lower()
                                 for _key in data_norm.keys()]) <= set([_key.lower() for _key in data.keys()]):
        data = fix_data(data, data_norm)
        status_list = [0]
    else:
        recorder = []
        status_list = []
        find_rec(data, data_norm[0] if isinstance(data_norm, list) else data_norm, recorder, status_list)
        if len(recorder) == 1 and isinstance(data_norm, dict):
            data = recorder[0]
        elif isinstance(data_norm, list):
            data = recorder
        else:
            data = data
    return (status_list, data)


class His_Data_Rule():
    """统一化整理从医院拉取处方数据，以及处方列表信息的数据"""

    def __init__(self, interface_name=''):
        """
        名称自定义
        含，不限于:
        fetch_presc
        """
        self.interface_name = interface_name

    def get_norm_data(self, source=None):
        """获取对照标准数据"""
        if source == "fetch_presc" or (not source and self.interface_name == "fetch_presc"):
            norm_data = {
                'pid': 'str',
                'date': 'str',
                'hospital': 'str',
                'department': 'str',
                'user_id': 'str',
                'gender': 'str',
                'birthday': 'str',
                'diagnosis': 'str',  #'AH': 'str', 
                'prescription': 'list'
            }
        elif source == "fetch_pids" or (not source and self.interface_name == "fetch_pids"):
            norm_data = [{
                'pid': 'str',
                'date': 'str',
                'hospital': 'str',
                'department': 'str',
                'user_id': 'str',
                'gender': 'str',
                'birthday': 'str',
                'diagnosis': 'str'
            }]
        return norm_data

    def str_2_dict(self, str_data):
        dict_data = {}
        sign_dict = collections.Counter(str_data)
        if sign_dict['<'] == sign_dict['>'] and sign_dict['>'] > 2 and sign_dict['{'] == 0:
            # xml数据
            xml_data = str_data
            xml_data = f'<result>{xml_data}</result>'
            try:
                dict_data = xmltodict.parse(xml_data)
            except Exception:
                print(f'Error:str_2_dict|{xml_data}')
        elif sign_dict['{'] == sign_dict['}']:
            # json数据
            json_data = str_data
            try:
                dict_data = json.loads(json_data)
            except Exception:
                print(f'Error:str_2_dict|{json_data}')

        return dict_data

    def convert_dt(self, dt):
        d = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
        return time.mktime(d.timetuple())

    def format_presc_data(self, presc_data, norm_data):
        """获取处方详情信息"""
        if isinstance(presc_data, str):
            presc_data = self.str_2_dict(presc_data)
        status_list, presc_data = check(presc_data, norm_data)
        return (status_list, presc_data or presc_data)

    def format_pids_data(self, pids_data, norm_data):
        """获取处方列表信息"""
        if isinstance(pids_data, str):
            pids_data = self.str_2_dict(pids_data)
        status_list, pids_data = check(pids_data, norm_data)
        formated_data = []
        for item in pids_data:
            if not item:
                continue
            rlt = {
                "_temp":
                True,
                "_placeholder":
                True,
                "_source":
                "list",
                "user_info": {
                    "gender": item["gender"],
                    "birthday": item["birthday"],
                    "allergy": "",
                    "diagnosis": item["diagnosis"],
                },
                "hospital":
                item["hospital"],
                "department":
                item["department"],
                "diagnosis": [],
                "feedback_id":
                "",
                "user_docs": [],
                "create_time":
                self.convert_dt(item.get("date") or '') if len(item.get("date")) == 19 else item.get("date"),
                "user_name":
                item.get("name") or ""
            }
            if item["diagnosis"]:
                for d in item["diagnosis"].replace("，", ",").replace("；", ",").replace("、", ",").split(","):
                    d = d.strip()
                    if not d:
                        continue
                    rlt["diagnosis"].append({
                        "name": d,
                    })
            newitem = {
                "data": rlt,
                "pid": item["pid"],
                "user_id": item["user_id"],
            }
            formated_data.append(newitem)
        formated_data.sort(key=lambda x: x["data"]["create_time"])
        return (status_list, formated_data)

    def format_data(self, source, data):
        """格式化"""
        aim_data = None
        self.interface_name = source
        norm_data = self.get_norm_data(source)
        if source == "fetch_presc":
            status_list, aim_data = self.format_presc_data(data, norm_data)
        elif source == "fetch_pids":
            status_list, aim_data = self.format_pids_data(data, norm_data)
        # print(status_list)
        return aim_data


if __name__ == "__main__":
    """数据整理测试"""
    demo_presc_data = {
        'pid':
        '4226',
        'date':
        '2017-01-04 15:39:00',
        'hospital':
        '深圳市龙岗区人民医院',
        'department':
        '中西医结合科',
        'user_id':
        '7687062',
        'gender':
        '女',
        'birthday':
        '1968-11-24',
        'AH':
        None,
        'diagnosis':
        '胃肠功能失调,胃肠功能紊乱,阴津 不足',
        'prescription': [{
            'order_no': '1',
            'generic_name': '氟哌噻吨美利曲辛片',
            'cfda_code': None,
            'size': '10.5mg*14s',
            'drug_no': '17132',
            'single_dose': '1.00',
            'single_unit': '片',
            'delivery': '口服',
            'frequency': '每日一次',
            'order_quality': '7.0000',
            'order_unit': '片',
            'course': '7天'
        }, {
            'order_no': '2',
            'generic_name': '奥美拉唑肠溶胶囊',
            'cfda_code': None,
            'size': '20mg*14粒',
            'drug_no': '06108',
            'single_dose': '1.00',
            'single_unit': '粒',
            'delivery': '口服',
            'frequency': '每日两次',
            'order_quality': '14.0000',
            'order_unit': '粒',
            'course': '7天'
        }, {
            'order_no': '3',
            'generic_name': '曲美布汀片',
            'cfda_code': None,
            'size': '0.1g*20片',
            'drug_no': '06233',
            'single_dose': '1.00',
            'single_unit': '片',
            'delivery': '口服',
            'frequency': '每日三次',
            'order_quality': '20.0000',
            'order_unit': '片',
            'course': '1天'
        }]
    }
    demo_pids_data = {
        'pid': 'D0000022648812',
        'date': '2019-02-15 14:25:00',
        'hospital': '宜昌市中心人民医院',
        'department': '简易门诊',
        'user_id': '0000950540',
        'gender': '男',
        'birthday': '1990-09-22',
        'diagnosis': '肠炎'
    }
    # print(get_dict_level_value_type(demo_presc_data, {}))
    # print("\n\n\n")
    # print(get_dict_level_value_type(demo_pids_data, {}))
    presc_data_1 = {
        'date':
        '2019-04-04 16:51:54',
        'birthday':
        '1984-09-22',
        'gender':
        '男',
        'user_id':
        '0000001925',
        'prescription': [{
            'order_no': '1',
            'generic_name': '信必可都保（布地奈德福莫特罗）',
            'cfda_code': 'H20160447',
            'size': '320ug/9ug×60吸/瓶',
            'drug_no': '25363',
            'single_dose': '8',
            'single_unit': 'ug',
            'delivery': '吸入',
            'frequency': 'bid',
            'order_quality': '1',
            'order_unit': '瓶',
            'course': ''
        }],
        'diagnosis':
        '阻塞性肺气肿',
        'pid':
        'D0000023078094',
        'hospital':
        '宜昌市中心人民医院',
        'department':
        '简易门诊',
        'AH':
        ''
    }
    presc_data_2 = {
        "status": "0",
        "data": {
            'pid':
            '4440542',
            'date':
            '2019-08-08 07:50:20',
            'hospital':
            '深圳市龙岗中心医院',
            'department':
            '儿童保健科',
            'user_id':
            '3948258',
            'gender':
            '女',
            'birthday':
            '2019-01-30',
            'diagnosis':
            '维生素D不足,高危 儿,缺铁性贫血',
            'prescription': [{
                'order_no': '3',
                'generic_name': '小儿复方四维亚铁散',
                'drug_no': '1180',
                'cfda_code': '国药准字H43021862',
                'size': '15袋',
                'single_dose': '0.500',
                'single_unit': '袋',
                'delivery': '口服',
                'frequency': 'BID',
                'order_quality': '2.0000',
                'order_unit': '盒',
                'course': '7'
            }, {
                "order_no": "4",
                "generic_name": "头孢呋辛酯片( 国家采购)",
                "drug_no": "11200",
                "cfda_code": "国药准字H20010026",
                "size": "0.25g×12片/盒",
                "single_dose": "0.250",
                "single_unit": "g",
                "delivery": "口服",
                "frequency": "BID",
                "order_quality": "1.0000",
                "order_unit": "盒",
                "course": "3"
            }, {
                "order_no": "5",
                "generic_name": "布洛芬缓释胶囊",
                "drug_no": "2034",
                "cfda_code": "国药准字H10900089",
                "size": "300mg×20片",
                "single_dose": "300.000",
                "single_unit": "mg",
                "delivery": "口服",
                "frequency": "QD",
                "order_quality": "1.0000",
                "order_unit": "粒",
                "course": "1"
            }]
        }
    }
    presc_data_3 = {
        'result': {
            'status': '0',
            'message': 'OK',
            'data': {
                'pid': '4440542',
                'date': '2019-08-08 07:50:20',
                'hospital': '深圳市龙岗中心医院',
                'department': '儿童保健科',
                'user_id': '3948258',
                'gender': '女',
                'birthday': '2019-01-30',
                'diagnosis': '维生素D不足,高危儿,缺铁性贫血',
                'prescription': {
                    'order_no': '3',
                    'generic_name': '小儿复方四维亚铁散',
                    'drug_no': '1180',
                    'cfda_code': '国药准字H43021862',
                    'size': '15袋',
                    'single_dose': '0.500',
                    'single_unit': '袋',
                    'delivery': '口服',
                    'frequency': 'BID',
                    'order_quality': '2.0000',
                    'order_unit': '盒',
                    'course': '7'
                }
            }
        }
    }

    presc_data_4 = '<Response><msgCode>0</msgCode><msg>OK</msg><msgCount></msgCount><data><pid>7054636</pid><date>2019-07-01 08:00:42</date><hospital>贵州医科大学附属医院</hospital><department>BMMZ-便民门诊</department><user_id>0000604919</user_id><gender>女</gender><birthday>1935-06-25</birthday><AH>1.注射用哌拉西林钠他唑巴坦钠.(限制使用)(4.5g(4.0g/0.5g))[珠海];2.碘 佛醇注射液(50ml:33.9g)[江苏]</AH><diagnosis>1.高血压；冠心病；失眠</diagnosis><prescription><order_no>10321385||3</order_no><generic_name>阿司匹林肠溶片</generic_name><cfda_code>国药准字J-20171021</cfda_code><size>0.1g×30片</size><drug_no>XY0025</drug_no><single_dose>0.1</single_dose><single_unit>g</single_unit><delivery>口服</delivery><frequency>Qd</frequency><order_quality>1</order_quality><order_unit>盒(30)</order_unit><course>30天</course></prescription><prescription><order_no>10321385||4</order_no><generic_name>培哚普利叔丁胺片</generic_name><cfda_code>国药准字H-20034053</cfda_code><size>4mg×30片</size><drug_no>XY1433</drug_no><single_dose>4</single_dose><single_unit>mg</single_unit><delivery>口服</delivery><frequency>Qd</frequency><order_quality>1</order_quality><order_unit>盒(30)</order_unit><course>30天</course></prescription><prescription><order_no>10321385||6</order_no><generic_name>阿托伐他汀钙片(薄膜衣片)</generic_name><cfda_code>国药准字H-19990258</cfda_code><size>10mg×7片</size><drug_no>XY0026</drug_no><single_dose>10</single_dose><single_unit>mg</single_unit><delivery>口服</delivery><frequency>Qd(睡前)</frequency><order_quality>5</order_quality><order_unit>盒(7)</order_unit><course>30天</course></prescription></data></Response>'
    presc_data_5 = '<Response><msgCode>0</msgCode><msg>OK</msg><msgCount></msgCount><data><pid>7054636</pid><date>2019-07-01 08:00:42</date><hospital>贵州医科大学附属医院</hospital><department>BMMZ-便民门诊</department><user_id>0000604919</user_id><gender>女</gender><birthday>1935-06-25</birthday><AH>1.注射用哌拉西林钠他唑巴坦钠.(限制使用)(4.5g(4.0g/0.5g))[珠海];2.碘 佛醇注射液(50ml:33.9g)[江苏]</AH><diagnosis>1.高血压；冠心病；失眠</diagnosis><prescription><order_no>10321385||3</order_no><generic_name>阿司匹林肠溶片</generic_name><cfda_code>国药准字J-20171021</cfda_code><size>0.1g×30片</size><drug_no>XY0025</drug_no><single_dose>0.1</single_dose><single_unit>g</single_unit><delivery>口服</delivery><frequency>Qd</frequency><order_quality>1</order_quality><order_unit>盒(30)</order_unit><course>30天</course></prescription></data></Response>'
    #print(His_Data_Rule().format_data("fetch_presc", presc_data_1))
    #print(His_Data_Rule().format_data("fetch_presc", presc_data_2))
    #print(His_Data_Rule().format_data("fetch_presc", presc_data_3))
    #print(His_Data_Rule().format_data("fetch_presc", presc_data_4))
    print(His_Data_Rule().format_data("fetch_presc", presc_data_5))

    pids_data_1 = [{
        'data': {
            '_temp': True,
            '_placeholder': True,
            '_source': 'list',
            'user_info': {
                'gender': '女',
                'birthday': '1935-06-25',
                'allergy': '',
                'diagnosis': ['1.高血压；冠心病；失眠']
            },
            'hospital': '贵州医科大学附属医院',
            'department': 'BMMZ-便民门诊',
            'diagnosis': [{
                'name': '1.高血压'
            }, {
                'name': '冠心病'
            }, {
                'name': '失眠'
            }],
            'feedback_id': '',
            'user_docs': [],
            'create_time': 1536538608.0,
            'user_name': ''
        },
        'pid': '5878841',
        'date': '2019-01-01 08:00:00',
        'user_id': '0000604919'
    }, {
        'data': {
            '_temp': True,
            '_placeholder': True,
            '_source': 'list',
            'user_info': {
                'gender': '女',
                'birthday': '1935-06-25',
                'allergy': '',
                'diagnosis': ['1.高血压；冠心病；失眠']
            },
            'hospital': '贵州医科大学附属医院',
            'department': 'BMMZ-便民门诊',
            'diagnosis': [{
                'name': '1.高血压'
            }, {
                'name': '冠心病'
            }, {
                'name': '失眠'
            }],
            'feedback_id': '',
            'user_docs': [],
            'create_time': 1536538608.0,
            'user_name': ''
        },
        'pid': '5878842',
        'date': '2019-01-01 08:00:00',
        'user_id': '0000604919'
    }, {
        'data': {
            '_temp': True,
            '_placeholder': True,
            '_source': 'list',
            'user_info': {
                'gender': '女',
                'birthday': '1935-06-25',
                'allergy': '',
                'diagnosis': ['1.高血压；冠心病；失眠']
            },
            'hospital': '贵州医科大学附属医院',
            'department': 'BMMZ-便民门诊',
            'diagnosis': [{
                'name': '1.高血压'
            }, {
                'name': '冠心病'
            }, {
                'name': '失眠'
            }],
            'feedback_id': '',
            'user_docs': [],
            'create_time': 1564623104.0,
            'user_name': ''
        },
        'pid': '7194251',
        'date': '2019-01-01 08:00:00',
        'user_id': '0000604919'
    }, {
        'data': {
            '_temp': True,
            '_placeholder': True,
            '_source': 'list',
            'user_info': {
                'gender': '女',
                'birthday': '1935-06-25',
                'allergy': '',
                'diagnosis': ['1.发热原因：上感、其他']
            },
            'hospital': '贵州医科大学附属医院',
            'department': 'JZNKMZ-急诊内科门诊',
            'diagnosis': [{
                'name': '1.发热原因：上感'
            }, {
                'name': '其他'
            }],
            'feedback_id': '',
            'user_docs': [],
            'create_time': 1566738539.0,
            'user_name': ''
        },
        'pid': '7300769',
        'user_id': '0000604919'
    }]

    pids_data_2 = '<Response><msgCode>0</msgCode><msg>OK</msg><msgCount></msgCount><data><prescList><pid>7194251</pid><date>2019-08-01 09:31:44</date><hospital>贵州医科大学附属医院</hospital><department>BMMZ-便民门诊</department><user_id>0000604919</user_id><gender>女</gender><birthday>1935-06-25</birthday><AH>1.注射 用哌拉西林钠他唑巴坦钠.(限制使用)(4.5g(4.0g/0.5g))[珠海];2.碘佛醇注射液(50ml:33.9g)[江苏]</AH><diagnosis>1.高血压；冠心病；失眠</diagnosis></prescList><prescList><pid>7194252</pid><date>2019-08-01 09:31:44</date><hospital>贵州医科大学附属医院</hospital><department>BMMZ-便民门诊</department><user_id>0000604919</user_id><gender>女</gender><birthday>1935-06-25</birthday><AH>1.注射用哌拉西林钠他唑巴坦钠.(限制使用)(4.5g(4.0g/0.5g))[珠海];2.碘佛醇注射液(50ml:33.9g)[江苏]</AH><diagnosis>1.高血压；冠心病；失眠</diagnosis></prescList><prescList><pid>7194253</pid><date>2019-08-01 09:31:44</date><hospital>贵州医科大学附属医院</hospital><department>BMMZ-便民门诊</department><user_id>0000604919</user_id><gender>女</gender><birthday>1935-06-25</birthday><AH>1.注射用哌拉西林钠他唑巴坦钠.(限制使用)(4.5g(4.0g/0.5g))[珠海];2.碘佛醇注射液(50ml:33.9g)[江苏]</AH><diagnosis>1.高血压；冠心病；失眠</diagnosis></prescList><prescList><pid>7300769</pid><date>2019-08-25 21:08:59</date><hospital>贵州医科大学附属医院</hospital><department>JZNKMZ-急诊内科门诊</department><user_id>0000604919</user_id><gender>女</gender><birthday>1935-06-25</birthday><AH>1.注射用哌拉西林钠他唑巴坦钠.(限制使用)(4.5g(4.0g/0.5g))[珠海];2.碘佛醇注射液(50ml:33.9g)[江苏]</AH><diagnosis>1.发热原因：上感、其他</diagnosis></prescList></data></Response>'

    pids_data_3 = '{"status":0,"message":"OK","data":[{"pid":"O18091001556","date":"2018-09-10 10:05:38","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死恢复期"},{"pid":"O18092801336","date":"2018-09-28 09:45:43","hospital":"深圳市 宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.脑梗塞恢复期"},{"pid":"O18092801851","date":"2018-09-28 10:26:15","hospital":"深圳市宝安区中医院","department":"NKMZ-内科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断: 急性咽喉炎;2.中医诊断:咳嗽病( 证型:风热犯肺证)"},{"pid":"O18092801846","date":"2018-09-28 10:25:54","hospital":"深圳 市宝安区中医院","department":"NKMZ-内科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:急性咽喉炎;2.中医诊断:咳嗽病( 证型:风热犯肺证)"},{"pid":"O18101201175","date":"2018-10-12 09:44:23","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死恢复期"},{"pid":"O18102701792","date":"2018-10-27 10:12:12","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.脑梗塞恢复期;2.中医诊断:中风病中经络( 证型:风痰入络证)"},{"pid":"O18111201570","date":"2018-11-12 09:59:24","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死后遗症"},{"pid":"O18121401357","date":"2018-12-14 09:59:47","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死后遗症"},{"pid":"O19011803008","date":"2019-01-18 14:22:01","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死后遗症"},{"pid":"O19012600171","date":"2019-01-26 08:07:51","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.脑梗塞后遗症期"},{"pid":"O19032503871","date":"2019-03-25 15:24:10","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.脑梗 死后遗症期"},{"pid":"O19042900558","date":"2019-04-29 08:41:44","hospital":"深圳市宝安区中医院","department":"NBKMZ- 脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死后遗症"},{"pid":"O19051300333","date":"2019-05-13 08:16:26","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死后遗症"},{"pid":"O19061101261","date":"2019-06-11 09:34:48","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死后遗症"},{"pid":"O19061302625","date":"2019-06-13 11:50:27","hospital":"深圳市宝安区中医院","department":"NKMZ-内科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:急性上呼吸道感染;2.中医诊断:感冒病( 证型:风热犯 表证*)"},{"pid":"O19061302626","date":"2019-06-13 11:50:27","hospital":"深圳市宝安区中医院","department":"NKMZ-内科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:急性上呼吸道感染;2. 中医诊断:感冒病( 证型:风热犯表证*)"},{"pid":"E19061400153","date":"2019-06-14 05:52:23","hospital":"深圳市宝安区中医 院","department":"JZK-急诊科","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西 医诊断:感染性发热;2.西医诊断:急性上呼吸道感染;3.中医诊断:感冒病( 证型:风热犯表证*)"},{"pid":"O19073102822","date":"2019-07-31 14:43:07","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":" 男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死后遗症;2.西医诊断:高尿酸血症"},{"pid":"O19080200695","date":"2019-08-02 08:59:56","hospital":"深圳市宝安区中医院","department":"NBKMZ-脑病科门诊","user_id":"0000003101","gender":"男","birthday":"1993-07-24","AH":"","diagnosis":"1.西医诊断:脑梗死后遗症"}]}'
    #print(His_Data_Rule().format_data("fetch_pids", pids_data_1))
    #print(His_Data_Rule().format_data("fetch_pids", pids_data_2)[0], "\n", "\n", His_Data_Rule().format_pids_data(pids_data_2)[1])
    print(His_Data_Rule().format_data("fetch_pids", pids_data_3)[0], "\n",
          f'len:::{len(His_Data_Rule().format_data("fetch_pids", pids_data_3))}', "\n",
          His_Data_Rule().format_data("fetch_pids", pids_data_3)[1])

