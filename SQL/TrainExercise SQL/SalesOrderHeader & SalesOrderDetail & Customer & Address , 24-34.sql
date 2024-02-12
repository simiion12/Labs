--Exercitiu 24
SELECT TOP 3
    c.FirstName,
    c.LastName,
    MAX(s.UnitPrice) AS MaxUnitPrice
FROM
    SalesLT.Customer c
JOIN
    SalesLT.SalesOrderHeader so ON c.CustomerID = so.CustomerID
JOIN
    SalesLT.SalesOrderDetail s ON so.SalesOrderID = s.SalesOrderID
JOIN
    SalesLT.Product p ON s.ProductID = p.ProductID
GROUP BY
    c.FirstName, c.LastName
ORDER BY
    MaxUnitPrice DESC;


--Exercitiu 25
SELECT TOP 5
	c.FirstName,
    c.LastName,
	SUM(so.TotalDue) AS TotalAmountSpent
From SalesLT.Customer as c
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
GROUP BY
    c.FirstName, c.LastName
ORDER BY
    TotalAmountSpent DESC;



--Exercitiu 26
SELECT TOP 10
	c.FirstName,
    c.LastName,
	COUNT(DISTINCT sod.ProductID) AS TotalDifferentProducts
From SalesLT.Customer as c
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
JOIN SalesLT.SalesOrderDetail AS sod ON so.SalesOrderID = sod.SalesOrderID
GROUP BY
    c.FirstName, c.LastName
ORDER BY
    TotalDifferentProducts DESC;


--Exercitiu 27
SELECT TOP 2
	c.FirstName,
    c.LastName,
	COUNT(DISTINCT sod.SalesOrderID) AS TotalOrders
From SalesLT.Customer as c
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
JOIN SalesLT.SalesOrderDetail AS sod ON so.SalesOrderID = sod.SalesOrderID
GROUP BY
    c.FirstName, c.LastName
ORDER BY
    TotalOrders DESC;


--Exercitiu 28
SELECT TOP 5
    c.FirstName,
    c.LastName,
    COUNT(sod.ProductID) AS TotalProducts
FROM
    SalesLT.Customer AS c
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
JOIN SalesLT.SalesOrderDetail AS sod ON so.SalesOrderID = sod.SalesOrderID
GROUP BY
    c.FirstName, c.LastName
HAVING
    COUNT(sod.ProductID) > 30



--Exercitiu 29
SELECT TOP 5
    c.FirstName,
    c.LastName,
    COUNT(sod.ProductID) AS TotalProducts
FROM
    SalesLT.Customer AS c
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
JOIN SalesLT.SalesOrderDetail AS sod ON so.SalesOrderID = sod.SalesOrderID
GROUP BY
    c.FirstName, c.LastName
HAVING
    COUNT(sod.ProductID) < 5



--Exercitiu 30
SELECT TOP 10
    c.FirstName,
    c.LastName,
    sod.ProductID,
    COUNT(*) AS OrderCount
FROM
    SalesLT.Customer AS c
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
JOIN SalesLT.SalesOrderDetail AS sod ON so.SalesOrderID = sod.SalesOrderID
GROUP BY
    c.CustomerID, c.FirstName, c.LastName, sod.ProductID
HAVING
    COUNT(*) > 1
ORDER BY
    OrderCount DESC;



--Exercitiu 31
SELECT 
    a.CountryRegion,
    SUM(so.TotalDue) AS TotalSalesAmount
FROM
    SalesLT.Customer AS c
JOIN SalesLT.CustomerAddress AS ca ON c.CustomerID = ca.CustomerID
JOIN SalesLT.Address AS a ON ca.AddressID = a.AddressID
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
GROUP BY
    a.CountryRegion



--Exercitiu 32
SELECT
    a.CountryRegion,
    a.City,
    SUM(so.TotalDue) AS TotalSalesAmount
FROM
    SalesLT.Customer AS c
JOIN SalesLT.CustomerAddress AS ca ON c.CustomerID = ca.CustomerID
JOIN SalesLT.Address AS a ON ca.AddressID = a.AddressID
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
GROUP BY
    a.CountryRegion, a.City
ORDER BY
    TotalSalesAmount DESC;


--Exercitiu 33
SELECT TOP 3
    a.City,
    COUNT(DISTINCT so.SalesOrderID) AS OrderCount
FROM
    SalesLT.Customer AS c
JOIN SalesLT.CustomerAddress AS ca ON c.CustomerID = ca.CustomerID
JOIN SalesLT.Address AS a ON ca.AddressID = a.AddressID
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
GROUP BY
    a.City
ORDER BY
    OrderCount DESC;



--Exercitiu 34
SELECT TOP 5
    a.City,
    SUM(so.TotalDue) AS TotalSalesAmount
FROM
    SalesLT.Customer AS c
JOIN SalesLT.CustomerAddress AS ca ON c.CustomerID = ca.CustomerID
JOIN SalesLT.Address AS a ON ca.AddressID = a.AddressID
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
GROUP BY
    a.City
ORDER BY
    TotalSalesAmount DESC;

