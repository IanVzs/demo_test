"""
elif cv2.waitKey(1) & 0xFF == ord('w'):
    w = True
妄想通过此方式实现延时播放的效果失败了。。。
"""

import cv2
import time

cap = cv2.VideoCapture("/home/ian/Videos/录屏/录屏 2022年05月06日 15时12分21秒.webm")

num = 0
w = False
e = False

ret, f = cap.read()
while ret:
        num += 1     
        cv2.imshow("", f)
        ret, f = cap.read()
        cv2.imwrite(f"{num}.png", f)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('w'):
            w = True
            time.sleep(0.5)
            print(num)
        elif cv2.waitKey(1) & 0xFF == ord('e'):
            e = True
            time.sleep(1)
            print("e -> ", num)
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            time.sleep(1)
            print("s -> -> -> ", num)
        if w:
            time.sleep(0.5)
        elif e:
            time.sleep(1)
            
cap.release()
cv2.destroyAllWindows()
