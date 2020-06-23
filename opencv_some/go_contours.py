import cv2
import numpy as np

from iamge_hi import ImageHi
imagehi = ImageHi()

img = cv2.imread("star.png")
def convexityAndpoint():
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 2, 1)
    cnt = contours[0]

    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)

    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        cv2.line(img,start,end,[0,255,0],2)
        cv2.circle(img,far,5,[0,0,255],-1)

    dist = cv2.pointPolygonTest(cnt,(50,50),measureDist=False)
    cv2.circle(img,(50, 50),3,[255,255,100],-1)
    print(f"50^2 dist: {dist}")
    dist = cv2.pointPolygonTest(cnt,(200,200),measureDist=False)
    cv2.circle(img,(200, 200),3,[255,255,100],-1)
    print(f"200^2 dist: {dist}")
    dist = cv2.pointPolygonTest(cnt,(500,500),measureDist=False)
    cv2.circle(img,(300, 300),3,[255,255,100],-1)
    print(f"300^2 dist: {dist}")

    # 测距, measureDist: True:测量距离, False:相对关系(内+1外-1上0)
    imagehi.add(img, img_name="img")
    imagehi.show()

def matchShape():
    img1 = cv2.imread('star.png',0)
    img2 = cv2.imread('star2.png',0)
    ret, thresh = cv2.threshold(img1, 127, 255,0)
    ret, thresh2 = cv2.threshold(img2, 127, 255,0)
    
    contours, hierarchy = cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    
    contours, hierarchy = cv2.findContours(thresh2,2,1)
    cnt2_list = []
    for i in range(len(contours)):
        cnt2 = contours[i]
        cnt2_list.append(cnt2)
    
    for i in range(cnt2_list[-2].shape[0]):
        x, y = cnt2_list[-2][i][0]
        cv2.circle(img2,(x, y),3,[255,255,100],-1)
    for n, cnt2 in enumerate(cnt2_list):
        ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
        print(n, ret)

    imagehi.add(img2, "img2")
    imagehi.show()
# convexityAndpoint()
matchShape()

