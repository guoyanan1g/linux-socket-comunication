# linux-socket-comunication
多线程的linux套接字通信程序，同样适用于windows。
该程序实现了多线程收发消息，共享变量的简单demo，根据需要稍微改改就行。
该程序功能如下：
+ 1.服务器端存放共享变量var_temp,该值从终端（键盘）中输入。
+ 2.4个客户端不断向服务器端发送数据请求（固定内容"get current var_temp")
+ 3.服务器点接收到客户端请求(" get current var_temp")后，将var_temp的值减1后发给请求的客户端
+ 4.客户端收到服务器端的数据后输出到终端上（显示器）
+ 5.当服务器端的var_temp值为0，向请求的客户端发送 "over"
+ 6.客户端收到"over"后，退出。

运行：
python3 server.py，然后输入var_temp的值，开始监听
python3 client.py
