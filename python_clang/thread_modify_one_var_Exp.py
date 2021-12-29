"""
升级版

主线程创建子线程，优雅退出
"""
import sys
from time import sleep
from threading import Thread
from signal import signal, SIGINT, SIGTERM

global global_a
global_a = 0
def print_msg(a):
    global global_a
    while 1:
        print(f"in print_msg a: {a}")
        print(f"in print_msg global_a: {global_a}")
        sleep(1)

def quit(signum, frame):
    # 检测`ctrl+c` 优雅退出
    print("\nYou kill me -_-~")
    sys.exit()

if "__main__" == __name__:
    # 中断信号注册
    signal(SIGINT, quit)
    signal(SIGTERM, quit)

    a = 0
    w1 = Thread(target=print_msg, args=(a, ))
    w1.setDaemon(True) # 放在start之前
    w1.start()
    while 1:
        sleep(1)
        a += 1
        global_a += 1

