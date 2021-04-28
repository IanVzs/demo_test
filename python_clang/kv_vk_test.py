aaa = {}
for i in range(10000000):
    aaa[i] = i/123

import time

a = time.time()

a123 = dict(zip(aaa.values(), aaa.keys()))

print(f"zip: {time.time()-a}")


b = time.time()

b123 = {v:k for k, v in aaa.items()}

print(f"dict: {time.time()-b}")


"""
zip: 3.073076009750366
dict: 3.150221824645996
"""
