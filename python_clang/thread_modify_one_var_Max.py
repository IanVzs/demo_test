"""
牛逼版

主线程创建子线程
将信息更新给子线程
优雅退出
"""
import sys
from time import sleep
from random import uniform
from threading import Thread
from signal import signal, SIGINT, SIGTERM

class Question:
    qid = 0
    content = ''
    # qid int
    # content str
class Answer:
    qid = 0
    content = ''
    # qid int
    # content str
    def __str__(self):
        return f"qid: {self.qid}\t content: {self.content}"

global global_question
global_question = Question()

global global_answer
global_answer = Answer()

def get_answer():
    global global_question
    global global_answer
    while 1:
        qid = global_question.content
        global_question.qid = qid
        global_answer.qid = qid
        global_answer.content = f"算出结果为: haha {qid}"

def quit(signum, frame):
    # 检测`ctrl+c` 优雅退出
    print("\nYou kill me -_-~")
    sys.exit()

class MainClass:
    def __init__(self):
        self.sub_thread = Thread(target=get_answer, args=())
        self.sign_sub_thread_runing = False
        self.dict_answer = {}
    def step(self, new_msg):
        global global_question
        global global_answer
        global_question.content = str(new_msg)
        global_question.qid = str(new_msg)
        if global_answer.qid != global_question.qid:
            # 问题答案不匹配,新问题
            print(f"新问题: {new_msg}")
        if not self.sign_sub_thread_runing:
            # 解答线程未启动
            self.sub_thread.setDaemon(True) # 放在start之前
            self.sub_thread.start()
            self.sign_sub_thread_runing = True

        sleep(0.01)
        if global_answer.qid not in self.dict_answer.keys() and global_answer.qid == global_question.qid:
            # 获取到了该问题的答案
            self.dict_answer[global_answer.qid] = global_answer
            print(f"答案为: {global_answer}")

if "__main__" == __name__:
    # 中断信号注册
    signal(SIGINT, quit)
    signal(SIGTERM, quit)

    obj = MainClass()
    for i in range(10):
        for ii in [i]*10:
            obj.step(i)
        sleep(0.1)
    # while 1:
    #     new_msg = int(uniform(1, 3))
    #     obj.step(new_msg)
    #     sleep(0.1)
