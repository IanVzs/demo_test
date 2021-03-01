class A:
    a = 1
    def __init__(self):
        self.ini = 'ini'

    def hi(self, w):
        print(self.a)
        print(w)

    @classmethod
    def cm(self):
        print(f"in cm classmethod self.a: {self.a}")
        print(f"in www: {self.ini}")

    @classmethod
    def cm2(hi):
        print(f"in www2: asd")

class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.iin = 'iin'

    def show_init(self):
        print("in class use super: ", self.ini, self.iin)

if "__main__" == __name__:
    B().show_init()

    A().hi("w is me")
    A.cm2()
    A().cm()
