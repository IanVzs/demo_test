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

def step1():
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

def step2():
    """算数运算"""
    x = np.uint8([250])
    y = np.uint8([10])

    print(cv2.add(x, y))
    print(x+y)
    # 差别, 一个封顶, 一个溢出
    """混合图像"""
    img1=cv2.imread('ml.png')
    img2=cv2.imread('opencv_logo.png')
    dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
    show_img(dst)

def step3():
    img1 = cv2.imread('demo.png')
    img2 = cv2.imread('ml.png')
    img2 = cv2.imread('opencv_logo.png')
    rows, cols, channels = img2.shape
    
    roi = img1[0:rows, 0:cols]
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols ] = dst
    show_img(img1)