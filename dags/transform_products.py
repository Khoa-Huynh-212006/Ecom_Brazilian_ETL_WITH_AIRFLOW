import pandas as pd
from transformations import get_engine

def trans_products():
    mysql_engine = get_engine('mysql', 'mysql')
    postgres_engine = get_engine('postgres_warehouse', 'postgres')
    sql = """
    SELECT product_id, product_category_name, product_name_lenght AS name_length, 
        product_description_lenght AS description_length,
        product_photos_qty AS photos_quantity, product_weight_g AS weight, 
        product_length_cm AS length, product_height_cm AS height, product_width_cm AS width
    FROM olist_products 
    """
    df = pd.read_sql(sql, mysql_engine)
    df.to_sql('dim_products', postgres_engine, if_exists='replace', index=False)
    print("Bảng dim_products đã được load vào postgres warehouse")