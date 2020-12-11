import numpy as np
import cv2
 
## 图片旋转
def rotate_bound(image, angle):
    #获取宽高
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    if abs(cX) < abs(cY):
        # 根据矩形, 增加90旋转
        angle += 90
 
    # 提取旋转矩阵 sin cos 
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # 计算图像的新边界尺寸
    nW = int((h * sin) + (w * cos))
#     nH = int((h * cos) + (w * sin))
    nH = h
 
    # 调整旋转矩阵
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    return cv2.warpAffine(image, M, (nW, nH),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
 
## 获取图片旋转角度
def get_minAreaRect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    return cv2.minAreaRect(coords)
 
image_path = "54321.png"
image_path = "321.jpg"
image_path = "dsa.jpg"
# image_path = "www.jpg"
image = cv2.imread(image_path)
tuple_point, tuple_lenwid, angle = get_minAreaRect(image)
print(angle)
print(tuple_point)
rotated = rotate_bound(image, angle)
 
cv2.putText(rotated, "angle: {:.2f} ".format(angle),
    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.putText(image, '·',
    (int(tuple_point[0]), int(tuple_point[-1])), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
# show the output image
print("[INFO] angle: {:.3f}".format(angle))
cv2.imshow("imput", image)
cv2.imshow("output", rotated)
cv2.waitKey(0)
cv2.imwrite("123123.jpg", rotated)