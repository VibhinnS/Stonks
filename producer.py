from kafka import KafkaProducer
import requests
import json
import time

API_KEY = '0N7K0B5VPZB3MCNR'
STOCK_SYMBOL = 'AAPL'
API_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={API_KEY}'

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def fetch_stock_data() -> None:
    response = requests.get(API_URL)
    data = response.json()

    time_series = data['Time Series (1min)']
    latest_time = list(time_series.keys())[0]
    latest_data = time_series[latest_time]
    stock_price = {
        'symbol':STOCK_SYMBOL,
        'price':latest_data['1. open'],
        'timestamp':latest_time
    }
    return stock_price

while True:
    stock_data = fetch_stock_data()
    print(f"Running Fine. Fetched {stock_data}")
    producer.send('stock_prices', stock_data)
    time.sleep(60)