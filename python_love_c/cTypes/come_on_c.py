import time
from ctypes import *

#load the shared object file
adder = CDLL('./adder.so')

loop_num = 10000000
def add_int(a, b):
    return a+b

def add_float_py(a, b):
    return a+b

#Find sum of integers
aaa = time.time()
res_int = adder.add_int(4,5)
print(f'Sum of 4 and 5 = {str(res_int)}, counter: {time.time()-aaa}')
aaa = time.time()
for i in range(loop_num):
    res_int = add_int(4, 5)
print(f'Sum of 4 and 5 = {str(res_int)}, counter: {time.time()-aaa}')


#Find sum of floats
a = c_float(5.5)
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
aaa = time.time()
add_float(a, b)
print(f"Sum of 5.5 and 4.1 add_float: {time.time()-aaa}")
aaa = time.time()
for i in range(loop_num):
    add_float_py(5.6, 4.1)
print(f"Sum of 5.5 and 4.1 add_float_py: {time.time()-aaa}")
