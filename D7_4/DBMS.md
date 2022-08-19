- sqlite3에서

```sql
SELECT weight / (height*height*0.0001) AS BMI FROM healthcare WHERE BMI >= 15 LIMIT 3;
```

이 구문이 실행된다. WHERE 이 SELECT 보다 실행 우선순위가 높아서 에러가 날 것 같았는데 예상과 달랐다. 



질문 드렸고, 이에 대한 답변으로  DBMS 내의 어떤 작업이 더해져서 실행이 되지 않았을까 라고 하셨다. 

실제로 이 쿼리는 답변자 분이 쓰시는 maridDB에서는 돌아가지 않는다고 한다. SQLite3 의 한 기능인 것 같다. 

강의에서 배운 SQL 실행 순서는 정석으로 알고 넘어가면 될 것 같다. 예외는 어디에나 있을 수 있다.

#### DBMS 작동 방식

- RDB에서 데이터 접근 절차를 결정하는 모듈을 쿼리 평가 엔진이라고 부른다. 

- Parser - Optimizer - Catalog manager - Plan evaluation
- parser
  - 구문분석을 한다. 사용자로부터 입력받은 SQL 구문이 문법적으로 오류가 있는지 검사해준다.
- optimizer
  - 최적화(데이터 접근법, 실행계획)을 세우고, 비용을 계산해서, 가장 낮은 비용을 가진 실행계획 계산한다.
  - 이때 고려하는 조건으로는 인덱스 유무, 데이터 분산 또는 편향 정도, 내부 매개변수 등을 고려한다.
- catalog manager
  - 옵티마이저가 실행계획을 세울 때 옵티마이저에게 중요한 정보를 제공한다.
  - 카탈로그란 DBMS의 내부 정보를 모아놓은 테이블로, 테이블 또는 인덱스 통계 정보가 저장되어 있다.
- plan evaluation
  - 최적의 실행 결과를 선택한다. 







---

[DBMS 작동방식](https://cornswrold.tistory.com/131?category=777471)