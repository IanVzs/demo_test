import cv2
import numpy as np

def add_alpha_channel(img)  -> np.ndarray:
    """ 为jpg图像添加alpha通道 """
 
    b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
 
    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
    return img_new
 
def merge(img_background, img_frontend, l_xy) -> np.ndarray:
    """ 将png透明图像与jpg图像叠加 
        y1,y2,x1,x2为叠加位置坐标值
    """
    x1, y1 = l_xy
    x2, y2 = x1 + img_frontend.shape[1], y1 + img_frontend.shape[0]
    # 判断jpg图像是否已经为4通道
    if img_background.shape[2] == 3:
        img_background = add_alpha_channel(img_background)
    
    '''
    当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
    '''
    yy1 = 0
    yy2 = img_frontend.shape[0]
    xx1 = 0
    xx2 = img_frontend.shape[1]
 
    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > img_background.shape[1]:
        xx2 = img_frontend.shape[1] - (x2 - img_background.shape[1])
        x2 = img_background.shape[1]
    if y2 > img_background.shape[0]:
        yy2 = img_frontend.shape[0] - (y2 - img_background.shape[0])
        y2 = img_background.shape[0]
 
    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_png = img_frontend[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png
    
    # 开始叠加
    for c in range(0,3):
        img_background[y1:y2, x1:x2, c] = ((alpha_jpg*img_background[y1:y2,x1:x2,c]) + (alpha_png*img_frontend[yy1:yy2,xx1:xx2,c]))
        # cv2.imshow("img_background", img_background)
        # cv2.waitKey(0)
 
    return img_background

if __name__ == "__main__":
    img = cv2.imread("/Users/ianvzs/Desktop/scrcpy_ai/scripts/test/axie-info/axieinfo_axie.png") # 普通图如 jpg等无透明度3通道图
    logo = cv2.imread("/Users/ianvzs/Desktop/scrcpy_ai/scripts/buffs/buff_bubble.png", cv2.IMREAD_UNCHANGED) # 涵透明度4通道png图
    # import ipdb; ipdb.set_trace()
    img_gogo = merge(img, logo, (0, 0))
    cv2.imshow("nani", img_gogo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()