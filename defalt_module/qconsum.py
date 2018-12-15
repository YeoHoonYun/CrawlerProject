# -*- coding: utf-8 -*-
import pika, time, json
# from ela_test import ela_test
from elasticsearch import Elasticsearch
import datetime

def q_consum():
    credentials = pika.PlainCredentials('admin', 'StrongPassword')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='192.168.56.101',
                                  port = 5672,
                                  credentials = credentials))

    es = Elasticsearch('localhost:9200')
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        # print(json.loads(body))
        data = json.loads(body)
        # data['timestamp'] = datetime.datetime.now()
        # res = es.index(index="crawler_test", doc_type='news', id=data["num"], body=data)
        res = es.index(index="crawler_test", doc_type='news', body=data)
        print(res['created'])

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_consume(callback, queue='hello', no_ack=True)
    try:
        channel.start_consuming()
    except:
        channel.start_consuming()

if __name__ == "__main__":
    q_consum()