"""
开始吧
hi之后的,真正的图像操作
"""

import cv2
import numpy as np

img = cv2.imread("demo.png")
def show_img(img):
    cv2.imshow('showed', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""逐像素修改"""
px = img[427, 325]
#print(px)
blue = img[427, 325, 1]
#print(blue)
img[100,100] = [222,211,200]
#print(img[100,100])
#print(img.item(100,100,0),img.item(100,100,1),img.item(100,100,2))
print(img.shape, img.size, img.dtype)

"""移动部分图像"""
img = cv2.imread("demo.png")
move_partial = img[280:340, 330:390]
img[203:263, 50:110] = move_partial
show_img(img)