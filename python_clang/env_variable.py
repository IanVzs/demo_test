
def run():
    a = 'a'
    print(locals().keys())
    print(globals().keys())

class A:
    def a_b(self):
        self.a_b_1 = ''


if "__main__" == __name__:
    a = A()
    run()
