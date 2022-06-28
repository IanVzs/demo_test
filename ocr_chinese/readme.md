### Get Data
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst_gnt.zip
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn_gnt.zip

### Thanks
https://blog.csdn.net/qq_31417941/article/details/97915035
https://github.com/chenyr0021/Chinese_character_recognition

# PaddleOCR
端对端的对于横平竖直的文字识别效果很差...而且貌似对于数据要求很高
尤其是标注方式，貌似很强要求14点标记的方式

对于弯曲旋转的文字识别效果较好(彩虹🌈形状排布的文字)
## 标签转换
`trans_img_label.py`
### 说明
将 PaddleOCR 标注工具 PPOCRLabel
导出的[矩形]标注数据 修改为文字识别所用数据集
```bash
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
```
