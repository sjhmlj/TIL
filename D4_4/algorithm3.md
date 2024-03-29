## 딕셔너리

1. 해시테이블
2. 딕셔너리 기본 문법
3. 딕셔너리 메서드

#### 1. 해시 테이블

- 해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수

- 해시 : 해시 함수를 통해 얻어진 값 

- 파이썬의 딕셔너리 특징

  - 해시 함수와 해시 테이블을 이용하기 때문에 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다.

  - ![스크린샷 2022-07-29 오전 9.05.53](algorithm3.assets/스크린샷 2022-07-29 오전 9.05.53.png)

  - |             |      |
    | ----------- | ---- |
    | Get item    | O(1) |
    | Delete item | O(1) |
    | update item | O(1) |
    | insert item | O(1) |
    | search item | O(1) |

- 딕셔너리는 언제 사용해야할까?
  - 리스트를 사용하기 힘든 경우
  - 데이터에 대한 빠른 접근 탐색이 필요한 경우