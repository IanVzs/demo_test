
import os
from models.base import BaseModel

class A(BaseModel):
    def go(self):
        self.a = 'c'
        print(self.a)

def go():
    c = 'c'
    c = os.listdir()
    #eval("print('from eval'*123)")
    print(c)

def get_appid():
    return "c"

def test_rewrite():
    sign = False
    print("test_rewrite", sign)
