# PaddleX
## mobileNetV2.py
```bash
wget -P ~/Downloads/ https://bj.bcebos.com/paddlex/datasets/vegetables_cls.tar.gz
tar xzf ~/Downloads/vegetables_cls.tar.gz -C ~/Downloads/

pip install paddlex -i https://mirror.baidu.com/pypi/simple
python mobileNetV2.py --output_dir=./output --data_dir=~/Downloads
```
**注意:** 其实并不支持`~`路径.

### 训练过程中可视化查看过程
```bash
pip install --upgrade --pre visualdl
visualdl --logdir {output_dir}/vegetables/mobilenetv2/vdl_log --port 8080 --language zh
```

## mobileNetV3_ssld
```
wget -P ~/Downloads/ https://bj.bcebos.com/paddlex/interpret/mini_imagenet_veg.tar.gz
tar xzf ~/Downloads/mini_imagenet_veg.tar.gz -C ~/Downloads/
```
