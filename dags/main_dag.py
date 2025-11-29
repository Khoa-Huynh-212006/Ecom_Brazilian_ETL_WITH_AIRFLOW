from airflow import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta 
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from create_table import create_table
from delete_table import delete_table
from load_into_mysql import load

from transform_dim_customers import transform_dim_customers



default_args = {
    'owner': 'Khoa Huynh',
    'retries': 0,
    'retry_delay': timedelta(seconds= 20)
}

with DAG(
    dag_id='main_dag', 
    default_args=default_args,
    start_date=datetime(2025,11,20),
    schedule_interval=None,
    catchup=False
) as dag:
    task_create_table = PythonOperator(
        task_id = 'create_table',
        python_callable = create_table
    )
    task_delete_table = PythonOperator(
        task_id = 'delete_table',
        python_callable = delete_table
    )
    task_load_data = PythonOperator(
        task_id = 'load_data',
        python_callable = load
    )
    task_delete_table >> task_create_table >> task_load_data
