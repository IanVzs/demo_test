# -*- coding: utf-8 -*
"""
Created on Sat Jan 11 21:46:11 2014
@author: duan, ian
"""
import cv2
import numpy as np

from image_go import ImageGo
paint = ImageGo()

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)

# 腐蚀
erosion = cv2.erode(img, kernel, iterations = 1)

# 膨胀
dilation = cv2.dilate(img,kernel,iterations = 1)

# 开(先腐蚀再膨胀)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 闭(先膨胀再腐蚀)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 形态学梯度(膨胀腐蚀差别)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 礼帽(原始与开运算差)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽(闭运算与原始的差)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)



paint.add(img, 1, "Original")
paint.add(erosion, 2, "Erode")
paint.add(dilation, 3, "Dilate")
paint.add(opening, 4, "Opening")
paint.add(closing, 5, "Closing")

paint.show(2)

"""
# Rectangular Kernel >>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel >>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) array([[0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel >>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) array([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], dtype=uint8)
"""