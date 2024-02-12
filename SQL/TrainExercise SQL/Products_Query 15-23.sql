-- Exercitiu 1
Select DISTINCT Color
From SalesLT.Product;

Select Color
From SalesLT.Product
GROUP BY Color;


--Exercitiu 2
Select Name, Color 
From SalesLT.Product
Where Color is NULL

 --Exercitiu 3
Select 
    ISNULL(Size, 'No size') AS ProductSize,
    COUNT(*) AS NumberOfProducts
From SalesLT.Product
GROUP BY Size WITH ROLLUP;

 --Exercitiu 4
 Select 
	ISNULL(Color, 'No size') AS ProductColor,
    COUNT(*) AS NumberOfProducts
From SalesLT.Product
GROUP BY Color WITH ROLLUP

--Exercitiu 5
Select 
	COUNT(*) as TotalNoSize
From SalesLT.Product
Where Size is Null

--Exercitiu 6
Select 
	ProductCategoryID,
	COUNT(*) AS NumberOfProducts
From SalesLT.Product
GROUP BY ProductCategoryID

--Exercitiu 7
Select
	pc.Name AS ProductCategoryName,
	COUNT(p.ProductID) AS NumberOfProducts
From SalesLT.Product AS p
Inner Join SalesLT.ProductCategory AS pc ON p.ProductCategoryID = pc.ProductCategoryID
GROUP BY pc.Name

--Exercitiu 8
Select * From SalesLT.Product
Select 
    COUNT(*) AS TotalProductsNoPhoto
From SalesLT.Product
Where ThumbnailPhotoFileName LIKE '%no_image_available%';

--Exercitiu 9
Select 
    IIF(ListPrice < 40, 'Cheap', 'Expensive') AS PriceCategory,
    SUM(1) AS ProductCount
From SalesLT.Product
GROUP BY IIF(ListPrice < 40, 'Cheap', 'Expensive');

Select
    CASE WHEN ListPrice < 40 THEN 'Cheap' ELSE 'Expensive' END AS PriceCategory,
    COUNT(*) AS ProductCount
From SalesLT.Product
GROUP BY CASE WHEN ListPrice < 40 THEN 'Cheap' ELSE 'Expensive' END;

--Exercitiu 10
Select
	IIF(ListPrice < 30, 'Cheap', 
		IIF(ListPrice < 80, 'Normal', 'Expensive')) AS PriceCategory,
	SUM(1) AS ProductCount
From SalesLT.Product
GROUP BY IIF(ListPrice < 30, 'Cheap', 
		IIF(ListPrice < 80, 'Normal', 'Expensive'))


Select 
    CASE
        WHEN ListPrice < 30 THEN 'Cheap'
        WHEN ListPrice < 80 THEN 'Normal'
        ELSE 'Expensive'
    END AS PriceCategory,
    SUM(1) AS ProductCount
From SalesLT.Product
GROUP BY 
    CASE
        WHEN ListPrice < 30 THEN 'Cheap'
        WHEN ListPrice < 80 THEN 'Normal'
        ELSE 'Expensive'
    END;


--Exercitiu 11
Select 
    ProductID,
    Name,
    Color,
    Size,
    ListPrice
From SalesLT.Product
Where 
    CHARINDEX('Men''s', Name) > 0
    AND CHARINDEX('Women''s', Name) = 0;


--Exercitiu 12
Select 
	ProductID,
	Name,
	Size,
	Color,
	ListPrice
From SalesLT.Product
Where
	CHARINDEX('Women''s', Name) > 0


--Exercitiu 13
Select  
    ProductID,
    Name,
    Color,
    Size,
    ListPrice
From SalesLT.Product
Where 
    CHARINDEX('Men''s', Name) = 0
    AND CHARINDEX('Women''s', Name) = 0;

--Exercitiu 14
Select 
    ProductID,
    Name,
    StandardCost,
    ListPrice,
    CONVERT(VARCHAR(10), CAST(((ListPrice - StandardCost) / StandardCost) * 100 AS DECIMAL(10,2))) + '%' AS PercentageDifference
From SalesLT.Product;