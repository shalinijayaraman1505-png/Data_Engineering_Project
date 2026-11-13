CREATE TABLE cleaned_orders (
    orderid INT,
    customername VARCHAR(100),
    product VARCHAR(100),
    category VARCHAR(50),
    quantity NUMERIC(10,2),
    price NUMERIC(10,2),
    orderdate DATE,
    shipped VARCHAR(20),
    country VARCHAR(50),
    totalamount NUMERIC(12,2)
);

SELECT * FROM cleaned_orders;

UPDATE cleaned_orders
SET totalamount = quantity * price;

SELECT orderid, quantity, price, totalamount
FROM cleaned_orders
LIMIT 10;

SELECT COUNT(*)
FROM cleaned_orders;

SELECT *
FROM cleaned_orders
WHERE totalamount is NULL;

SELECT
    country,
	SUM(totalamount) AS total_sales
FROM cleaned_orders
GROUP BY country;

SELECT SUM(totalamount)
FROM cleaned_orders;

SELECT
    category,
	SUM(quantity) AS quanityby_category
FROM cleaned_orders
GROUP BY category;

 
SELECT country, SUM(totalamount) AS total_sales
FROM cleaned_orders
GROUP BY country;

SELECT *
FROM cleaned_orders
WHERE totalamount>1000;

SELECT
    country,
	SUM(totalamount) AS total_sales
FROM cleaned_orders
GROUP BY country
HAVING SUM(totalamount) > 5000;


SELECT *
FROM cleaned_orders
ORDER BY totalamount ASC;

SELECT *
FROM cleaned_orders
ORDER BY totalamount DESC;

SELECT
    country,
	SUM(totalamount) AS total_sales
FROM cleaned_orders
GROUP BY country
ORDER BY total_sales DESC;


SELECT
    country,
    SUM(totalamount) AS total_sales
FROM cleaned_orders
GROUP BY country
ORDER BY total_sales DESC;

SELECT DISTINCT country
FROM cleaned_orders;

SELECT country, COUNT(*)
FROM cleaned_orders
GROUP BY country;

SELECT *
FROM cleaned_orders
LIMIT 5;