# 说明
需求来自于要做`pyinstall`打包成的`exe`安装程序

## 解压zip 创建启动快捷方式
所以制作了解压zip,自动创建快捷方式的脚本
`zip_file.py`

## 封装gui进度条
`gui.py`
### 需要完善的
- 线程执行`zip_file`内容
- 信号传导进度
- 进度显示

## 将ui文件转为py
`pyside6-uic install.ui -o ui_install.py`
