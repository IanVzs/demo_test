"""
获取字典，每个层级的数据类型
返回一个结构相同的字典，但其中只包括数据类型的字符串
"""

def get_dict_level_value_type(
        aim_data: dict, __type_tree: dict = {}, __father_key: str = "") -> dict:
    """
    只处理是字典的结构
    !调用时, __type_tree 应传入'{}'空字典，用于清空上一次调用的缓存(可能有)
    """
    father_key = __father_key
    if father_key and father_key not in __type_tree.keys():
        __type_tree[father_key] = {}

    if isinstance(aim_data, dict):
        for _k in aim_data.keys():
            get_dict_level_value_type(aim_data[_k], __type_tree[father_key] if father_key else __type_tree, _k)
    else:
        __type_tree[father_key] = aim_data.__class__.__name__
    return __type_tree




def get_iterative_value_type(aim_data, addition_list):
    """
    addition_list 中定义拆分的数据类型， 返回任意输入的层级结构
    """
    for _k in aim_data.keys():
        if aim_data[_k] in addition_list:
            pass

    return ''

if __name__ == "__main__":
    print(get_dict_level_value_type({"a": 123, "lol": "你吼", "loop": {"emmm": True, "again": {"3level": [1,2,3]}}}, {}))
    print(get_dict_level_value_type({'data': {'alarm_id': '117af20b-9da7-4ad5-b1cb-dd064373ece8', 'drugs': ['阿奇霉素片', '布洛芬片'], 'feedback_id': 'tester_feedbackid', 'owner': ['1111222'], 'report_url': 'https://kfz.dos2unix.cn/take_drug/presc_report_list?app_id=&user_id=1111222', 'switch': False, 'timeline': [{'items': [{'alarm_id': '117af20b-9da7-4ad5-b1cb-dd064373ece8', 'dose': '1片', 'generic_name': '阿奇霉素片', 'new_time': '', 'status': 0, 'tags': '饭前', 'time': '2019-08-07 08:00:00', 'user_id': '1111222'}], 'time': '2019-08-07 08:00:00'}, {'items': [{'alarm_id': '117af20b-9da7-4ad5-b1cb-dd064373ece8', 'dose': '1片', 'generic_name': '布洛芬片', 'new_time': '', 'status': 0, 'tags': '饭前', 'time': '2019-08-07 08:30:00', 'user_id': '1111222'}], 'time': '2019-08-07 08:30:00'}, {'items': [{'alarm_id': '117af20b-9da7-4ad5-b1cb-dd064373ece8', 'dose': '1片', 'generic_name': '阿奇霉素片', 'new_time': '', 'status': 0, 'tags': '饭前', 'time': '2019-08-07 12:00:00', 'user_id': '1111222'}], 'time': '2019-08-07 12:00:00'}, {'items': [{'alarm_id': '117af20b-9da7-4ad5-b1cb-dd064373ece8', 'dose': '1片', 'generic_name': '布洛芬片', 'new_time': '', 'status': 0, 'tags': '饭前', 'time': '2019-08-07 13:00:00', 'user_id': '1111222'}], 'time': '2019-08-07 13:00:00'}, {'items': [{'alarm_id': '117af20b-9da7-4ad5-b1cb-dd064373ece8', 'dose': '1片', 'generic_name': '阿奇霉素片', 'new_time': '', 'status': 0, 'tags': '饭前', 'time': '2019-08-07 17:00:00', 'user_id': '1111222'}], 'time': '2019-08-07 17:00:00'}, {'items': [{'alarm_id': '117af20b-9da7-4ad5-b1cb-dd064373ece8', 'dose': '1片', 'generic_name': '布 洛芬片', 'new_time': '', 'status': 0, 'tags': '饭前', 'time': '2019-08-07 19:00:00', 'user_id': '1111222'}], 'time': '2019-08-07 19:00:00'}], 'user_name': ''}, 'message': '请求 成功', 'status': 0}, {}))
