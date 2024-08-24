from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('retail_sales', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', value_deserializer=lambda v: json.loads(v.decode('utf-8')))

def consume_data():
    for message in consumer:
        print(f"Consumed: {message.value}")

if __name__ == "__main__":
    consume_data()
