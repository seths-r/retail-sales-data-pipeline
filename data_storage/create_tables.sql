CREATE TABLE retail_sales (
    order_id INT PRIMARY KEY,
    product_id VARCHAR(50),
    quantity INT,
    price DECIMAL(10, 2),
    order_date DATE
);
