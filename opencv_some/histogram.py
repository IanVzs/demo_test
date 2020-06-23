# -*-coding: utf-8-*-
"""直方图"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

from iamge_hi import iamgego

def hello_hist():
    img = cv2.imread('flower.png', 0)
    color = ('b','g','r')
    plt.hist(img.ravel(),256,[0,256])
    # 别忘了中括号 [img],[0],None,[256],[0,256]，只有 mask 没有中括号
    hist = cv2.calcHist([img], [0], None, [256], [0,256])
    print(hist) # 256x1 的数组

    #hist, bins = np.histogram(img.ravel(),256,[0,256])  # 比上者慢40倍， 坚持使用opencv函数欧耶
    # print(hist) # 256x1 的数组

    img_color = cv2.imread('flower.png')
    for i,col in enumerate(color):
        print(i, col)
        histr = cv2.calcHist([img_color], [i], None, [256], [0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])

    plt.show()

def go_hist():
    """失败的函数..."""
    img = cv2.imread('moon.png',0)
    print(img)
    #flatten() 将数组变成一维
    # aaa = img.ravel() 影响原始图
    # bbb = img.flatten()  拷贝一份原始图进行处理
    # a = (aaa == bbb) -> True
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    # 计算累积分布图
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    # plt.plot(cdf_normalized, color = 'b')
    # plt.hist(img.flatten(),256,[0,256], color = 'r')
    # plt.xlim([0,256])
    # plt.legend(('cdf','histogram'), loc = 'upper left')

    # 构建 Numpy 掩模数组，cdf 为原数组，当数组元素为 0 时，掩盖（计算时被忽略）。 
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    # 对被掩盖的元素赋值，这里赋值为 0
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    import ipdb; ipdb.set_trace()
    img2 = cdf[img]
    plt.imshow(img2, "gray")
    plt.xticks([]), plt.yticks([])
    plt.show()

def write_hist():
    """直方图均衡化"""
    img1 = cv2.imread('moon.png',0)
    img2 = cv2.imread('flower.png', 0)
    equ1 = cv2.equalizeHist(img1)
    equ2 = cv2.equalizeHist(img2)
    res1 = np.hstack((img1,equ1))
    res2 = np.hstack((img2,equ2))
    
    #stacking images side-by-side 
    cv2.imwrite('hist_res1.png',res1)
    cv2.imwrite('hist_res2.png',res2)

def write_hist_clahe():
    """自适应直方图均衡化"""
    img1 = cv2.imread('moon.png',0)
    img2 = cv2.imread('flower.png', 0)

    # 均衡化
    equ1 = cv2.equalizeHist(img1)
    equ2 = cv2.equalizeHist(img2)

    # 自适应均衡化
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    calhe_img1 = clahe.apply(img1)
    calhe_img2 = clahe.apply(img2)
    
    #stacking images side-by-side 
    cl11 = np.hstack((img1,equ1, calhe_img1))
    cl12 = np.hstack((img2,equ2, calhe_img2))
    
    cv2.imwrite('clahe_hist_1.jpg',cl11)
    cv2.imwrite('clahe_hist_2.jpg',cl12)

# hello_hist()
# go_hist()
# write_hist()
write_hist_clahe()