import time

from delay_event import Delayer

delayer = Delayer(name='test')
delayer2 = Delayer(name='test2')

expired = int(time.time()) + 2
delayer.push(str(expired+1), expired, {"test": "go!!!!"})
delayer2.push(str(expired), expired, {"test2": "go2!!!!"})
print(f"test push success.")
