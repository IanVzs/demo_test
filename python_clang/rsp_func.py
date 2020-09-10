def rsp_status(func):
    """返回函数执行状态"""
    def wrapper(*args):
        rsp = {"sign": 0, "msg": ''}
        data = func(*args)
        if "a" in data:
            rsp["sign"] = 1
            rsp.update(data)
        else:
            rsp["msg"] = data.get("msg") or ''
        return rsp
    return wrapper

@rsp_status
def return_dict(a):
    if a:
        return {"a": "goood"}
    else:
        return {"msg": "not a"}

print(return_dict(1))
print(return_dict(0))
