# 使用配置
## 非root版
参考自: [这里](https://blog.csdn.net/codeswarrior/article/details/107511960)

1. pip安装supervisord
2. `echo_supervisord_conf > /home/ian/iand/supervisord.conf`
3. `vim supervisord.conf`
4. 检查配置中文件路径指向
5. 看情况将/tmp 或其他换为自己目录
6. `:1, 111s/tmp/home\/ian\/iand/g`
7. 文件末尾增加
```
[include]
files = conf.d/*.conf
```
8. 同`supervisord.conf`级创建: `mkdir conf.d`
9. 新建文件`demo_server.conf`, 配置如下:
```
[program:demo_server]
command=/home/ian/anaconda3/bin/python3 main.py
directory=/home/ian/demo_server/
user=ian
autostart=true
autorestart=true
killasgroup=true
stderr_logfile=/home/ian/iand/log_info/demo_server.log
stdout_logfile=/home/ian/iand/log_error/demo_server.log
```
10. 如果需要显卡还需要加上这句话
```
environment=CUDA_VISIBLE_DEVICES=显卡号
```

### 控制
```bash
supervisord -c supervisord.conf
supervisorctl status
supervisorctl stop
supervisorctl ...
```
**注意**： 控制命令一律只能在`supervisord.conf`同级目录下执行,否则调用的还是root的. 准确来说使用的`supervisord.conf`还是该程序默认路径下的.
