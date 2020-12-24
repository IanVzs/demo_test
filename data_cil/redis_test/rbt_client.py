#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
import sys
import time
from multiprocessing import Process as Thread
from pika.exceptions import AMQPConnectionError, StreamLostError, NackError, ChannelWrongStateError
# pika.exceptions.ChannelWrongStateError: Channel is closed.
s = time.time()


def test(sub_p):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    """
    credentials = pika.PlainCredentials('hello', 'hi')  # 远程rabbitMQ服务器用户名，密码
    parameters = pika.ConnectionParameters('129.28.192.11', 5672, '/test', credentials)
    try:
        connection = pika.BlockingConnection(parameters)
    except AMQPConnectionError:
        print('AMQPConnectionError')
        exit(0)
    """
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)  # 声明队列，durable=True队列持久化
    cfm = channel.confirm_delivery()  # confirm 机制，消息发送失败时会引发NackError异常
    message = ' '.join(sys.argv[1:]) or "Hello World! has confirm"

    for _ in range(500):
        try:
            push_rst = channel.basic_publish(
                exchange='',
                routing_key='task_queue',
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # 消息持久化
                ))
            # print(" [x] Sent %r, push_rst = %s" % (message, push_rst))
        except StreamLostError:
            print('stream lost!')
        except NackError:
            print('Nack Error!')
    connection.close()

p_list = []
for i in range(2):
    p = Thread(target=test, name='sub_%s' % i, args=(i,))
    print('sub process %s' % p.name)
    p_list.append(p)
    p.start()
for p in p_list:
    p.join()  # join表示延时时间，也就是等待子进程的时间，当10秒过了以后，则会运行主进程。



print(time.time() - s)




