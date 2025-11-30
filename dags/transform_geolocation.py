import pandas as pd
from transformations import get_engine 

def trans_geolocation():
    mysql_engine = get_engine('mysql', 'mysql')
    postgres_engine = get_engine('postgres_warehouse', 'postgres')

    sql = """
    WITH cte_table AS (   
        SELECT ROW_NUMBER() OVER(PARTITION BY geolocation_zip_code_prefix ORDER BY geolocation_lat) AS rn,geolocation_zip_code_prefix AS zip_code_zefix,geolocation_lat AS latitude, 
            geolocation_lng AS longitude, geolocation_city AS city, geolocation_state  AS state
        FROM olist_geolocation
    )
    SELECT zip_code_zefix , latitude, longitude, city, state FROM cte_table WHERE rn = 1;
    """

    df = pd.read_sql(sql, mysql_engine)
    df.to_sql('dim_geolocation', postgres_engine, index= False, if_exists= 'append', chunksize= 5000)
    print('Bảng dim_geolocation đã được load vào postgres warehouse')
