"""
使用说明, 每使用一个新(name不同以往)的 Delayer,
都需要在delay_event.py中进行显式声明.
否则无法监控到,即无效`send`(后期多了可能改成自动的,但现在还没实现)
"""
import time
from delay_event import Delayer

delayer = Delayer(name='test')
delayer2 = Delayer(name='test2')

expired = int(time.time()) + 2
no = str(expired + 1)
delayer.push(no, expired, {"test": "go!!!!"})

no = str(expired)
delayer2.push(no, expired, {"test2": "go2!!!!"})
print(f"test push success.")

# reigion 撤销事件
delayer.remove(no)
#endregion
