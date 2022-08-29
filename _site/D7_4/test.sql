SELECT * FROM albums ORDER BY Title DESC LIMIT 5;
SELECT COUNT(*) AS '고객 수' FROM customers ;
SELECT firstName '이름', lastName '성' FROM customers WHERE Country = 'USA' ORDER BY firstName LIMIT 5;
SELECT firstName AS '이름', lastName '성' FROM customers WHERE Country = 'USA' ORDER BY "이름" LIMIT 5;

SELECT COUNT(*) '송장수' FROM invoices WHERE BillingPostalCode IS NOT NULL;
SELECT * FROM invoices WHERE BillingState IS NULL ORDER BY InvoiceDate LIMIT 5;
SELECT COUNT(*) FROM invoices WHERE strftime('%Y', InvoiceDate) = "2013";

SELECT CustomerId '고객ID', FirstName '이름', LastName '성' FROM customers 
WHERE FirstName LIKE "L%"
ORDER BY CustomerId;

SELECT COUNT(*) '고객 수', Country '나라' FROM customers GROUP BY Country ORDER BY "고객 수" DESC LIMIT 5;
SELECT Country '나라', COUNT(*) '고객 수' FROM customers  ORDER BY "고객 수" DESC LIMIT 5;

SELECT ArtistId, COUNT(*) FROM albums
GROUP BY ArtistId
ORDER BY COUNT(*) DESC LIMIT 1
;

SELECT ArtistId, COUNT(*) '앨범 수' FROM albums GROUP BY ArtistId HAVING COUNT(*) >10 ORDER BY COUNT(*) DESC;

SELECT COUNT(*) '고객 수', Country, State FROM customers WHERE State IS NOT NULL 
GROUP BY Country , State ORDER BY COUNT(*)DESC, Country LIMIT 5;

SELECT CustomerId, (CASE WHEN Fax IS NULL THEN 'O' ELSE 'X' END) AS 'Fax 유/무' FROM customers ORDER BY CustomerId LIMIT 5; 

SELECT LastName, FirstName, (strftime('%Y', 'now')-strftime('%Y', BirthDate)+1) as '나이' FROM employees ORDER BY EmployeeId;

SELECT Name FROM artists WHERE ArtistId = (
    SELECT ArtistID FROM albums GROUP BY ArtistId ORDER BY COUNT(*) DESC 
);

SELECT ArtistID , COUNT(*) FROM albums GROUP BY ArtistId ORDER BY COUNT(*) DESC LIMIT 5;

SELECT Name FROM genres WHERE GenreId = (SELECT GenreId FROM tracks GROUP BY GenreId ORDER BY COUNT(*));

SELECT GenreId, COUNT(*) FROM tracks GROUP BY GenreId ORDER BY COUNT(*);

-- 윤식님 풀이 16번
SELECT Name 
FROM artists 
WHERE ArtistId = (
  SELECT ArtistId FROM (
    SELECT ArtistId, max(a) FROM (                 -- 이부분이 이해가 안가네. 이렇게 묶여 있나/??? 그런듯. 
      SELECT ArtistId, count(*) AS a FROM albums GROUP BY ArtistId
    )
  )
);