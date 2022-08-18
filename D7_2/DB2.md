#### 조건식에 사용되는 연산자 종류

| 구분             | 연산자              | 연산자의 의미                                        |
| ---------------- | ------------------- | ---------------------------------------------------- |
| 비교 연산자      | =                   |                                                      |
|                  | >                   |                                                      |
|                  | >=                  |                                                      |
|                  | <                   |                                                      |
|                  | <=                  |                                                      |
| SQL 연산자       | BETWEEN a AND b     | a와 b의 값 사이에 있으면 된다.(a, b 포함)            |
|                  | IN (list)           | 리스트에 있는 값 중에서 어느 하나라도 일치하면 된다. |
|                  | LIKE '비교문자열'   | 비교문자열과 형태가 일치하면 된다. (%, _ 사용)       |
|                  | IS NULL             | NULL 값인 경우                                       |
| 논리 연산자      | AND                 |                                                      |
|                  | OR                  |                                                      |
|                  | NOT                 | 뒤에 오는 조건에 반대되는 결과를 되돌려 준다.        |
| 부정 비교 연산자 | !=                  | 같지 않다                                            |
|                  | ^=                  | 같지 않다                                            |
|                  | <>                  | 같지 않다(ISO 표준, 모든 운영체제에서 사용 가능)     |
|                  | NOT 칼럼명 =        | ~ 와 같지 않다.                                      |
|                  | NOT 칼럼명 >        | ~ 보다 크지 않다.                                    |
| 부정 SQL 연산자  | NOT BETWEEN a AND b | a와 b 값 사이에 있지 않다.(a, b 포함 하지 않는다)    |
|                  | NOT IN (list)       | list 값과 일치하지 않는다.                           |
|                  | IS NOT NULL         | NULL 값을 갖지 않는다.                               |

- 연산자 우선순위
  1. 괄호 ()
    2. NOT
    3. 비교 연산자, SQL
    4. AND 
    5. OR

#### SQLite Aggregate Functions

- Agrregate Function

  - 각 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결괏값을 반환하는 함수
  - SELECT 구문에서만 사용됨

- 종류

  - COUNT
  - AVG
  - MAX
  - MIN
  - SUM

- LIKE

  - 'query data based on pattern matching'
  - 패턴 일치를 기반으로 데이터를 조회하는 방법
  - SQLite는 패턴 구성을 위한 2개의 wildcards를 제공
    - % : 0개 이상의 문자
    - _ : 임의의 단일 문자

  ```sql
  -- users 테이블에서 나이가 20대인 사람만 조회
  SELECT * FROM users WHERE age LIKE '2_'
  ```

- ORDER BY

  - 'sort a result set of a query'
  - 조회 결과 집합을 정렬
  - SELECT 문에 추가하여 사용
  - 정렬 순서를 위한 2개의 keyword 제공
    - ASC - 오름차순(default)
    - DESC - 내림차순

#### 실습하면서 알게 된 점

- unique constraint 가 real 이면 '' 공백을 입력할 수 있다. typeof를 찍으면 text로 나온다. int의 경우 공백 입력이 안된다. 공백과 NULL은 다르다. 

  - SQLite3에서는 정수끼리 나눗셈을 하면 정수가 나온다. 

  ```sql
  SELECT COUNT(*) FROM healthcare WHERE weight/((height*0.01)*(height*0.01)) >= 30;
  -- 정상 작동
  SELECT COUNT(*) FROM healthcare WHERE weight/((height/100)*(height/100)) >= 30;
  -- 정상 작동 안함. 
  -- 뭐냐 이건
  
  SELECT weight/((height*0.01)*(height*0.01)) FROM healthcare LIMIT 1;
  -- 22.0385674931129   
  
  SELECT weight/((height/100)*(height/100)) FROM healthcare LIMIT 1;
  -- 60  
  
  SELECT weight, (height * height) * 0.0001 , (height/100), (height/100)*(height/100), weight / ((height * height) * 0.0001)FROM healthcare LIMIT 1;
  -- 60      2.7225                      1             1                          22.0385674931129  
  ```

  정확한 계산을 위해서는 숫자를 실수형으로 형변환해야 한다. 

  ```sql
  -- 1. CAST 함수 이용하기.
  CAST( ~ AS REAL)
  
  -- 2. 0.0을 더하던지 100.0으로 나누던지 등등
  SELECT weight/((height/100.0)*(height/100.0)) FROM healthcare LIMIT 1;
  -- 22.0385674931129  
  ```

  

#### SELECT 쿼리 진행 순서

1. FROM - 전체 데이블의 결과를 가져옴
2. WHERE - 조건에 맞는 결과만 갖도록 데이터를 간추림. 집계함수를 사용할 ㅜㅅ 없다.
3. GROUP BY
4. HAVING - 집계함수를 가지고 조건비교를 할 때 사용한다. (GROUP BY 와 함께 사용된다.)
5. SELECT
6. ORDER BY



#### 실습

- 스키마에 int를 설정해도 텍스트가 들어갈 수 있었다. 밑에 보면 좋다 . SQLite 공식 사이트에서 가져왔다. 

  ```text
  Most SQL database engines (every SQL database engine other than SQLite, as far as we know) uses static, rigid typing. With static typing, the datatype of a value is determined by its container - the particular column in which the value is stored.
  
  SQLite uses a more general dynamic type system. In SQLite, the datatype of a value is associated with the value itself, not with its container. The dynamic type system of SQLite is backwards compatible with the more common static type systems of other database engines in the sense that SQL statements that work on statically typed databases work the same way in SQLite. However, the dynamic typing in SQLite allows it to do things which are not possible in traditional rigidly typed databases. Flexible typing is a feature of SQLite, not a bug.
  ```

- ```sql
  DELETE FROM 테이블이름 WHERE 조건;
  ```

- 