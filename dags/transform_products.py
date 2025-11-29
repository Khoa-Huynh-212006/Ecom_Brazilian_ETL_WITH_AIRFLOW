import pandas as pd
from transformations import get_engine

def sync_products():
    mysql_engine = get_engine('mysql', 'mysql')
    pg_engine = get_engine('postgres_warehouse', 'postgres')
    query = """
        SELECT 
            product_id, 
            product_category_name, 
            product_name_lenght, 
            product_description_lenght, 
            product_weight_g 
        FROM olist_products
    """
    df = pd.read_sql(query, mysql_engine)
    df.to_sql('dim_products', pg_engine, if_exists='replace', index=False)
    print(f"Done transformation products !!!")