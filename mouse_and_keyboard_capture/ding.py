import pyautogui
from pyautogui import keyboard

# mouse 控制
LIST_RECORDER = []

AAA = []

def abc(xxx):
    a = keyboard.KeyboardEvent('down', 28, 'enter')
    if xxx.event_type == 'down' and xxx.name == a.name:
        x, y = pyautogui.position()
        LIST_RECORDER.append((x, y))
        AAA.append(1)
        print("你按下了enter键")
        print(f"已经记录坐标位置:  {x}, {y}")
        alert(text=f'已经记录坐标位置:  {x}, {y}', title='ding', button='OK')
try:
    while True:
        keyboard.hook(abc)
        keyboard.wait()
except KeyboardInterrupt:
    for n, i in enumerate(LIST_RECORDER):
        x, y = i
        pyautogui.click(x=x, y=y)
        time.sleep(AAA[n])
    alert(text=f'您已完成全部设定课程, Nice!', title='ding', button='OK')
