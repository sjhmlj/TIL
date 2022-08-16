#### DB는 어디에 쓰일까
- 쿠팡 상품 정보 등

- DB에서 조작하는 언어가 SQL(quere: 질의)

- DB 관리하는 다양한 sw가 있는데, 조금씩 다른 부분이 있지만 공통적이고 유사한 부분도 있음.

# 데이터베이스
- 체계화된 데이터의 모임
- 여러 사랑미 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 자료의 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
  - 즉, 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체 

- 장점
  - 데이터 중복 최소화
  - 데이터 무결성(정확한 정보를 보장)
  - 데이터 일관성
  - 데이터 독립성(물리적 / 논리적)
  - 데이터 표준화
  - 데이터 보안 유지

## 관계형 데이터베이스(RDB)
- 서로 관련된 데이터지점에 대한 접근을 저장 및 제공하는 데이터베이스 유형
- 키와 값들의 간단한 관계를 표 형태로 정리한 데이터 베이스
- 용어
  - 스키마 (schema) : 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것
    - ex) id - INT, name - TEXT, address - TEXT, age - INT
  - 테이블 : 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합![스크린샷 2022-08-16 오후 1.39.16](DB1.assets/스크린샷 2022-08-16 오후 1.39.16.png)
  - 열(column) : 각 열에 고유한 데이터 형식 지정 (name 이란 필드에 고객의 이름(text) 정보가 저장됨)
  - 행(row) : 실제 데이터가 저장되는 형태
  - 기본키(primary key) : 각 행(레코드)의 고유 값 
    - 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨. Ex) 학번, 주민등록번호
    - sqlite에서 기본적으로 제공하는 rowid가 있음.

#### RDBMS(RDB Management System)

- 관계형 데이터베이스 관리 시스템
- 생성, 수정 등 관계형 데이터베이스를 관리할 수 있는 소프트웨어
- MySQL, SQLite, ORACLE, SQL Server, PostgreSQL

#### SQLite

- 서버가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용 가능
- SQLite Date Type
  - NULL
  - INTEGER
    - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정ㅇ수
  - REAL
    - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
  - TEXT
  - BLOB
    - 입력된 그대로 저장된 데이터(별다른 타입 없이 그대로 저장)
- SQL Type Affinity(특정 컬럼에 저장하도록 권장하는 데이터 타입) ![스크린샷 2022-08-16 오후 1.56.45](1.assets/스크린샷 2022-08-16 오후 1.56.45.png)

## SQL(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 프로그래밍 언어

- 데이터베이스 스키마 생성 및 수정

- 자료의 검색 및 관리

- 데이터베이스 객체 접근 조정 관리

- | 분류                                 | 개념                                                         | 예시                                      |
  | ------------------------------------ | ------------------------------------------------------------ | ----------------------------------------- |
  | DDL<br/>(Date Definition Language)   | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE <br/>DROP <br/>ALTER               |
  | DML<br/>(Date Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT <br/>SELECT <br/>UPDATE<br/>DELETE |
  | DCL<br>(Date Control Languate)       | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT<br>REVOKE<br/>COMMIT<br/>ROLLBACK   |

  csv : comma-separate variables


#### 실습
```sql 
-- 데이터베이스 생성
sqlite3 tutorial.sqlite3
> .database
-- main : ~~~/tutorial.sqlite3 r/w

-- csv 파일을 table로 만들기
> .mode csv
> .import hellodb.csv examples
> .tables
-- examples

-- 읽기
> SELECT * FROM examples;
-- 1," 주현"," 서"," 26"," 010-1121-3323"

-- 터미널 view 변경하기
> .headers on
> .mode column

-- 테이블 생성하기
CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,
  name TEXT
);
INSERT INTO classmates (id, name) VALUES (1, '주현');

-- 테이블 삭제하기
DROP TABLE examples;

-- 특정 테이블의 schema 조회
> .schema classmates

```

- 필드 제약 조건

  - NOT NULL : NULL 값 입력 금지
  - UNIQUE : 중복 값 입력 금지(NULL 값은 중복 입력 가능)
  - PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
  - FOREIGN KEY : 외래키. 다른 테이블의 키
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본 설정 값

```sql
CREATE TABLE students(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER DEFAULT 1 CHECK (0 < age)
);
```
#### CRUD

#### create

- INSERT
  - 'insert a single row into a table'
  ```sql
  INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
  ```
  - 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력
    ```sql
    INSERT INTO 테이블_이름 VALUES (값1, 값2, ...);
    ```

#### read

- SELECT
  - 'query data from a table'
  
  - 테이블에서 데이터를 조회
  
  - SELECT 문은 SQLite에서 가장 기본이 되는 문이며 다양한 절(clause)와 함께 사용
    - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY , ...
    
  - LIMIT
    - 'constrain the number of rows returned by a query'
    - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
    
  - WHERE
    - 'specify the search condition for rows returned by the query'
    
    ```sql
    SELECT COUNT(*) FROM healthcare WHERE smoking = 3 and is_drinking = 1;
    ```
    
  - SELECT DISTINCT
    - 'remove cuplicate rows in the result set'
    - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함
    
    ```sql
    SELECT DISTINCT sido FROM healthcare ;
    ```
    
    