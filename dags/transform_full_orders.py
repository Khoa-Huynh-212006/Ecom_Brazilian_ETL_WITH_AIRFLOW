import pandas as pd
from transformations import get_engine 

def trans_full_orders():
    mysql_engine = get_engine('mysql', 'mysql')
    postgres_engine = get_engine('postgres_warehouse', 'postgres')

    sql = """
        WITH cte_orders AS(
        SELECT ord.order_id, ord.customer_id, ord.order_status AS status,
                ord.order_purchase_timestamp AS purchase_date, ord.order_approved_at - ord.order_purchase_timestamp  AS time_approve,
                ord.order_delivered_customer_date - ord.order_approved_at   AS time_delivery, 
                CASE WHEN ord.order_delivered_customer_date > ord.order_estimated_delivery_date THEN '1'
                WHEN ord.order_delivered_customer_date > ord.order_estimated_delivery_date THEN '0' 
                END AS on_time,
                DAY(order_purchase_timestamp) AS day, MONTH(order_purchase_timestamp) AS month, YEAR(order_purchase_timestamp) AS year
        FROM olist_orders AS ord
        ), cte_ord_items AS (
        SELECT *
        FROM olist_order_items ooi
        ), cte_ord_payments AS (
        SELECT oop.order_id, oop.payment_sequential AS sequentital, oop.payment_type AS type, oop.payment_installments AS installments, oop.payment_value AS value
        FROM olist_order_payments oop
        ), cte_ord_reviews AS (
        SELECT oor.review_id , oor.order_id, oor.review_score AS score , oor.review_comment_title AS title,
                oor.review_comment_message AS message, HOUR(oor.review_answer_timestamp) - HOUR(oor.review_creation_date)  AS response_hour
        FROM olist_order_reviews oor 
        )
        SELECT ord.order_id, ord.customer_id, ord.status, ord.purchase_date, ord.time_approve, ord.time_delivery, ord.on_time, ord.day, ord.month, ord.year,
                items.order_item_id AS number_item, items.product_id, items.seller_id, items.shipping_limit_date,
                items.price, items.freight_value, payments.sequentital, payments.type, payments.installments, payments.value, 
                reviews.review_id, reviews.order_id, reviews.score, reviews.title, reviews.message, reviews.response_hour
        FROM cte_orders AS ord
        LEFT JOIN cte_ord_items AS items 
        ON ord.order_id = items.order_id 
        LEFT JOIN cte_ord_payments AS payments 
        ON ord.order_id = payments.order_id
        LEFT JOIN cte_ord_reviews AS reviews 
        ON ord.order_id = reviews.order_id

    """

    df = pd.read_sql(sql, mysql_engine)
    df.to_sql('dim_full_orders', postgres_engine, index= False, if_exists= 'append', chunksize= 5000)
    print('Bảng dim_full_orders đã được load vào postgres warehouse')
