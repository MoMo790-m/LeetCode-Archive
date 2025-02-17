SELECT products.product_name , SUM(orders.unit) AS unit
FROM products 
JOIN orders
ON products.product_id = orders.product_id
WHERE MONTH(orders.order_date) = 2 
AND YEAR(orders.order_date) = 2020
GROUP BY products.product_name
HAVING SUM(orders.unit) >= 100