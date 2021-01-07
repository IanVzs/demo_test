"""
使用Redis存储事件,实现可能不好,不过也比脚本实现要靠谱多了

Python版
如果想不到更好的解决方式估计以后还会更新其他语言版？
"""
import json
import time
import redis

class Log:
    def info(self, data):
        print(data)
    def error(self, data):
        print(data)
log = Log()

REDIS_DATABASE = {
    'HOST': 'localhost',
    'PORT': 6379,
    'DB': 0
}

rds = redis.Redis(
    host=REDIS_DATABASE['HOST'],
    port=REDIS_DATABASE['PORT'],
    db=REDIS_DATABASE['DB']
)

def request(data):
    import requests
    rsp = requests.request(**data).json()
    return rsp

class Delayer():
    def __init__(self, name=''):
        self.name = name

    def push(self, no:str, expired: int, data: dict):
        sign = sign2 = 0
        try:
            sign = rds.zadd(self.name, int(expired), no)
            sign2 = rds.set(no, json.dumps(data, ensure_ascii=False))
        except Exception as err:
            rds.zrem(self.name, no)
            rds.delete(no)
            info = {
                "name": self.name,
                "no": no,
                "data": data
            }
            log.error(f"Delayer|push|{err}|{info}")
        return bool(sign and sign2)
    
    def remove(self, no) -> bool:
        sign = rds.zrem(self.name, no)
        sign2 = rds.delete(no)
        return bool(sign and sign2)
    
    def get(self, no):
        bdata = rds.get(no)
        bdata = bdata and bdata.encode()
        bdata = bdata and json.loads(bdata)
        return bdata
    
    def zcount(self, now: int=0, left: int=1000, right: int=10):
        min = now - left
        max = now + right
        count = rds.zcount(self.name, min=min, max=max)
        return count

    def zrange2data(self, max, now=0):
        list_result = rds.zrange(self.name, 0, max, withscores=True)
        # TODO
        data = {}
        for r in list_result:
            no = r["scores"]
            if no > now:
                continue
            data = self.get(no)
            data[no] = data
        return data

    def do_thing(self, now):
        need = self.zcount(now, 10, 0)
        range_data = self.zrange2data(need, now)
        for no, data in range_data.items():
            rsp = request(**data)
            if rsp["status"] == 0:
                self.remove(no)
            else:
                pass

    def run(self):
        int_now = int(time.time())
        if self.zcount(int_now):
            self.do_thing(int_now)


if __name__ == "__main__":
    delayer = Delayer(name='test')
    delayer.run()
