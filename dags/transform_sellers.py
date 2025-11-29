import pandas as pd
from transformations import get_engine

def sync_sellers():
    mysql_engine = get_engine('mysql', 'mysql')
    pg_engine = get_engine('postgres_warehouse', 'postgres')

    query = "SELECT seller_id, seller_city, seller_state FROM olist_sellers"
    df = pd.read_sql(query, mysql_engine)
    

    df.to_sql('dim_sellers', pg_engine, if_exists='replace', index=False)
    print(f"Done transformation sellers !!!")