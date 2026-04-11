
select A.name from customers A LEFT JOIN orders B ON A.id=B.customer_id where B.customer_id is NULL;