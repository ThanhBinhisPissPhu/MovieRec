from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import json
import time
import logging
from streamer import CSVStreamerPandas
from kafka import KafkaProducer

rating_path = 'new_streaming_data/new_streaming_ratings.csv'
review_path = 'new_streaming_data/new_streaming_reviews.csv'

default_args = {
    'owner': 'thanhbinh',
    'start_date': datetime(2024, 11, 10),
}

rating_streamer = CSVStreamerPandas(rating_path)
# review_streamer = CSVStreamerPandas(review_path)

def get_rating_data(streamer):

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() - curr_time > 15:
            break
        try:
            new_data = streamer.get_next_row()
            producer.send('ratings', json.dumps(new_data).encode('utf-8'))
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            continue


def get_review_data(streamer):
    new_data = streamer.get_next_row()
    print(new_data)


with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='streaming_data_from_csv',
        python_callable=get_rating_data,
    )


