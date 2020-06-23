import time
from multiprocessing import Pool

def f(x):
    time.sleep(1)
    print(x*x)
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
