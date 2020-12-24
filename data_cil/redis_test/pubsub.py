import redis

# redis-cli -h 192.168.0.202 -d 0
config = {"host": "192.168.0.202", "db": 0}
rds = redis.Redis(**config)
rds
# >>> Redis<ConnectionPool<Connection<host=192.168.0.202,port=6379,db=0>>>

rds.get("123")

pubsub = rds.pubsub()
pubsub.subscribe(["singleton.refresh_config"])
pubsub.get_message(ignore_subscribe_messages=False)
# ignore_subscribe_messages True: 忽略订阅退订channel 产生的消息
# >>> {'type': 'subscribe', 'pattern': None, 'channel': b'singleton.refresh_config', 'data': 1}

rds.publish("singleton.refresh_config","asdasd")
# >>> 1
pubsub.get_message(ignore_subscribe_messages=False)
# >>> {'type': 'message', 'pattern': None, 'channel': b'singleton.refresh_config', 'data': b'asdasd'}

pubsub.get_message(ignore_subscribe_messages=False)
pubsub.get_message(ignore_subscribe_messages=False)
pubsub.get_message(ignore_subscribe_messages=False)
pubsub.get_message(ignore_subscribe_messages=True)
rds.publish("singleton.refresh_config","asdasd")
# >>> 1

pubsub.get_message(ignore_subscribe_messages=True)
# >>> {'type': 'message', 'pattern': None, 'channel': b'singleton.refresh_config', 'data': b'asdasd'}
pubsub.get_message(ignore_subscribe_messages=True)
