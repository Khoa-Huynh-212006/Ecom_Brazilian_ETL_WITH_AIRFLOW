import pandas as pd
from transformations import get_engine

def create_fact_orders():
    mysql_engine = get_engine('mysql', 'mysql')
    pg_engine = get_engine('postgres_warehouse', 'postgres')

    query = """
    SELECT 
        o.order_id,
        o.customer_id,
        o.order_status,
        o.order_purchase_timestamp,
        COUNT(oi.order_item_id) as total_items,
        SUM(op.payment_value) as total_payment_value
    FROM olist_orders o
    LEFT JOIN olist_order_items oi ON o.order_id = oi.order_id
    LEFT JOIN olist_order_payments op ON o.order_id = op.order_id
    GROUP BY o.order_id, o.customer_id, o.order_status, o.order_purchase_timestamp
    LIMIT 50000; -- Bỏ LIMIT khi chạy Production
    """
    
    df = pd.read_sql(query, mysql_engine)
    
    df.to_sql('fct_orders', pg_engine, if_exists='append', index=False, chunksize=5000)
    print(f"Done transformation orders !!!")