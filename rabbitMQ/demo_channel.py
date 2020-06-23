import pika

# Set the connection parameters to connect to rabbit-server1 on port 5672
# on the / virtual host using the username "guest" and password "guest"
credentials = pika.PlainCredentials('hello', 'hi')
parameters = pika.ConnectionParameters('129.28.192.11', 5672, '/test', credentials)
connection = pika.BlockingConnection(parameters)
