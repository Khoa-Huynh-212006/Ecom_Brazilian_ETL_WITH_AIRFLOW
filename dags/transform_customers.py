import pandas as pd
from transformations import get_engine 

def sync_customers():
    mysql_engine = get_engine('mysql', 'mysql')
    pg_engine = get_engine('postgres_warehouse', 'postgres')

    query = """
        SELECT customer_id, customer_unique_id, customer_city, customer_state 
        FROM olist_customers
    """
    df = pd.read_sql(query, mysql_engine)

    df.to_sql('dim_customers', pg_engine, if_exists='replace', index=False)
    print(f"Done transformation customers !!!")