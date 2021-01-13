"""
使用:
    # data 传入{"action": "request", "request": {"url", "method", "params", "data", "json"}}
"""
import json
import time
import redis
import requests
from multiprocessing import Process

from tornado.log import app_log as log

from delay_event import config
REDIS_DATABASE = config.REDIS_DATABASE

rds = redis.Redis(host=REDIS_DATABASE['HOST'], port=REDIS_DATABASE['PORT'], db=REDIS_DATABASE['DB'])


def request(**data):
    rsp = None
    if not data:
        log.error("request|error|get_None")
        return rsp
    try:
        data["timeout"] = 10
        rsp = requests.request(**data).json()
    except Exception as err:
        log.error(f"request|error|{err}")
    return rsp


class Delayer():
    def __init__(self, name=''):
        self.name = name

    def push(self, no: str, expired: int, data: dict):
        sign = sign2 = 0
        try:
            sign = rds.zadd(self.name, {no: int(expired)})
            sign2 = rds.set(no, json.dumps(data, ensure_ascii=False))
            log.info(f"Delayer|push|{self.name}|{no}")
        except Exception as err:
            rds.zrem(self.name, no)
            rds.delete(no)
            info = {"name": self.name, "no": no, "data": data}
            log.error(f"Delayer|push|{err}|{info}")
        return bool(sign and sign2)

    def remove(self, no) -> bool:
        log.info(f"Delayer|remove|{self.name}|{no}")
        sign1 = rds.zrem(self.name, no)
        sign2 = rds.delete(no)
        sign = bool(sign1 and sign2)
        log.info(f"Delayer|remove|{self.name}|{no}|{sign1}&{sign2}")
        if not sign:
            info = {"sign_zrem": sign1, "sign_delete": sign2}
            log.error(f"Delayer|remove|failed|{self.name}|{no}|{info}")
        return sign

    def get(self, no):
        bdata = rds.get(no)
        bdata = bdata and bdata.decode()
        bdata = bdata and json.loads(bdata)
        return bdata

    def zcount(self, now: int = 0, left: int = config.LEFT_OFFSET, right: int = 10):
        min = now - left
        max = now + right
        count = rds.zcount(self.name, min=min, max=max)
        return count

    def zrange2data(self, max, now=0):
        list_result = rds.zrange(self.name, 0, max, withscores=True)
        dict_datas = {}
        for bmembr, score in list_result:
            no = bmembr.decode()
            if score > now:
                continue
            data = self.get(no)
            dict_datas[no] = data
        return dict_datas

    def do_thing(self, now):
        need = self.zcount(now, right=0)
        range_data = self.zrange2data(need, now)
        rsp = None
        for no, data in range_data.items():
            action = data and data.get("action")
            if action == "request":
                rsp = request(**(data.get(action) or {}))
            elif action == "xxx":
                # do other
                pass
            else:
                log.error(f"Delayer|do_thing|nothing|{data}")
            if rsp and rsp["status"] == 0:
                self.remove(no)
                log.info(f"Delayer|do_thing|sucess&rm|{no}")
            else:
                # TODO 应该加入重试队列，之后再实现
                log.error(f"Delayer|do_thing|rsp_error_but_rm|{no}")
                self.remove(no)

    def run(self):
        while 1:
            int_now = int(time.time())
            znum = self.zcount(int_now)
            if znum:
                log.info(f"{self.name}|delaye event|{int_now}|{znum}")
                self.do_thing(int_now)
            else:
                log.info(f"{self.name} no delaye event|{int_now}")
            time.sleep(10)


def run(name=''):
    delayer = Delayer(name=name)
    delayer.run()


if __name__ == "__main__":
    list_names = ["test", "test", "test2"]
    for i in list_names:
        p = Process(target=run, args=(i, ))
        p.start()
        p.join()
