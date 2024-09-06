from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer('stock_prices', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', group_id='stock-group', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Initialize Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme':'http'}])

for message in consumer:
    stock_data = message.value
    print(f"Consumed: {stock_data}")

    # Index stock data in Elasticsearch
    es.index(index='stock_data', body=stock_data)
    print(f"Indexed to Elasticsearch: {stock_data}")
