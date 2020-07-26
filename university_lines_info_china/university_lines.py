import json
import time
import requests

def get_data():
    with open("university_lines.txt", "a") as u_file:
        # for i in range(0, 1000):
        for i in range(1000, 5000):
            try:
                data = requests.get(f"https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/{i}/14/1/1.json").json()
                if not data or data["code"] != "0000":
                    print(f"University ID {i} no info.<<<<<<<")
                    continue
                str_data = json.dumps(data, ensure_ascii=False)
                u_file.write(str_data+"\n")
                print(f"University ID {i} yeah.")
                time.sleep(0.3)
            except:
                print(f"University ID {i} failed.>>>>>>>>>>>>>>>>>")

def get_info(school_id):
    name, province_name, city_name, content = '','','',''
    with open("university_infos.txt", "a") as u_file:
        # for i in range(0, 1000):
        try:
            data = requests.get(f"https://static-data.eol.cn/www/2.0/school/{school_id}/info.json").json()
            if not data or data["code"] != "0000":
                print(f"University InFo {school_id} no info.<<<<<<<")
            str_data = json.dumps(data, ensure_ascii=False)
            u_file.write(str_data+"\n")
            print(f"University InFo {school_id} yeah.")
            time.sleep(0.3)
            name, province_name, city_name, content = data["data"]["name"], data["data"]["province_name"], data["data"]["city_name"], data["data"]["content"]
            content.replace(",", ".")
        except:
            print(f"University InFo {school_id} failed.>>>>>>>>>>>>>>>>>")
    return name, province_name, city_name, content
    
def get_commenttop(school_id):
    comm_list = []
    comprehensive_score, comment_time, content = '','',''
    with open("university_comm.txt", "a") as u_file:
        # for i in range(0, 1000):
        try:
            data = requests.get(f"https://static-gkcx.eol.cn/www/2.0/json/commenttop/{school_id}.json").json()
            if not data or data["code"] != "0000":
                print(f"University Comm {school_id} no info.<<<<<<<")
            str_data = json.dumps(data, ensure_ascii=False)
            u_file.write(str_data+"\n")
            print(f"University Comm {school_id} yeah.")
            time.sleep(0.3)
            for i in data["data"]["item"]:
                line_keys = ["comprehensive_score", "comment_time", "content"]
                line_datas = [(i.get(_i) or '') for _i in line_keys]
                line_datas_str = '|'.join(line_datas)
                line_datas_str = line_datas_str.replace(",", ".")
                comm_list.append(line_datas_str)
        except:
            print(f"University Comm {school_id} failed.>>>>>>>>>>>>>>>>>")
    return comm_list


def check_point(point, _min, _max):
    if point >= _min and point < _max:
        return True
    else:
        return False

def para_data():
    with open("university_lines.txt", "r") as u_file:
        school_id_list = []
        for i in u_file:
            i = json.loads(i)
            if i:
                for ii in i["data"]["item"]:
                    if set(ii["min"]) & set("1234567890"):
                        _point = float(ii["min"])
                    elif set(ii["max"]) & set("1234567890"):
                        _point = float(ii["max"])
                    elif set(ii["average"]) & set("1234567890"):
                        _point = float(ii["average"])
                    else:
                        continue
                    #if check_point(_point, 430, 500):
                    if check_point(_point, 490, 507):
                        if ii["school_id"] in school_id_list:
                            name = province_name = city_name = content = comm_list = ''
                        else:
                            name, province_name, city_name, content = get_info(ii["school_id"])
                            comm_list = get_commenttop(ii["school_id"])
                            school_id_list.append(ii["school_id"])
                        line_keys = ["school_id", "year", "max", "average", "min", "local_batch_name", "zslx_name"]
                        line_datas = [(ii.get(_i) or '') for _i in line_keys]
                        line_datas_str = ','.join(line_datas)
                        print(f"{name},{province_name},{city_name},{line_datas_str},{content},{comm_list}")
                        break

def format_word(file_path, aim_path):
    """
    执行para_data后， 将print写入文件，但Linux >> 写入有编码问题， 需要在手动重新编码

    不如直接把print换为 写文件，然而懒
    """
    import csv
    with open(aim_path,'w',newline='',encoding='utf-8-sig') as f:
        with open(file_path, 'r') as r:
            for i in r:
                print(i)
                f.write(str(i))

if "__main__" == __name__:
    # get_data()
    # para_data()
    format_word("goal3s.txt", "goal_490_507.txt")
