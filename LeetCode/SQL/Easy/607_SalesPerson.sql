-- SalesPerson
SELECT s.name
FROM SalesPerson s LEFT JOIN (SELECT sales_id 
                              FROM Orders o RIGHT JOIN Company c2 
                                ON o.com_id = c2.com_id
                              WHERE name = "RED") j
    ON s.sales_id = j.sales_id
WHERE j.sales_id IS NULL