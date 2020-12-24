"""删除列表中混入的某些坏家伙"""

def del_str_in_int_list(list_data):
    """删除int列表中的str"""
    counter = 0
    counter_del = 0
    for i, ii in enumerate(list_data):
        if isinstance(ii, int):
            # 保留条件
            list_data[counter] = list_data[i]
            counter += 1
        else:
            counter_del += 1
            list_data[counter] = list_data[i]
    if counter_del:
        list_data = list_data[:-counter_del]
    return list_data

if __name__ == "__main__":
    a = [1,2,"a","234", 3,4, "c", 5,6,"asd", "23333"]
    b = del_str_in_int_list(a)
    print(a, '\n', b)
    a = [1,]
    b = del_str_in_int_list(a)
    print(a, '\n', b)
    a = [1,1]
    b = del_str_in_int_list(a)
    print(a, '\n', b)
    a = [1,"a"]
    b = del_str_in_int_list(a)
    print(a, '\n', b)

