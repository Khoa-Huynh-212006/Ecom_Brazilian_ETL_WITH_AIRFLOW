import pandas as pd
from transformations import get_engine

def trans_sellers():
    mysql_engine = get_engine('mysql', 'mysql')
    postgres_engine = get_engine('postgres_warehouse', 'postgres')

    sql = """
    SELECT seller_id, seller_zip_code_prefix AS zip_code_prefix, seller_city AS city, seller_state AS state
    FROM olist_sellers
    """
    df = pd.read_sql(sql, mysql_engine)
    

    df.to_sql('dim_sellers', postgres_engine, if_exists='replace', index=False)
    print("Bảng dim_sellers đã được load vào postgres warehouse")