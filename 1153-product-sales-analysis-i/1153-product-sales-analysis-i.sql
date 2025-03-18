# Write your MySQL query statement below
SELECT 
    product_name, year, price
FROM 
    SALES
LEFT JOIN Product

ON SALES.product_id = Product.product_id