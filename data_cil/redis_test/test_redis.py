# -*- coding: utf-8 -*-
# 300~1000人抢100张票，保证不超发
import redis
import time
import threading
from redis import WatchError
from redis_lock import synchronized

REDIS_DATABASE = {
    'HOST': 'localhost',
    'PORT': 6379,
    'DB': 0
}
TICKET_NUM = 100  # 票数
PEOPLE_NUM = 3000  # 人数

rds = redis.Redis(host=REDIS_DATABASE['HOST'], port=REDIS_DATABASE['PORT'], db=REDIS_DATABASE['DB'])
rds.delete('ticket_num')
rst = rds.incr('ticket_num', amount=TICKET_NUM)

rds.delete('tickets')
values = ['' for _ in xrange(TICKET_NUM)]
tickets = rds.lpush('tickets', *values)


class TestRedis(threading.Thread):
    def __init__(self, t_num):
        self.t_num = t_num
        super(TestRedis, self).__init__()

    def run(self):
        self.error_examples()  # 错误示范，多线程下会超发
        # self.optimistic_lock()  # 利用redis自带事务（乐观锁）
        # self.pessimistic_lock  # 自实现的悲观锁，比乐观锁快一丢丢
        # self.redis_list()  # 利用redis单线程特性，队列操作
        # self.redis_incr()  # 推荐方法！利用redis单线程特性，计数器操作

    def error_examples(self):
        """
        错误示范，多线程下会超发
        :return:
        """
        ticket_num = int(rds.get('ticket_num'))
        if ticket_num > 0:
            print('t_num=%s, ticket_num=%s' % (self.t_num, ticket_num))
            rds.set('ticket_num', ticket_num-1)

    def optimistic_lock(self):
        """
        乐观锁
        :return:
        """
        while 1:
            with rds.pipeline(transaction=True) as r_pip:
                r_pip.watch('ticket_num')
                try:
                    r_pip.multi()
                    ticket_num = int(rds.get('ticket_num'))
                    if ticket_num > 0:
                        r_pip.decr('ticket_num')
                    r_pip.execute()
                    return
                except WatchError:
                    r_pip.unwatch()

    @synchronized(rds, "lock", 1000)
    def pessimistic_lock(self):
        """
        悲观锁
        :return:
        """
        ticket_num = int(rds.get('ticket_num'))
        if ticket_num > 0:
            rds.decr('ticket_num')

    def redis_list(self):
        """
        减列表方式，防止超发。利用redis单线程特性
        缺点：消耗内存
        :return:
        """
        ticket = rds.lpop('tickets')
        if ticket is not None:
            rds.decr('ticket_num')

    def redis_incr(self):
        """
        利用redis单线程特性。
        :return:
        """
        if int(rds.get('ticket_num')) > 0:
            de_num = rds.decr('ticket_num')  # 当只剩最后一张票时，多个线程都取到1，同时减后会成负数即“超发”
            if de_num < 0:  # “超发”后补回。不继续操作
                rds.incr('ticket_num')


tests = []
for i in xrange(PEOPLE_NUM):
    t = TestRedis(i+1)
    tests.append(t)

s = time.time()
for t in tests:
    t.start()
for t in tests:
    t.join()

print('result ticket_num=%s, time=%s' % (rds.get('ticket_num'), (time.time()-s)*1000))








