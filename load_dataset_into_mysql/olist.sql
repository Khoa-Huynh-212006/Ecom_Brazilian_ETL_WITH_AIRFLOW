SET FOREIGN_KEY_CHECKS=0;
-- Customers
DROP TABLE IF EXISTS olist_customers;
CREATE TABLE olist_customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(100),
    customer_state CHAR(2)
);


-- Orders
DROP TABLE IF EXISTS olist_orders;
CREATE TABLE olist_orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50),
    order_status VARCHAR(30),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP,
    CONSTRAINT fk_customers_orders FOREIGN KEY (customer_id) REFERENCES olist_customers(customer_id)
);

-- Geolocation
DROP TABLE IF EXISTS olist_geolocation;
CREATE TABLE olist_geolocation (
    geolocation_zip_code_prefix INT PRIMARY KEY,
    geolocation_lat DECIMAL(10,6),
    geolocation_lng DECIMAL(10,6),
    geolocation_city VARCHAR(100),
    geolocation_state CHAR(2)
);

-- Products
DROP TABLE IF EXISTS olist_products;
CREATE TABLE olist_products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name VARCHAR(100),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

-- Sellers
DROP TABLE IF EXISTS olist_sellers;
CREATE TABLE olist_sellers (
    seller_id VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix INT,
    seller_city VARCHAR(100),
    seller_state CHAR(2),
    CONSTRAINT df_sellers_geolocation FOREIGN KEY (seller_zip_code_prefix) REFERENCES olist_geolocation(geolocation_zip_code_prefix)
);


-- Order Items
DROP TABLE IF EXISTS olist_order_items;
CREATE TABLE olist_order_items (
    order_id VARCHAR(50),
    order_item_id INT PRIMARY KEY,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date TIMESTAMP,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),
    CONSTRAINT fk_order_id FOREIGN KEY (order_id) REFERENCES olist_orders(order_id),
    CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES olist_products(product_id),
    CONSTRAINT fk_seller_id FOREIGN KEY (seller_id) REFERENCES olist_sellers(seller_id)
);




-- Payments
DROP TABLE IF EXISTS olist_order_payments;
CREATE TABLE olist_order_payments (
    order_id VARCHAR(50),
    payment_sequential INT,
    payment_type VARCHAR(50),
    payment_installments INT,
    payment_value DECIMAL(10,2),
    CONSTRAINT fk_order_payments FOREIGN KEY (order_id) REFERENCES olist_orders(order_id)
);

-- Reviews
DROP TABLE IF EXISTS olist_order_reviews;
CREATE TABLE olist_order_reviews (
    review_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50),
    review_score INT,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP,
    CONSTRAINT fk_order_reviews FOREIGN KEY (order_id) REFERENCES olist_orders(order_id)
);


-- Product Category Translation
DROP TABLE IF EXISTS product_category_name_translation;
CREATE TABLE product_category_name_translation (
    product_category_name VARCHAR(100),
    product_category_name_english VARCHAR(100)
);

SET FOREIGN_KEY_CHECKS=1;