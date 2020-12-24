# coding: utf-8
"""
    redis 分布式悲观锁，需要解决以下几个问题
    1、A获取锁后崩溃，需要能将锁释放
    2、A获取锁后处理时间过长，导致锁过期，被B获取，A处理完后错误的将B锁释放
    
    redis.Redis()会有些问题，连接最好使用redis.StrictRedis()
"""

import math
import time
import uuid
from contextlib import contextmanager
from functools import wraps

from redis import WatchError


def acquire_lock(conn, lock_name, acquire_timeout=1, lock_timeout=1):
    """
    获取锁
    :param conn: redis连接
    :param lock_name: 锁名称
    :param acquire_timeout: 获取锁最长等待时间，-1为永久阻塞等待
    :param lock_timeout: 锁超时时间
    :return: 
    """

    def should_acquire():
        if acquire_timeout == -1:
            return True
        acquire_end = time.time() + acquire_timeout
        return time.time() < acquire_end

    identity = str(uuid.uuid1())
    lock_timeout = int(math.ceil(lock_timeout))
    while should_acquire():
        if conn.set(lock_name, identity, ex=lock_timeout, nx=True):
            return identity
        else:
            pttl = conn.pttl(lock_name)
            # Redis or StrictRedis
            # 如果使用的是Redis , 可能会存在pttl为0 但是显示为None的情况
            if pttl is None or pttl == -1:
                conn.expire(lock_name, lock_timeout)
        time.sleep(.1)
    return None


def release_lock(conn, lock_name, identity):
    pipe = conn.pipeline(True)
    while True:
        try:
            pipe.watch(lock_name)
            if pipe.get(lock_name) == identity:
                pipe.delete(lock_name)
                return True
            pipe.unwatch()
            break
        except WatchError:
            pass
    return False


@contextmanager
def lock(conn, lock_name, lock_timeout):
    """
    with lock(conn, "lock", 10):
        do something
    """
    id_ = None
    try:
        id_ = acquire_lock(conn, lock_name, -1, lock_timeout)
        yield id_
    finally:
        release_lock(conn, lock_name, id_)


def synchronized(conn, lock_name, lock_timeout):
    """
    @synchronized(conn, "lock", 10)
    def fun():
        counter = int(r.get("counter"))
        counter += 1
        r.set("counter", counter)
    """

    def decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            with lock(conn, lock_name, lock_timeout):
                return func(*args, **kwargs)

        return wrap

    return decorator


if __name__ == '__main__':
    import redis

    r = redis.Redis("localhost", db=5)

    id_ = acquire_lock(r, "lock", acquire_timeout=1, lock_timeout=10)
    release_lock(r, "lock", id_)
    with lock(r, "lock", 1):
        print("do something")


    @synchronized(r, "lock", 10)
    def fun():
        counter = int(r.get("counter"))
        counter += 1
        r.set("counter", counter)


    for i in range(10000):
        fun()

