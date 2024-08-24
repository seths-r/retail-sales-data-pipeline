from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def produce_data():
    sample_data = {
        'order_id': 12345,
        'product_id': 'ABC123',
        'quantity': 3,
        'price': 29.99,
        'order_date': '2024-08-24'
    }
    while True:
        producer.send('retail_sales', sample_data)
        print(f"Produced: {sample_data}")
        time.sleep(5)

if __name__ == "__main__":
    produce_data()
