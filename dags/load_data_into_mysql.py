from airflow.hooks.base import BaseHook
import pandas as pd
from sqlalchemy import create_engine
import os


dataset_path = '/tmp/dataset' 

def load_data():
    conn_airflow = BaseHook.get_connection('mysql') 
    conn_str = f"mysql+mysqlconnector://{conn_airflow.login}:{conn_airflow.password}@{conn_airflow.host}:{conn_airflow.port}/{conn_airflow.schema}"
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

    print(f"--> Bắt đầu đọc file từ: {dataset_path}")

    for filename, table_name in files_to_tables.items():
        file_path = os.path.join(dataset_path, filename) 

        if not os.path.exists(file_path):
            print(f"Warning: Không tìm thấy file {filename}, bỏ qua.")
            continue
            
        try:
            print(f"Đang xử lý: {filename} -> Bảng: {table_name}")
            df = pd.read_csv(file_path) 
            df.to_sql(name=table_name, 
                      con=engine, 
                      if_exists='append', 
                      index=False, 
                      chunksize=5000)  
            print(f"--> Thành công: Đã insert {len(df)} dòng vào {table_name}")
        except Exception as e:
            print(f"LỖI khi load file {filename}: {e}")
            raise e
              
    print("HOÀN TẤT QUÁ TRÌNH LOAD DATA")