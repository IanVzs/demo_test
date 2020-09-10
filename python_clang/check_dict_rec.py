"""
检查两个字典结构/内容是否相同,
data_norm为必要条件,
!被验证data必须含有data_norm所有的结构
"""


TYPE_DICT = {"dict": dict, "str": str, "list": list, "float": float, "int": int}

def check_rec(data, data_norm, recorder):
    """递归检查"""
    #print(data, data_norm, "\n\n\n")
    if isinstance(data_norm, dict) and data and data_norm:
        for _k in data_norm.keys():
            if _k in data.keys():
                check_rec(data[_k], data_norm[_k], recorder)
            else:
                print(f'check_rec:key in dict|{_k}|not exist/loss')
                recorder.append(False)
    else:
        if data == data_norm:
            recorder.append(True)
            return True
        elif data_norm in TYPE_DICT:
            _data_norm = TYPE_DICT[data_norm]
            if isinstance(data, _data_norm):
                if _data_norm == list and len(data) == 0:
                    recorder.append(False)
                else:
                    recorder.append(True)
                return True
            else:
                print(f'check_rec:|{data} {data_norm}|type not match')
                recorder.append(False)
                return False
        else:
            print(f'check_rec: {data} != {data_norm}')
            recorder.append(False)
            return False


def check(data, data_norm):
    """检测"""
    checked = False
    if data == data_norm:
        checked = 1
    elif not checked:
        recorder = []
        check_rec(data, data_norm, recorder)
        if False in recorder:
            checked = 0
        elif True in recorder:
            checked = 1
    else:
        print('error')

    if checked == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(check({"a": 123}, {"a": 123}))
    print(check({"a": 123}, {"a": 12}))
    print(check({"a": 123}, {"a": 'int'}))
    print(check({"a": 123}, {"a": 'str'}))
    print(check({"a": 123}, {"b": 'str'}))
