# 记得安装
因为其中指定了版本,所以可以根据自己需求删除某些东西
```bash
pip install -r `yolov5/requirements.txt`
```
# 运行时提示的需要下载的东西
```
Downloading https://ultralytics.com/assets/Arial.ttf to /home/ian/.config/Ultralytics/Arial.ttf...
YOLOv5 🚀 v6.0-115-gbc48457 torch 1.10.0+cu102 CPU

Downloading https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt to /home/ian/projects/demo_test/opencv_some/yolo5v_test/yolov5/yolov5s.pt...
100%|██████████████████████████████████████| 14.0M/14.0M [00:02<00:00, 5.93MB/s]

```

# 训练
## 标注
- 去[标注平台](https://app.roboflow.com/)
- 注册用户、新建项目、上传图片、标注、导出标注数据、下载标注数据
- 存为`axie.v1i.yolov5pytorch`
## 训练
```bash
cp axie.v1i.yolov5pytorch/data.yaml .
cp axie.v1i.yolov5pytorch/train/ .
cd yolov5/
python train.py --img 416 --batch 16 --epochs 3 --data ../data.yaml --weights yolov5s.pt
```
## 验证
具体`exp`根据实际情况调整
```bash
python detect.py --source=../train/images/ --weights=runs/train/exp5/weights/best.pt
```

## 但是
我用这些东西失败了/哭.... 压根识别不了
# 使用方法
## 标注工具
[labelImg](https://github.com/tzutalin/labelImg)
- 选择yolo模式, 关闭`Use default label`

标注完成后将标注文件整理为以下数据格式.
## 标注文件目录
```tree
yolov5/
datasets/
├── bigcard
│   ├── classes.txt
│   ├── images
│   │   └── train2017
│   │       ├── a1.jpeg
│   │       ├── a2.jpeg
│   │       ├── a3.jpeg
│   │       ├── a4.jpeg
│   │       ├── a5.jpeg
│   │       ├── a6.jpeg
│   │       ├── a7.jpeg
│   │       ├── a8.jpeg
│   │       └── a9.jpeg
│   └── labels
│       ├── train2017
│       │   ├── a1.txt
│       │   ├── a2.txt
│       │   ├── a3.txt
│       │   ├── a4.txt
│       │   ├── a5.txt
│       │   ├── a6.txt
│       │   ├── a7.txt
│       │   ├── a8.txt
│       │   └── a9.txt
│       └── train2017.cache
└── card
    ├── classes.txt
    ├── images
    │   └── train2017
    │       ├── a1.jpeg
    │       ├── a2.jpeg
    │       ├── a3.jpeg
    │       ├── a4.jpeg
    │       ├── a5.jpeg
    │       ├── a6.jpeg
    │       ├── a7.jpeg
    │       ├── a8.jpeg
    │       └── a9.jpeg
    └── labels
        ├── train2017
        │   ├── a1.txt
        │   ├── a2.txt
        │   ├── a3.txt
        │   ├── a4.txt
        │   ├── a5.txt
        │   ├── a6.txt
        │   ├── a7.txt
        │   ├── a8.txt
        │   └── a9.txt
        └── train2017.cache
```
## Data 文件配置
`yolov5/data/card.yaml`修改自`yolov5/data/coco128.yaml`
```
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
# COCO128 dataset https://www.kaggle.com/ultralytics/coco128 (first 128 images from COCO train2017)
# Example usage: python train.py --data coco128.yaml
# parent
# ├── yolov5
# └── datasets
#     └── coco128  ← downloads here


# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: ../datasets/card  # dataset root dir
train: images/train2017  # train images (relative to 'path') 128 images
val: images/train2017  # val images (relative to 'path') 128 images
test:  # test images (optional)

# Classes
nc: 6  # number of classes
names: [ "bp", "sr", "us", "al", "ab", "sc"]


# Download script/URL (optional)
#download: https://ultralytics.com/assets/coco128.zip
```
## 开始训练和测试
```bash
# 训练
python train.py --img 640 --batch 8 --epochs 500 --data data/bigcard.yaml --cfg ./models/yolov5s.yaml --weights ./yolov5s.pt
# 测试
python detect.py --source ../datasets/card/images/train2017/a1.jpeg --weights ./runs/train/exp13/weights/best.pt
```

