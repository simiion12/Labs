--Exercitiu 15
SELECT
    LastName,
    COUNT(*) AS CustomerLNameCount
FROM
    SalesLT.Customer
GROUP BY
    LastName
HAVING
    COUNT(*) > 1


--Exercitiu 16
SELECT 
	FirstName,
	COUNT(*) as CustomerFNameCount
FROM SalesLT.Customer
GROUP BY 
	FirstName
HAVING
	COUNT(*) > 1


--Exercitiu 17

SELECT
	IIF( Title = 'Mr.', 'Men', 
		IIF(Title in ('Mrs.', 'Ms.'), 'Women', 'Kids')) as CostumerGender,
	SUM(1) as Total
FROM SalesLT.Customer 
GROUP BY 
	IIF( Title = 'Mr.', 'Men', 
		IIF(Title in ('Mrs.', 'Ms.'), 'Women', 'Kids'))

SELECT
	CASE
		WHEN Title = 'Mr.' THEN 'Men'
		WHEN Title in ('Mrs.', 'Ms.') THEN 'Women'
		ELSE 'Kids'
	END AS CostumerGender,
	SUM(1) as Total
FROM SalesLT.Customer
GROUP BY
	CASE
		WHEN Title = 'Mr.' THEN 'Men'
		WHEN Title in ('Mrs.', 'Ms.') THEN 'Women'
		ELSE 'Kids'
	END


--Exercitiu 18
SELECT
    *
FROM
    SalesLT.Customer 
WHERE
    CompanyName IN (
        SELECT
            CompanyName
        FROM
            SalesLT.Customer
        GROUP BY
            CompanyName
        HAVING
            COUNT(DISTINCT LastName) > 1
    );



--Exercitiu 19
SELECT
	LEN(FirstName) AS LengthFName,
	COUNT(*) AS Frequency
FROM SalesLT.Customer
GROUP BY
	LEN(FirstName)
ORDER BY
	Frequency DESC


--Exercitiu 20
SELECT
	LEN(LastName) AS LengthLName,
	COUNT(*) AS Frequency
FROM SalesLT.Customer
GROUP BY
	LEN(LastName)
ORDER BY
	Frequency DESC



--Exercitiu 21
SELECT
	COUNT(*) AS TotalCount
FROM SalesLT.Customer
WHERE LEFT(FirstName , 1) IN ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

SELECT
	COUNT(*) AS TotalCount
FROM SalesLT.Customer
WHERE FirstName LIKE '[aeiouAEIOU]%';

--Exercitiu 22
SELECT
	COUNT(*) AS TotalCount
FROM SalesLT.Customer
WHERE RIGHT(LastName , 1) IN ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

SELECT
	COUNT(*) AS TotalCount
FROM SalesLT.Customer
WHERE LastName LIKE '%[aeiouAEIOU]';


--Exercitiu 23
SELECT
	COUNT(*) AS TotalCount
FROM SalesLT.Customer
WHERE LEFT(LastName , 1)  NOT IN ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

SELECT
	COUNT(*) AS TotalCount
FROM SalesLT.Customer
WHERE LastName LIKE '[^aeiouAEIOU]%';