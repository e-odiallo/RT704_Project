#!/usr/bin/python3
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) 
channel = connection.channel()
channel.queue_declare(queue='Hello') # Declaration/creation de la queue/file nommée
channel.basic_publish(exchange='', routing_key='hello', body='Hola Marcelo')# Ecriture
print(" it's OK ")
connection.close()
