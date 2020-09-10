import pika

credentials = pika.PlainCredentials('hello', 'hi')
parameters = pika.ConnectionParameters('129.28.192.11', 5672, '/test', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
