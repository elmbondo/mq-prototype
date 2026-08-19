 Message Queue Prototype



Solo learning exercise for Assignment 1 of the Meridian Pivot sprint (PLP).

Demonstrates a producer/consumer pattern using RabbitMQ (via CloudAMQP) and Python's `pika` library.



 Files

\- `producer.py` - publishes stock update messages to a queue

\- `consumer.py` - consumes messages, builds an in-memory stock cache, persists it to JSON

\- `query\_stock.py` - reads the cached stock data and answers a lookup by SKU



 Setup

Requires an `AMQP\_URL` environment variable pointing to a RabbitMQ broker.

