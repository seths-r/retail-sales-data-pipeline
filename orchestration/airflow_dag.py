from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'sethu_prakash',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 24),
    'retries': 1,
}

dag = DAG('retail_sales_pipeline', default_args=default_args, schedule_interval='@daily')

t1 = BashOperator(
    task_id='data_ingestion',
    bash_command='python /path/to/sethu_prakash/data_ingestion/kafka_consumer.py',
    dag=dag
)

t2 = BashOperator(
    task_id='data_processing',
    bash_command='python /path/to/sethu_prakash/data_processing/etl_pipeline.py',
    dag=dag
)

t3 = BashOperator(
    task_id='data_storage',
    bash_command='python /path/to/sethu_prakash/data_storage/load_data.py',
    dag=dag
)

t1 >> t2 >> t3
