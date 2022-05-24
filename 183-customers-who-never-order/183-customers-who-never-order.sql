# USING NOT EXISTS
# SELECT name as Customers
# FROM Customers
# WHERE
#   NOT EXISTS (SELECT customerId FROM Orders WHERE Orders.customerId = Customers.id);

SELECT 
    c.name as Customers
FROM 
    Customers as c
LEFT JOIN Orders as o
    ON c.id = o.customerId
WHERE 
    o.customerId IS NULL;