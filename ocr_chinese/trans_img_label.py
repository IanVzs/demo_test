"""
将 PaddleOCR 标注工具 PPOCRLabel
导出的[矩形]标注数据 修改为文字识别所用数据集

$ ls
rec                test               train              trans_img_label.py

$ tree rec -L 1
rec
├── rec_gt_test.txt
├── rec_gt_train.txt
├── test
└── train

$ tree | grep -v png
.
├── rec
│   ├── rec_gt_test.txt
│   ├── rec_gt_train.txt
│   ├── test
│         ├── *png
│   └── train
│         ├── *png
├── test
│   ├── Cache.cach
│   ├── Label.txt
│   └── fileState.txt
│   └── *png
├── train
│   ├── Cache.cach
│   ├── Label.txt
│   └── fileState.txt
│   └── *png
└── trans_img_label.py
"""
import os
import cv2
import json
import uuid
import random

NAME_LIST = []
def split_img(root_path, img_path, label_data):
    """
    分割图像, 保存分割后的小图后返回保存路径
    str, str -> str
    """
    try:
        img = cv2.imread(img_path)
        label_data = json.loads(label_data)
        img_name = os.path.split(img_path)[-1]
        img_name = img_name.split('.')[0]
        for one_data in label_data:
            points = one_data["points"]
            transcription = one_data["transcription"]
            x_min = x_max = y_min = y_max = 0
            for i in points:
                x, y = i
                if x >= x_max:
                    x_max = x
                elif x_min == 0 or x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                elif y_min == 0 or y < y_min:
                    y_min = y
            x_min -= random.randint(0, 5)
            x_max += random.randint(0, 5)
            y_min -= random.randint(0, 5)
            y_max += random.randint(0, 5)
            if x_min <= 0:
                x_min = 0
            if y_min <= 0:
                y_min = 0
            if x_max >= img.shape[1]:
                x_max = img.shape[1]
            if y_max >= img.shape[0]:
                y_max = img.shape[0]

            new_img_name = f"{img_name}_{transcription}.png"
            while new_img_name in NAME_LIST:
                new_img_name = f"{img_name}_{transcription}_{str(uuid.uuid4()).split('-')[0]}.png"
            NAME_LIST.append(new_img_name)
            save_path = os.path.join("rec", root_path, new_img_name)
            img_transcription = img[y_min: y_max, x_min: x_max]
            cv2.imwrite(save_path, img_transcription)
            
            new_line = f"{os.path.join('train_data', save_path)}\t{transcription}\n"
            print(f"save {save_path}  ->  {new_line}")
            return new_line
    except Exception as err:
        import ipdb; ipdb.set_trace()
        print(f"fuck {img_path}\t\t{err}")
        return ''

def main(path):
    if not os.path.isdir("rec"):
        os.mkdir("rec")
    if not os.path.isdir( os.path.join("rec", "test") ):
        os.mkdir( os.path.join("rec", "test") )
    if not os.path.isdir( os.path.join("rec", "train") ):
        os.mkdir( os.path.join("rec", "train") )
    path_label = os.path.join(path, "Label.txt")
    
    new_label_lines = []
    with open(path_label, "r") as f:
        for line in f:
            if "\t" not in line:
                continue
            img_path, label_data = line.split("\t")
            new_line = split_img(path, img_path, label_data)
            if new_line:
                new_label_lines.append( new_line )

    with open( os.path.join("rec", f"rec_gt_{path}.txt") , "w") as f:
        for line in new_label_lines:
            f.write(line)




def test_label_right(path):
    label_path = os.path.join("rec", f"rec_gt_{path}.txt")
    with open(label_path) as f:
        for line in f:
            _path = line.split("\t")[0]
            _path = _path.replace("train_data/", '')
            if os.path.exists(_path):
                # print('.', end='')
                continue
            else:
                print(f"this file miss: {_path}")
                raise
    print(f"{path} pass")
                

if "__main__" == __name__:
    # main("test")
    # main("train")
    test_label_right("test")
    test_label_right("train")