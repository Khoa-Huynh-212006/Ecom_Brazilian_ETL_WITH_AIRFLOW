from airflow import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta 
from airflow.operators.python import PythonOperator


def delete_table():
    hook = MySqlHook(mysql_conn_id = 'mysql' , local_infile=True)

    tables = [
        'olist_customers',
        'olist_geolocation',
        'olist_order_items',
        'olist_order_payments',
        'olist_order_reviews',
        'olist_orders',
        'olist_products',
        'olist_sellers',
        'product_category_name_translation'
    ]


    for i in tables:
        try:
            hook.run(f'DROP TABLE IF EXISTS {i};')
            print(f'Đã drop table {i}!')
        except Exception as e:
            print(f'table {i} Lỗi {e}')

