import time

from delay_event import Delayer

delayer = Delayer(name='test')

expired = int(time.time()) + 2
delayer.push(str(expired), expired, {"test": "go!!!!"})
print(f"test push success.")