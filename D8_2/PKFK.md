## PK

본 키(Primary Key)의 각 데이터는 테이블에서 유일한 값이다. 

**즉, 기본키는 하나의 테이블에서 각 행의 데이터를 유일하게 확인하는데 사용되는 것이다.**

기본 키는 원래의 데이터 내의 하나의 필드 또는 하나로 만들어진 필드(원래 데이터와 관계없는 필드)가 가능하다. 

기본 키는 하나 이상의 필드를 포함할 수 있다. 기본 키가 여러 필드를 포함하는 경우, 복합키(Composite Key)라고 부른다.



```mysql
# MySQL
CREATE TABLE customer (
	sid INTEGER,
  last_name VARCHAR(30),
  first_name VARCHAR(30),
  PRIMARY KEY(sid)
);
```



## FK

왜래 키(Foreign Key)는 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키를 말한다. 

다른 테이블에서 '기본 키'로 사용되는 칼럼이 현재 테이블에서도 칼럼으로 사용되는 것을 의미한다. 단순 중복 칼럼이 아니라, 의도적으로 테이블 조인과 같은 목적을 수행하기 위해 넣은 키이다. 

- 테이블에서 FK가 PK 역할을 하는 경우 - 식별 관계
- 테이블에서 FK가 일반 칼럼이고, 따로 PK가 존재하는 경우 - 비식별 관계

FK의 참조 무결성 제약 조건 : 참조 무결성이 강제 적용되면 왜래 키가 선언된 테이블의 왜래 키를 구성하는 칼럼의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값 또는 기본 키가 아닌 후보 키 값으로 존재해야 한다. 예를 들어, 다른 테입르의 왜래 키에 의해 참조되는 쌍을 제거하는 것은 참조 무결성을 파괴해 버리게 되기 때문에 RDBMS에서는 참조 무결성을 유지하도록 일반적으로 삭제를 방지한다. 예외적으로 참조하는 왜래 키를 포함하는 쌍을 연결하고 제거하는 것이 수반되어 삭제를 수행할 수 있으며, 이 경우 참조 무결성이 유지된다.

데이터 무결성(data integrity)은 컴퓨팅 분야에서 완전한 수명 주기를 거치며 데이터의 정확성과 일관성을 유지하고 보증한느 것을 가리킴. 데이터베이스나 RDBMS의 중요한 기능. 



```mysql
CREATE TABLE orders (
	order_id INTEGER ,
  order_date DATE, 
  customer_sid INTEGER,
  amount DOUBLE,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_sid) REFERENCES customer (sid)
);
```











\## 관계 변수 = 테이블 이라고 생각해라. 









---

[프로그램 개발 지식 공유](https://araikuma.tistory.com/494?category=785111)

[위키백과](https://ko.wikipedia.org/wiki/%EC%99%B8%EB%9E%98_%ED%82%A4)

[정명훈의 블로그](https://audgnssweet.tistory.com/21)