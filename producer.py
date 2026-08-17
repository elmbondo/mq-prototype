import pika
import os

amqp_url = os.environ.get("AMQP_URL")
params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="hello")

messages = [
    "Stock update: SKU-001 qty=42",
    "Stock update: SKU-002 qty=0",
    "Stock update: SKU-003 qty=17",
]

for msg in messages:
    channel.basic_publish(exchange="", routing_key="hello", body=msg)
    print(f"Sent: {msg}")

connection.close()