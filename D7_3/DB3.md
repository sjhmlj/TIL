

## 함수

#### 문자열 함수

- SUBSTR(문자열, start, length) : 문자열 자르기
  - 시작 인덱스는 1, 마지막 인덱스는 -1
- TRIM(문자열), LTRIM(문자열), RTRIM(문자열) : 문자열 공백 제거
- LENGTH(문자열) : 문자열 길이
- REPLACE(문자열, 패턴, 변경값) : 패턴에 일치하는 부분을 변경
- UPPER(문자열), LOWER(문자열) : 대소문자 변경
- || : 문자열 합치기

#### 숫자 함수

- ABS(숫자) : 절댓값
- SIGN(숫자) : 부호(양수 1, 0, 음수 -1)
- MOD(숫자1, 숫자2) : 숫자 1을 숫자 2로 나눈 나머지
- CEIL(숫자), FLOOR(숫자), ROUND(숫자, 자리) : 올림, 내림, 반올림
- POWER(숫자1, 숫자2) : 숫자1의 숫자2 제곱
- SQRT(숫자) : 제곱근

---

## SELECT

- ALIS

  - 칼럼 명이나 테이블명이 너무 길거나 다른 명칭으로 확인하고 싶을 때는 ALIAS를 활용
  - AS를 생략하여 공백으로 표현할 수 있음
  - 별칭에 공백, 특수문자 등이 있는 경우 따옴표로 묶어서 표기

- GROUP BY

  - 'make a set of sumary rows from a set of rows'
  - SELECT 문의 optional 절 
  - 행 집합에서 요약 행 집합을 만듦
  - 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듬
  - 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함. 
  - 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐. 
  - GROUP BY 의 결과는 기존의 순서와 바뀔 수도 있음. 

  ```sql
  ```

  

- HAVING

  - 집계합수는 WHERE 절의 조건식에서는 사용할 수 없음(실행 순서에 의해)
    - WHERE 로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서 있기 때문
  - 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING 을 사용

- 

## ALTER TABLE

- 테이블 이름 변경
- 새로운 column 추가
- column 이름 수정
- column 삭제

```sql
ALTER TABLE table_name
RENAME TO new_name;

ALTER TABLE table_name
ADD COLUMN column_definition;

ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;

ALTER TABLE table_name
DROP COLUMN column_name;

-- 
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
-- NOT NULL 로 설정하려는데, 기존의 레코드에 null 값이 있다면 에러가 뜨기 때문에 default를 정해준다. 
```

