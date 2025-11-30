import pandas as pd
from transformations import get_engine

def trans_product_category():
    mysql_engine = get_engine('mysql', 'mysql')
    pg_engine = get_engine('postgres_warehouse', 'postgres')

    sql = """
        SELECT *
        FROM product_category_name_translation
    """
    df = pd.read_sql(sql, mysql_engine)
    

    df.to_sql('dim_product_category', pg_engine, if_exists='replace', index=False)
    print("Bảng dim_product_category đã được load vào postgres warehouse")