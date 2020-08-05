from matplotlib import pyplot as plt

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

