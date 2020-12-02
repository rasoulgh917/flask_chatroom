#Import Libs
import pika
import json

#Create function for sending message in new_user queue
def send_new_user(username, email, first_name, last_name, password):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='new_user')
    data = {"username": username, "email": email, "first_name": first_name, "last_name": last_name, "password": password}
    channel.basic_publish(exchange='', routing_key='new_user', body=(json.dumps(data)))
    connection.close()