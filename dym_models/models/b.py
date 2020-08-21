from models.base import BaseModel
class A(BaseModel):
    def go(self):
        self.a = 'b'
        print(self.a)

def go():
    a = 'b'
    print(a)

def get_appid():
    return "b"

def test_rewrite():
    sign = True
    print("test_rewrite", sign)
