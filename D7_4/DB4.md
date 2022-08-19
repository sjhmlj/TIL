#### CASE

- CASE문은 특정 상황에서 데이터를 변환하여 활용할 수 있음

```sql
SELECT
	CASE
		WHEN 조건식 THEN 식
		WHEN 조건식 THEN 식
		ELSE 식
	END
FROM ~~
;
```

## 서브쿼리

- 서브쿼리는 특정한 값을 메인 쿼리에 반환하여 활용하는 것
- 실제 테이블에 없는 기준을 이용한 검색이 가능함
- 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 칼럼을 모두 사용할 수 있음
- 메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없음

```sql
SELECT *
FROM 테이블
WHERE 컬럼1 = (
	SELECT 컬럼1
  FROM 테이블
)
```

- 단일행 서브쿼리
  - 서브쿼리의 결과가 0 또는 1개인 경우
  - 단일행 비교 연산자와 함께 사용(=, <. <=. >=, >, <>)
```sql
-- users 에서 가장 나이가 작은 사람의 수는?
SELECT COUNT(*)
FROM users
WHERE age = (
	SELECT MIN(age)
  FROM users
);
-- SELECT 에서의 활용. 이렇게 쓸 수도 있음
SELECT 
	(SELECT COUNT(*) FROM users) AS '총인원',
	(SELECT AVG(balance) FROM users) AS '평균연봉',
	(SELECT AVG(age) FROM users) AS '평균나이'
	;
-- UPDATE 에서의 활용
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);
```
- 다중행 서브쿼리
  - 서브쿼리 결과가 2개 이상인 경우
  - 다중행 비교 연산자와 함께 사용(IN, EXISTS 등)

```sql
SELECT COUNT(*) 
FROM users
WHERE country IN (
	SELECT country
 	FROM users
  WHERE first_name = '은정' AND last_name = '이'
);
```

- 다중컬럼 서브쿼리

```SQL
-- 특정 성씨에서 가장 어린 사람들의 이름과 나이
SELECT 
	last_name,
	first_name, 
	age
FROM users
WHERE (last_name, age) IN (
	SELECT last_name, MIN(age)
  FROM users
  GROUP BY last_name
)
ORDER BY last_name
;
```



#### 실습

```sql
-- '' 이랑 "" 이랑 다르다. 
SELECT firstName AS '이름', lastName '성' FROM customers WHERE Country = 'USA' ORDER BY '이름' LIMIT 5;
-- 정렬이 제대로 안되고 (firstName으로 안된다.)
SELECT firstName AS '이름', lastName '성' FROM customers WHERE Country = 'USA' ORDER BY "이름" LIMIT 5;
-- 정렬이 제대로 된다.

-- '' , "" 에 따라 색깔이 달라지는 거 보니까 "" 만이 변수를 나타낼 때 쓰이는 것 같다. 
```

- strftime 사용법

```sql
SELECT start_date, strftime('%Y', start_date) as "Year",
strftime('%m', start_date) as "Month"
strftime('%d', start_date) as "Day"
FROM job_history
WHERE strftime('%m', start_date) 
IN ('01', '02', '03');
-- 실습할 때는 WHERE 절에서 비교할 때 '2013' 이나 2013 은 제대로 작동하지 않은 반면 "2013"은 제대로 작동했다.

-- strftime(format, timestring, modifier, modifier, ...)
```

- 집계함수가 있으면 한 번만 출력되는 것 같다.

```sql
SELECT Country '나라', COUNT(*) '고객 수' FROM customers  ORDER BY "고객 수" DESC LIMIT 5;
-- 1줄만 출력
SELECT Country '나라'FROM customers  ORDER BY "고객 수" DESC LIMIT 5;
-- 5줄 출력
```

- CAST

```sql
-- The CAST() function converts a value (of any type) into a specified datatype.

SELECT CAST(26.65 AS int);
SELECT CAST('2017-08-25' AS datetime);
```

- =, IN  차이

```sql
SELECT Name FROM artists WHERE ArtistId = (
    SELECT ArtistID FROM albums GROUP BY ArtistId ORDER BY COUNT(*) DESC 
);
-- 하나만 출력됨
SELECT Name FROM artists WHERE ArtistId IN (
    SELECT ArtistID FROM albums GROUP BY ArtistId ORDER BY COUNT(*) DESC 
);
-- 다 출력됨. 정렬은 하려면 따로 해줘야 함(메인 쿼리에서)
```

- 이렇게도 된다.

```sql
SELECT Name 
FROM artists 
WHERE ArtistId = (
  SELECT ArtistId FROM (
    SELECT ArtistId, max(a) FROM (           -- 이부분이 이해가 안가네. 이렇게 묶여 있나/??? 그런듯. 
      SELECT ArtistId, count(*) AS a FROM albums GROUP BY ArtistId
    )
  )
);
-- 여기서 max(a) 의 값에 해당하는 레코드 값이 있어서, 같은 레코드의 ArtistId도 나오는 것 같다. 하긴 SELECT 의 본질이네. 
```



---

강의자료

[strftime](https://www.w3resource.com/sqlite/sqlite-strftime.php)
