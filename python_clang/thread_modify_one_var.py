"""
简单测试

多线程修改同一全局变量
"""
from time import sleep
from threading import Thread

global global_a
global_a = 0
def print_msg(a):
    global global_a
    while 1:
        print(f"in print_msg a: {a}")
        print(f"in print_msg global_a: {global_a}")
        sleep(1)

def modify_var(a):
    global global_a
    while 1:
        sleep(1)
        a += 1
        global_a += 1

if "__main__" == __name__:
    a = 0
    w1 = Thread(target=print_msg, args=(a, ))
    w2 = Thread(target=modify_var, args=(a, ))

    w1.start()
    w2.start()
