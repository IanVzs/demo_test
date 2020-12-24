import time

def t_diff(start: float, end: float):
    s = end - start
    print(f"all cost s: {s},   u: <-")

def go():
    I = 73 ** 5
    for i in range(I):
        pass
    return I, i

if "__main__" == __name__:
    print("*******************Python3**********************")
    start = time.time()
    a, b = go()
    end = time.time()
    print(f"loop result: {b}")
    print(f"pow result: {a}")
    t_diff(start, end)
