import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noisy.png',0)
ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# Global
for i in range(6):
    plt.subplot(6,5,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


# Block
img = img
# 中值滤波
img = cv2.medianBlur(img, 5)
#11 为 Block size, 2 为 C 值 
th1 = thresh1
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2)

titles = ['Original Image', 'Global Thresholding\n(v = 127)', 'Adaptive Mean\nThresholding', 'Adaptive Gaussian\nThresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(6,5,6+i+1+4)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


# Otsu’s
img = img
# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
#（5,5）为高斯核的大小，0 为标准差
blur = cv2.GaussianBlur(img,(5,5),0)

# 阈值一定要设为 0！
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plot all the images and their histograms

images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)', 'Original Noisy Image','Histogram',"Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
# 这里使用了 pyplot 中画直方图的方法，plt.hist, 要注意的是它的参数是一维数组
# 所以这里使用了（numpy）ravel 方法，将多维数组转换成一维，也可以使用 flatten 方法
#ndarray.flat 1-D iterator over an array.
#ndarray.flatten 1-D array copy of the elements of an array in row-major order.

for i in range(3):
    plt.subplot(6,5,i*3+1+15)
    plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3])
    plt.xticks([]), plt.yticks([])
    
    plt.subplot(6,5,i*3+2+15)
    plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1])
    plt.xticks([])
    plt.yticks([])

    plt.subplot(6,5,i*3+3+15)
    plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2])
    plt.xticks([]), plt.yticks([])

plt.show()