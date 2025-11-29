from airflow.hooks.base import BaseHook
import pandas as pd
import os 
from sqlalchemy import create_engine

dataset_path = '/tmp/dataset'

def load():
    conn_airflow = BaseHook.get_connection('mysql')
    conn_str = f'mysql+mysqlconnector://{conn_airflow.login}:{conn_airflow.password}@{conn_airflow.host}:{conn_airflow.port}/{conn_airflow.schema}'
    engine = create_engine(conn_str)

    files_to_tables = {
        "olist_customers_dataset.csv": "olist_customers",
        "olist_geolocation_dataset.csv": "olist_geolocation",
        "olist_sellers_dataset.csv": "olist_sellers",
        "olist_products_dataset.csv": "olist_products",
        "olist_orders_dataset.csv": "olist_orders",
        "olist_order_items_dataset.csv": "olist_order_items",
        "olist_order_payments_dataset.csv": "olist_order_payments",
        "olist_order_reviews_dataset.csv": "olist_order_reviews",
        "product_category_name_translation.csv": "product_category_name_translation"
    }

    for file, table in files_to_tables.items():
        file_path = os.path.join(dataset_path, file)
        if not (os.path.exists(file_path)):
            print(f'không tìm thấy file {file}')
            continue

        try:
            print(f'Đang load table {table}')
            df = pd.read_csv(file_path)

            df.to_sql(
                name = table,
                con = engine,
                chunksize= 5000,
                index= False,
                if_exists = 'append'
            )
            print(f'Đã load xong data table {table} vào MySQL')
        except Exception as e:
            print(f'Lỗi này là {e}')
            raise e
        
    print('Đã load thành công toàn bộ bảng')   

