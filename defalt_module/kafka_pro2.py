# -*- coding: utf-8 -*-
from pykafka import KafkaClient

client = KafkaClient('192.168.56.101:6667')
topic = client.topics['crawler_test']
producer = topic.get_producer()
for i in xrange(100):
    producer.produce('message {}'.format(i))