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
