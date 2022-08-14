import cv2
import numpy as np

def circle_extract(dict_circle, img):
    """
    para:
        1. dict_circle = {"center": (0, 0), "radius": 0}
        2. img: np.ndarray
    """
    center = dict_circle["center"]
    radius = dict_circle["radius"]
    x, y = center
    x1, x2, y1, y2 = x-radius, x+radius, y-radius, y+radius

    row, col, channel = img.shape

    # img_new = np.zeros((row, col, 4), np.uint8) # 透明度
    # img_new[:,:,0:3] = img[:,:,0:3]

    img_circle = np.zeros((row, col, 1), np.uint8) # 单通道图
    img_circle[:,:,:] = 0 # 全透明
    img_circle = cv2.circle(img_circle, center, radius, (1), -1) # 圆形区域不透明

    # 融合
    img_new = img[y1:y2, x1:x2] * img_circle[y1:y2, x1:x2]
    return img_new


if __name__ == "__main__":
    # import os
    # home = os.environ.get("HOME")
    # path = os.path.join(home, "Downloads", "bird_img", "1654590155.975295.png")

    path = "flower.png"
    img = cv2.imread(path)

    for i in range(100, 1300, 20):
        dict_circle = {"center": (i, 200), "radius": 100}
        img_new = circle_extract(dict_circle, img)

        cv2.imshow(f"flower circle", img_new)
        if cv2.waitKey(50) == ord('q'):
            break
    cv2.destroyAllWindows()