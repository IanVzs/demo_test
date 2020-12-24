from hashlib import blake2b
from hmac import compare_digest

SECRET_KEY = b'pseudorandomly generated server secret key'


def get_key(data):
    try:
        import requests
    except:
        print("请正确安装requests: `pip install requests`")
    def __get_params_str(dict_data: dict) -> str:
        params_str = ''
        for i in sorted(dict_data):
            if i == "data":
                continue
            params_str += f"{i}={dict_data[i]}"
        return params_str

    def __get_sign(key, size, cookie):
        h = blake2b(digest_size=size, key=key)
        h.update(cookie)
        return h.hexdigest().encode('utf-8')

    url = "https://wx.zuoshouyisheng.com/wx_api/get_key"
    app_id = data.get("app_id")
    date_keys_set = set(data.keys())
    need_keys_set = set(["datetime", "app_id", "zykf_app_id", "data"])
    if app_id and date_keys_set == need_keys_set:
        rsp_data = requests.get(url, params={"app_id": app_id}).json()
        rsp_key = ("key" in rsp_data) and rsp_key["key"]
        rsp_size = ("size" in rsp_data) and rsp_key["size"]
        if rsp_key:
            params_str = __get_params_str(data)
            sign = __get_sign(key=rsp_key, size=rsp_size, cookie=params_str)
            data = data.update(sign=sign)
        else:
            raise "获取key错误."
    else:
        raise "传参错误."
    return data



AUTH_SIZE = 16
SECRET_KEY = "iamkey"
def sign(cookie):
    h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY.encode())
    h.update(cookie)
    return h.hexdigest().encode('utf-8')

def verify(cookie, sig):
    good_sig = sign(cookie)
    print(cookie, good_sig, sig)
    print("VS :", good_sig == sig)
    return compare_digest(good_sig, sig)

cookie = b'appid=123&hello=321'
sig = sign(cookie)
print("{0},{1}".format(cookie.decode('utf-8'), sig))

print(verify(cookie, sig))
