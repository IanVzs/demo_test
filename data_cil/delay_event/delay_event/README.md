
# 使用说明

## 日志以及配置文件
在本目录下:
1. 复制`config.py.template` 到 `config.py`

在上层目录下需要具备 文件:
2. `run_delay_monitor.py`

## 运行说明
```
python3 run_delay_monitor.py --log_path=logs/delayer.log
```
### log_path
指定日志目录以及文件名

## 注
如要使用还是需要根据具体项目修改一下日志配置，无法直接使用，也可能导致配置覆盖啥的问题
