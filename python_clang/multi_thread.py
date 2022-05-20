from threading import Thread


class SingleThread(Thread):
    def __init__(self, func, *params, **kwargs):
        """
        :param func:    object  待执行的函数对象
        :param params:  tuple   函数的参数
        :param kwargs:  dict    函数的key-value参数
        """
        Thread.__init__(self)
        self.func = func
        self.args = params
        self.kwargs = kwargs
        self.result = None

    # 调用SingleThread.start()时该函数会自动执行
    def run(self):
        self.result = self.func(*self.args, **self.kwargs)


class Threads(object):
    """
    并发执行多个线程，并获取进程的返回值
    """
    def __init__(self):
        self.threads = list()
        self.result = list()  # 进程执行的返回值组成的列表

    def add(self, my_thread):
        """
        将任务添加到待执行线程队列中
        :param my_thread:   SingleThread    线程对象
        :return:
        """
        self.threads.append(my_thread)

    def exec(self):
        """
        多线程同时执行线程队列中的人物
        :return:
        """
        # 启动进程序列
        for t in self.threads:
            t.start()

        # 等待进程序列执行完成
        for t in self.threads:
            t.join()

        # 获取线程返回值
        for t in self.threads:
            self.result.append(t.result)


if __name__ == "__main__":
    from time import sleep

    def test_add(name, a, b, num):
        for i in range(num):
            sleep(1)
            print("{}: {}".format(name, i))
        return a+b

    thread1 = SingleThread(test_add, "thread1", 1, 2, 5)
    thread2 = SingleThread(test_add, "thread2", a=2, b=3, num=4)
    threads = Threads()
    threads.add(thread1)
    threads.add(thread2)
    threads.exec()
    print(threads.result)
