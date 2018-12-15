from pykafka import KafkaClient

client = KafkaClient(hosts='192.168.56.101:6667')
topic = client.topics['crawler_test']
consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
         print message.offset, message.value