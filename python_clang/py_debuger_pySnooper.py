import pysnooper
import random

def foo():
    lst = []
    for i in range(10):
        lst.append(random.randrange(1, 1000))

    with pysnooper.snoop("test.log"):
        lower = min(lst)
        upper = max(lst)
        mid = (lower + upper) / 2
        print(lower, mid, upper)

@pysnooper.snoop(depth=1)
def while_fun():
    a = 0
    while 1:
        a += 1
        if a > 10000:
                break
while_fun()
foo()
