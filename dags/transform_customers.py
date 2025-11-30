import pandas as pd
from transformations import get_engine 

def trans_customers():
    mysql_engine = get_engine('mysql', 'mysql')
    postgres_engine = get_engine('postgres_warehouse', 'postgres')

    sql = """
    SELECT customer_id, customer_unique_id, customer_zip_code_prefix AS zip_code_prefix,
        customer_city  AS city, customer_state  AS state
    FROM olist_customers;
    """

    df = pd.read_sql(sql, mysql_engine)
    df.to_sql('dim_customers', postgres_engine, index= False, if_exists= 'append', chunksize= 5000)
    print('Bảng dim_customers đã được load vào postgres warehouse')
