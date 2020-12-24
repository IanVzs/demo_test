# coding=utf-8
import signal
import time
  
  
def set_timeout(timeout, callback):
    def wrap(func):
        def time_out_handle(signum, frame): # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
            raise RuntimeError
    
        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, time_out_handle) # 设置信号和回调函数
                signal.alarm(timeout) # 设置 timeout 
                print('start alarm signal.')
                r = func(*args, **kwargs)
                print('close alarm signal.')
                signal.alarm(0) # 正常处理则关闭
                return r
            except RuntimeError as e:
                callback()
        return to_do
    return wrap
  
if __name__ == '__main__':
    def after_timeout(): # 超时后的处理函数
        print("do something after timeout.")
    
    @set_timeout(1, after_timeout) # 限时 1 秒
    def connect(): # 要执行的函数
        a = []
        pass
        while 1:
            a.append(1)
        return 'connect success.'
    print(connect())





elif 0:
    """
    信号掐断
    
    windows不可用, 需要改signal类型.
    原来已经添加过了...
    """
    import signal
    
    def set_timeout_class(timeout, callback):
        # 设置函数超时退出(防止死循环)
        def wrap(func):
            def time_out_handle(signum, frame):
                raise RuntimeError
    
            def to_do(*args, **kwargs):
                self = args[0]
                try:
                    signal.signal(signal.SIGALRM, time_out_handle)
                    signal.alarm(timeout)
                    r = func(*args, **kwargs)
                    signal.alarm(0)
                    return r
                except RuntimeError as e:
                    callback(self)
    
            return to_do
    
        return wrap
    
    def set_timeout(timeout, callback):
        # 设置函数超时退出(防止死循环)
        def wrap(func):
            def time_out_handle(signum, frame):
                raise RuntimeError
    
            def to_do(*args, **kwargs):
                try:
                    signal.signal(signal.SIGALRM, time_out_handle)
                    signal.alarm(timeout)
                    r = func(*args, **kwargs)
                    signal.alarm(0)
                    return r
                except RuntimeError as e:
                    callback()
    
            return to_do
    
        return wrap
    
    def after_timeout():
        # can do anthing.（；´д｀）ゞ
        print("超时了")
    
    
    @set_timeout(1, after_timeout)
    def print_hello():
        import time
        time.sleep(1)
        print("hello")
    
    print_hello()
