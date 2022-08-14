"""
失败 不能用
"""
import cv2
import numpy as np

def illum(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(img_gray, 180, 255, 0)
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    """
    # opencv 3.4:
        ret: 
            img, contours, hierarchy
    # opencv 4.0
        ret:
            contours, hierarchy
    """
    img_zero = np.zeros(img.shape, dtype=np.uint8)
    
    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        # x，y是矩阵左上点的坐标，w，h是矩阵的宽和高
        img_zero[y:y+h, x:x+w] = 255
    mask = img_zero
    result = cv2.illuminationChange(img, mask, alpha=1, beta=2)
    for i in [img, mask, result]:
        cv2.imshow("", i)
        cv2.waitKey()

    return result

if __name__ == "__main__":
    import os
    home = os.environ.get("HOME")
    path = os.path.join(home, "Desktop", "3.png")

    img = cv2.imread(path)
    rst = illum(img)

    # cv2.imshow("", img)
    # cv2.waitKey()

    cv2.imshow("", rst)
    cv2.waitKey()

    cv2.destroyAllWindows()