import cv2
from matplotlib import pyplot as plt

class ImageHi:
    """
    add 添加图像, show展示.

    按s显示下一张, Esc 退出展示, 再次Esc退出界面终结程序
    """
    def __init__(self):
        self.image_list = []
        self.num = 0
    def add(self, img, img_name):
        img_name = img_name or ''
        self.image_list.append((img_name, img))
    def show(self):
        sign = 0
        if self.image_list:
            sign = 1
            cv2.imshow(self.image_list[0][0], self.image_list[0][-1])
            while 1:
                k = cv2.waitKey(1)&0xFF
                if k == ord('s'):
                    self.num += 1
                    if self.num >= len(self.image_list):
                        self.num = 0
                    cv2.imshow(self.image_list[self.num][0], self.image_list[self.num][-1])
                elif k == 27:
                    # Esc
                    break
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return sign

class ImageGo:
    def __init__(self):
        self.num = 0
        self.img_list = []
    def add(self, img, pos=1, name=None):
        self.num += 1
        if pos < self.num:
            pos = self.num
        self.img_list.append((img, name, pos))
        return 1

    def show(self, nrows=1, ncol=0, cmap=None):
        ncols = ncol or int(self.num / nrows)
        ncols = ncols if nrows*ncols >= self.num else ncols + 1
        for img, name, pos in self.img_list:
            plt.subplot(nrows, ncols, pos)
            plt.imshow(img, cmap=cmap),plt.title(name)
            plt.xticks([]), plt.yticks([])
        plt.show()
        
iamgego = ImageGo()