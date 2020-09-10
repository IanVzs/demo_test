class A:
    def __init__(self):
        pass
    def fuca(self):
        self.__dict__["hi"] = "go"
    def test_go(self):
        self.fuca()
        print(self.hi)

a = A()
a.test_go()
