```bash
g++ -Wall server.cpp -o server && g++ -Wall client.cpp -o client
./server localhost 1234
./client localhost 1234
```
在`client`端输入东西后回车发送

在`server`端默认有延迟`1s`处理.

也没啥高级的么...不就是处理完成回调. 冠名`多路复用`emmmmm...