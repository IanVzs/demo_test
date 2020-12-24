
# -*- coding: utf-8 -*
"""
Created on Fri Jan 10 20:25:00 2014
@author: duan&ian
"""
import cv2
import numpy as np

flags = [i for i in dir(cv2) if "COLOR_" in i]
# print(flags)

cap=cv2.VideoCapture(0)

# 获取绿色hsv
green=np.uint8([[[0,255,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print("hsv_green: ", hsv_green)

red=np.uint8([[[255,0,0]]])
hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print("hsv_red: ", hsv_red)

while(1):
    # 获取每一帧
    ret,frame=cap.read()

    # 转换到HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # 设定蓝色的阈值
    lower_blue=np.array([100,50,50])
    upper_blue=np.array([130,255,255])

    lower_red=np.array([0,50,50])
    upper_red=np.array([60,255,255])

    # 根据阈值构建掩模
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    mask2=cv2.inRange(hsv,lower_red,upper_red)

    # 对原图像和掩模进行位运算
    res=cv2.bitwise_and(frame,frame,mask=mask)
    res2=cv2.bitwise_and(frame,frame,mask=mask2)
    
    # 蓝红  居然意外可以拿到人像哈哈哈
    res=cv2.bitwise_or(res,res2)

    # 显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('mask2',mask2)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
# 关闭窗口
cv2.destroyAllWindows()