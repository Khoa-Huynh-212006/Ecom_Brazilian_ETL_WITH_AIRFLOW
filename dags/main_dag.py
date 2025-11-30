from airflow import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta 
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from create_table import create_table
from delete_table import delete_table
from load_into_mysql import load

from transformations import get_engine
from transform_customers import trans_customers
from transform_full_orders import trans_full_orders
from transform_geolocation import trans_geolocation
from transform_product_category import trans_product_category
from transform_products import trans_products
from transform_sellers import trans_sellers





default_args = {
    'owner': 'Khoa Huynh',
    'retries': 0,
    'retry_delay': timedelta(seconds= 20)
}

with DAG(
    dag_id='main_dag', 
    default_args=default_args,
    start_date=datetime(2025,11,1),
    schedule_interval='0 8 * * 1',
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
    task_trans_cus = PythonOperator(
        task_id = 'trans_cus',
        python_callable = trans_customers
    )
    task_trans_ords = PythonOperator(
        task_id = 'trans_ords',
        python_callable = trans_full_orders
    )
    task_trans_pro = PythonOperator(
        task_id = 'trans_prod',
        python_callable = trans_products
    )
    task_trans_sell = PythonOperator(
        task_id = 'trans_sellers',
        python_callable = trans_sellers
    )
    task_trans_geo = PythonOperator(
        task_id = 'trans_geolocation',
        python_callable = trans_geolocation
    )
    task_trans_pro_cate = PythonOperator(
        task_id = 'trans_product_category',
        python_callable = trans_product_category
    )
    task_delete_table >> task_create_table >> task_load_data
    task_load_data >> task_trans_cus
    task_load_data >> task_trans_ords
    task_load_data >> task_trans_pro
    task_load_data >> task_trans_sell
    task_load_data >> task_trans_geo
    task_load_data >> task_trans_pro_cate