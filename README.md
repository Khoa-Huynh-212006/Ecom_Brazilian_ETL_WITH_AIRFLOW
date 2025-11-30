# Brazilian E-commerce ETL Pipeline with Airflow

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

<img width="1917" height="1019" alt="image" src="https://github.com/user-attachments/assets/ec1e70a4-d462-4bfd-be64-5a6735418f2f" />
---

## 🔄 3. Quy trình ETL (The Pipeline Workflow)

Toàn bộ quy trình được quản lý bởi **Airflow DAG** tên là `main_dag`.

### 📊 Luồng xử lý (DAG Graph)
Dưới đây là sơ đồ thực tế của Pipeline trên giao diện Airflow. Các tác vụ chuyển đổi (Transformation) được xử lý song song để tối ưu hóa hiệu suất:

<img width="1914" height="985" alt="image" src="https://github.com/user-attachments/assets/2ae92ae0-5d22-4e60-b6d3-5d9ba6d4c59c" />

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

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/d7f69562-40e7-415d-9ee8-681d7ba81e49" />



### 🔵 Giai đoạn 2: Data Warehouse (PostgreSQL)
Dữ liệu sau khi được làm sạch bằng Python (Pandas) sẽ được mô hình hóa theo dạng **Star Schema** để phục vụ phân tích (Analytics Ready).
* **Schema:** `public`
* **Fact Table:** `fct_orders` (Chứa dữ liệu giao dịch).
* **Dimension Tables:** `dim_customers`, `dim_products`, `dim_sellers` (Chứa dữ liệu danh mục).

<img width="1912" height="1077" alt="image" src="https://github.com/user-attachments/assets/2ceddc57-b39a-460d-b41e-f885bb115051" />


---
*Project by Khoa Huynh - UIT Student*
