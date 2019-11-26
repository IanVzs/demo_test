"""
loop 实力吊打 numpy (○´･д･)ﾉ
"""

import time
import numpy as np

a = [1,'w'*2000, '']*10
b = [1,'w'*2000, '1']*10
n = ['', '', '']*10


s_time = time.time()
for i in range(1000000):
    bool_list = []
    for num, i in enumerate(a):
        if i == '':
            bool_list.append(True)
        elif i == b[num]:
            bool_list.append(True)
        else:
            bool_list.append(False)
    result = False not in bool_list
print("round2: ", time.time()-s_time, result)


s_time = time.time()
aaa = np.array(a)
bbb = np.array(b)
nnn = np.array(n)
for i in range(1000000):
    aa = aaa == bbb
    bb = aaa == nnn
    result = not (aa == bb).any()
print("round1: ", time.time()-s_time, result)
