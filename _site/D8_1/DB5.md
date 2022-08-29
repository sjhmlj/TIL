#### Join

- 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능
- 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를  저장한느 것이 아니라 여러 테이블로 나눠 저장하게 되며, 여러 테이블을 결합하여 출력하여 활용
- 일반적으로 레코드는 기본키(PK)나 외래키(FK) 값의 관계에 의해 결합됨



---

- INNER JOIN : 두 테이브렝 모두 일치하는 행만 반환

  ```sql
  SELECT *
  FROM 테이블2	[INNER] JOIN 테이블2
  	ON 테이블1.칼럼 = 테이블2.칼럼;
  ```

  

- OUTER JOIN : 동일한 값이 없는 행도 반환

  - 기준이 되는 테이블에 따라 LEFT/RIGHT/FULL을 지정

  ```sql
  SELECT *
  FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
  	ON 테이블1.칼럼 = 테이블2.칼럼
  ```

  

- CROSS JOIN : 모든 데이터의 조합

```sql
SELECT *
FROM users CROSS JOIN role;
```

![스크린샷 2022-08-22 오후 4.12.57](DB5.assets/스크린샷 2022-08-22 오후 4.12.57.png)

#### 실습

```sql
SELECT *  FROM users JOIN role ON users.role_id = role.id;

SELECT *  FROM users JOIN articles ON users.role_id = articles.user_id;

SELECT * FROM articles LEFT OUTER JOIN users ON users.id = articles.user_id;

SELECT * FROM articles FULL OUTER JOIN users ON users.id = articles.user_id;

SELECT * FROM users JOIN role ON users.role_id  = role.id JOIN articles ON users.id = articles.user_id;

SELECT * FROM articles FULL OUTER JOIN users ON users.id = articles.user_id;

SELECT * FROM users CROSS JOIN role;
```

---

강의자료

구글 이미지