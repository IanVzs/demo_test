# -*- coding: utf-8 -*
"""
Created on Sun Jan 12 11:01:40 2014
@author: duan, ian
"""
import cv2
import numpy as np

from image_go import ImageGo
paint = ImageGo()

def hi_gradient():
    img=cv2.imread('dave_num.png',0)
    #cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致 np.uint8
    #laplacian=cv2.Laplacian(img, cv2.CV_64F)
    laplacian = cv2.Laplacian(img, -1, ksize=5)

    # 参数 1,0 为只在 x 方向求一阶导数，最大可以求 2 阶导数。
    #sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobelx=cv2.Sobel(img, -1, 1, 0, ksize=5)
    # 参数 0,1 为只在 y 方向求一阶导数，最大可以求 2 阶导数。
    sobely=cv2.Sobel(img, -1, 0, 1, ksize=5)

    paint.add(img, 1, name="Original")
    paint.add(laplacian, 2, name="Laplacian")
    paint.add(sobelx, 3, name="Sobelx")
    paint.add(sobely, 4, name="Sobely")


    # Canny 边缘检测
    edges = cv2.Canny(img, threshold1=100, threshold2=200)
    img2=cv2.imread('ml.png',0)
    edges2 = cv2.Canny(img2, threshold1=100, threshold2=200)
    paint.add(edges, 5, name="Canny")
    paint.add(edges2, 6, name="Canny2")

    paint.show(2, 'gray')

def go_gradient():
    """滑块调节阈值, 进行边缘提取"""
    global sign
    global threshold1
    global threshold2

    img=cv2.imread('ml.png',0)
    sign = 0
    threshold1 = 0
    threshold2 = 0

    def draw_img(img):
        cv2.imshow("image", img)

    def canny_image(img, v1, v2):
        """对图像进行canny提取边缘操作"""
        print(v1, v2)
        edges = cv2.Canny(img, threshold1=v1, threshold2=v2)
        return edges

    def chage_threshold1(x):
        global sign
        global threshold1
        global threshold2
        sign = 1
        threshold1 = x
        

    def chage_threshold2(x):
        global sign
        global threshold1
        global threshold2
        sign = 1
        threshold2 = x

    cv2.namedWindow("image")
    cv2.createTrackbar('threshold1', "image", 0, 320, chage_threshold1)
    cv2.createTrackbar('threshold2', "image", 0, 320, chage_threshold2)

    draw_img(img)
    while(1):
        if sign:
            edges = canny_image(img, threshold1, threshold2)
            draw_img(edges)
        else:
            pass
        sign = 0
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #hi_gradient()
    go_gradient()