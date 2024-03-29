# Hello World!
from airflow import DAG
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def print_hello():
    print('Hello world from first Airflow DAG!')

dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2023, 10, 20), catchup=False)

hello_operator = PythonOperator(task_id='hello_world', python_callable=print_hello, dag=dag)

hello_operator