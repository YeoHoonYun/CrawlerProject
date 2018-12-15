# -*- coding: utf-8 -*-
import pika, time

def q_publish(text):
    credentials = pika.PlainCredentials('admin', 'StrongPassword')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='192.168.56.101',
                                  port = 5672,
                                  credentials = credentials))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=str(text))
    connection.close()
if __name__ == "__main__":
    q_publish('test')

