# -*- coding: utf-8 -*
"""
Created on Sat Jan 11 19:43:04 2014
@author: duan, ian
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.png')
kernel = np.ones((5,5), np.float32)/25

# cv.Filter2D(src, dst, kernel, anchor=(-1, -1))
# ddepth –desired depth of the destination image;
# if it is negative, it will be the same as src.depth();
# the following combinations of src.depth() and ddepth are supported:
# src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
# src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F #src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
# src.depth() = CV_64F, ddepth = -1/CV_64F #when ddepth=-1, the output image will have the same depth as the source.
dst = cv2.filter2D(img,-1,kernel)
plt.subplot(241)
plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(242)
plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])


# 归一化
blur = cv2.blur(img,(5,5))
plt.subplot(243)
plt.imshow(blur),plt.title('Blurred')
# cv2.boxFilter(img, (5,5), normalize=False)
plt.xticks([]), plt.yticks([])

# 高斯模糊
gao_kernel = cv2.getGaussianKernel(5, 0)
print(gao_kernel)
blur_gaussian = cv2.GaussianBlur(img, (5, 5), 0)
plt.subplot(244)
plt.imshow(blur_gaussian),plt.title('GaussianBlur')
# cv2.boxFilter(img, (5,5), normalize=False)
plt.xticks([]), plt.yticks([])

# 中值模糊(去除椒盐噪声)
blur_midian = cv2.medianBlur(img, 5)
plt.subplot(245)
plt.imshow(blur_midian),plt.title('MidianBlur')

# 双边滤波(保持边界清晰)   高斯权重+灰度相似
blur_bilateral = cv2.bilateralFilter(img,9,75,75)
plt.subplot(246)
plt.imshow(blur_bilateral),plt.title('MidianBlur')

plt.show()
