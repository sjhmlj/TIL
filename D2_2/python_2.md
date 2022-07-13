## 제어문
- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 **선택적으로 실행**하거나 **계속하여 실행**하는  제어가 필요함 
- 제어문은 순서도(flow chart)로 표현이 가능

### 조건문
- 참/거짓을 판단할 수 있는 조건식과 함께 사용

- expression에는 참/거짓에 대한 조건이 들어간다. 
  ```python
  if <expression> :
    # space 4
  else :
    # space 4
  ```
  
- 복수 조건문
  
  복수의 조건식을 활용할 경우 elif를 활용하여 표현함 (동시에 검사하는 것이 아니라 순차적으로 비교)
  
  ```python
  if <expression> :
      # code block
  elif <expression> :
      # code block
  elif <expression> :
      # code block
  else : 
      # code block
  ```
  
- 중첩 조건문 - 가능!
  ```python
  if <expression> :
      # code block
      if <expression> :
          #code block
  else : 
      # code block
  ```
  
- 조건 표현식
  <True인 경우 값> if <expression> else <false인 경우 값>
  
  ```python
  value = num if num >= 0 else -num ## 성립
  
  if num >= 0 :    ## 이것과 같음
      value = num
  else :
    	value = -num
  ```
  👀이런 문법이 성립하는 이유는 뭘까? 오른쪽 부터 읽는다는 것? 그냥 이런 문법을 만든건가?
  🐝elif 등이 안되는 걸 보면 그냥 자주 쓰는 형태여서 문법을 따로 만든 것 같다. 
  
### 반복문
- 특정 조건을 만족할 때까지, 계속 반복되는 일련의 문장
  - while문
    종료조건에 해당하는 코드를 통해 반목문을 종료시켜야 함
  - for 문
    반복가능한 객체를 모두 순회하면 종료(별도의 종료조건이 필요 없음)
  
- while문
  - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨
  - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
  - while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요
    ```python
    while <expression> :
        # code block
    ```
  
- for 문
  - for문은 시퀀스를 포함한 순회가능한 객체요소를 모두 순회함
    ```python
    for <변수명> in <iterable> : 
        # code block
        
    chars = input()
    for i in range(len(chars)) :
    print(chars[i])
    ```
    
  - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용한다. 
  
  - enumerate 순회
  
    인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환. 튜플로 구성됨
  
    ```python
    members = ['minsoo', 'yeonghui', 'cheolsoo']
    
    for i in range(len(members)) :
        print(f'{i} {members[i]}')
    for i, member in enuberate(members) :
      print(i, member)
    ```
  
    
  
    
  
- 반복문 제어
  - break : 반복문을 종료
  - continue : continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
  - for-else : 끝까지 반복문을 실행한 경우에  else문 실행 (break을 통해 for문이 종료되면 실행 안됨)
    ```python
    for char in 'apple' :
        if char == 'b' :
            print('b!')
            break
    else : print('b가 없습니다.') # b가 없습니다.
    ```
    ---
    출처
    강의 교재