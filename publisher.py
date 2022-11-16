#!/usr/bin/env python

# Sent json file data to RabbitMQ
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='reddit')

import json

# data = []
# for line in open('test.json', 'r'):
#     data.append(json.loads(line))
file = 'result.json'
with open(file, "r") as r:
    response = r.read()
    response = response.replace('\n', '')
    response = response.replace('}{', '},{')
    response = "[" + response + "]"
    data = json.loads(response)
    result = ''.join(map(str, data))

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=result,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
print(" [x] Sent 'Reddit Crawling Data'")
connection.close()
