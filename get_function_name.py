import sys
def hello():
    print(sys._getframe().f_code.co_name)

class A():
    def who_am_i(self):
        print(sys._getframe().f_code.co_name)

hello()
A().who_am_i()
