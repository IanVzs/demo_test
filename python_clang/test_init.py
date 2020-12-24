class A():
    def __init__(self):
        self.a = 1
    def hello(self):
        self.b = 233
        return self.b
    def hi(self):
        print(self.b)
w = A()
print(w.a)
try:
    w.hi()
except Exception as err:
    print(err)
print(w.hello())
