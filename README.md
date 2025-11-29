# 🇧🇷 Brazilian E-commerce ETL Pipeline with Airflow

## 🌟 1. Tổng quan (Overview)

Dự án này xây dựng một quy trình **ETL (Extract, Transform, Load)** tự động hóa hoàn toàn để xử lý dữ liệu thương mại điện tử Brazil (Olist Dataset). Hệ thống được thiết kế để chạy định kỳ vào **8:00 sáng Thứ Hai hàng tuần**, đảm bảo dữ liệu luôn được cập nhật cho các báo cáo kinh doanh.

**Mục tiêu chính:**
1.  **Extract:** Lấy dữ liệu thô từ CSV.
2.  **Load:** Đưa vào vùng đệm (Staging) trên MySQL.
3.  **Transform:** Làm sạch và chuyển đổi dữ liệu sang mô hình Star Schema.
4.  **Warehouse:** Lưu trữ kết quả cuối cùng vào PostgreSQL (Data Warehouse).

---

## 🏗️ 2. Kiến trúc & Công nghệ (Architecture & Tech Stack)

Dự án sử dụng **Docker** để đóng gói toàn bộ môi trường, đảm bảo tính nhất quán khi triển khai.

**Tech Stack:**
* **Orchestration:** Apache Airflow (v2.7+)
* **Containerization:** Docker & Docker Compose
* **Staging Database:** MySQL (Ver 8.0)
* **Data Warehouse:** PostgreSQL (Ver 16)
* **Processing:** Python (Pandas, SQL Alchemy)

### 🐳 Môi trường Docker
Hệ thống bao gồm các container cho Airflow (Webserver, Scheduler, Triggerer), MySQL và Postgres đang chạy ổn định:

![Docker Environment](images/docker_setup.png)

---

## 🔄 3. Quy trình ETL (The Pipeline Workflow)

Toàn bộ quy trình được quản lý bởi **Airflow DAG** tên là `main_dag`.

### 📊 Luồng xử lý (DAG Graph)
Dưới đây là sơ đồ thực tế của Pipeline trên giao diện Airflow. Các tác vụ chuyển đổi (Transformation) được xử lý song song để tối ưu hóa hiệu suất:

![Airflow DAG Graph](images/airflow_dag.png)

**Giải thích các Task:**
1.  `delete_table`: Xóa dữ liệu cũ để tránh trùng lặp.
2.  `create_table`: Khởi tạo lại cấu trúc bảng (Schema).
3.  `load_data`: Tải dữ liệu CSV thô vào MySQL.
4.  `trans_...` (Transformation Groups): Các tác vụ song song thực hiện làm sạch và tạo bảng Dimension/Fact.

---

## 🗃️ 4. Dữ liệu & Mô hình hóa (Data & Modeling)

### 🟢 Giai đoạn 1: Staging Area (MySQL)
Dữ liệu thô từ các file CSV (Olist dataset) được tải nguyên trạng vào MySQL để làm vùng đệm xử lý.
* **Database:** `olist`
* **Tables:** `olist_customers`, `olist_orders`, `olist_products`, v.v.

![MySQL Staging Data](images/mysql_staging.png)

### 🔵 Giai đoạn 2: Data Warehouse (PostgreSQL)
Dữ liệu sau khi được làm sạch bằng Python (Pandas) sẽ được mô hình hóa theo dạng **Star Schema** để phục vụ phân tích (Analytics Ready).
* **Schema:** `public`
* **Fact Table:** `fct_orders` (Chứa dữ liệu giao dịch).
* **Dimension Tables:** `dim_customers`, `dim_products`, `dim_sellers` (Chứa dữ liệu danh mục).

![Postgres Data Warehouse](images/postgres_dwh.png)

---

## 🚀 5. Hướng dẫn chạy (How to Run)

1.  **Clone Repository:**
    ```bash
    git clone [https://github.com/Khoa-Huynh-212006/Ecom_BRAZILIAN_ETL_WITH_AIRFLOW.git](https://github.com/Khoa-Huynh-212006/Ecom_BRAZILIAN_ETL_WITH_AIRFLOW.git)
    cd Ecom_BRAZILIAN_ETL_WITH_AIRFLOW
    ```

2.  **Chuẩn bị Dữ liệu:**
    Tải các file CSV vào thư mục `dataset/`.

3.  **Khởi chạy Docker:**
    ```bash
    docker-compose up -d
    ```

4.  **Truy cập Airflow:**
    * URL: `http://localhost:8080`
    * User/Pass: `airflow` / `airflow`
    * Trigger DAG `main_dag` để bắt đầu quy trình.

---
*Project by Khoa Huynh - UIT Student*
