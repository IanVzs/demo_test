"""
类装饰器
"""
import datetime

def check_access_token(func):
    def wrapper(self, *args, **kwargs):
        time_now = datetime.datetime.now()
        if time_now < self.access_token_expired_time:
            return func(self, *args, **kwargs)
        else:
            self.get_access_token(self.mode)
            self.format_url()
            return func(self, *args, **kwargs)

    return wrapper


def check_time(func):
    time_server_start = 9
    time_server_end = 11
    time_server_end = 17
    def wrapper(self, *args, **kwargs):
        time_now = datetime.datetime.now()
        if time_now.hour < time_server_end and time_now.hour > time_server_start:
            return func(self, *args, **kwargs)
        else:
            return self.failed("超时.")

    return wrapper

class A():
    def sucess(self):
        return "sucess"

    def failed(self, msg=''):
        return f"failed: {msg}"

    @check_time
    def run(self):
        return self.sucess()


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

if "__main__" == __name__:
    a = A()
    print(a.run())
    print(return_dict(1))
    print(return_dict(0))

