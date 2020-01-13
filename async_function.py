import random
import asyncio
from time import sleep


class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos

all_potatos = Potato.make(5)


def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            sleep(.1)
        else:
            potato = all_potatos.pop()
            yield potato
            count += 1
            if count == num:
                break

def buy_potatos():
    bucket = []
    for p in take_potatos(50):
        bucket.append(p)

def main():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(buy_potatos())
    loop.close()
# main() #当make数目不足时, 将死等
#-----------------------------------------------------------------#

async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break

async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))


async def buy_potatos():
    bucket = []
    async for p in take_potatos(50):
        bucket.append(p)
        print(f'Got potato {id(p)}...')
    
async def buy_tomatos():
    bucket = [p async for p in take_potatos(50)]# 懒得换生产西红柿了...
    # 类似的: result = [await fun() for fun in funcs if await condition()]
    print(f'Done {bucket}')

def main():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(buy_potatos())
    loop.close()
def main():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(asyncio.wait([buy_potatos(), buy_tomatos()]))
    loop.close()
main()
