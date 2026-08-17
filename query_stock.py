import json

sku = input("Enter SKU to check stock (e.g. SKU-001): ")

try:
    with open("stock_cache.json", "r") as f:
        cache = json.load(f)
    if sku in cache:
        print(f"{sku} has {cache[sku]} units in stock")
    else:
        print(f"{sku} not found in cache")
except FileNotFoundError:
    print("No stock data yet — run the consumer first to receive messages")