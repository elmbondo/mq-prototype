import pika
import os
import json

amqp_url = os.environ.get("AMQP_URL")
params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="hello")

stock_cache = {}

def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Received: {message}")
    try:
        parts = message.split()
        sku = parts[2]
        qty = int(parts[3].split("=")[1])
        stock_cache[sku] = qty
        print(f"Cache updated -> {stock_cache}")
        with open("stock_cache.json", "w") as f:
            json.dump(stock_cache, f)
    except (IndexError, ValueError) as e:
        print(f"Could not parse message: {e}")

channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

print("Waiting for messages. Press CTRL+C to exit.")
channel.start_consuming()