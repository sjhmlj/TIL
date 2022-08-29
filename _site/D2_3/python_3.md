# 함수

```python
len('happy!')   ## 비교!

word = 'happy!'
cnt = 0
for char in word :
    cnt += 1
```
## 우리는 왜 함수를 사용할까? 
- Decomposition . 
  기능을 분해하고 재사용이 가능하다. 
  `print(sum(numbers)/len(numbers))`
-  Abstraction
  복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음.
## 1. 함수란?
- 특정한 기능을 하는 코드의 조각(묶음)
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 사용
- 사용자 함수 
  - 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능. 
- [내장함수](https://docs.python.org/3/)
## 2.  함수 기본 구조
### 2.1. Define & Call
- 함수는 parameter를 넘겨줄 수 있음

- 함수는 동작 후에 return을 통해 결과값을 반환함
  ```python
  def foo() :
      return True
  def add(x, y) :
      return x + y
  ```

- 함수는 함수명으로 호출

  > 함수 부분(def ~)은 호출 될 때 연산된다. 그 전에는 윗 줄에 있어도 안 읽히는 것 같다.
### 2.2. Input
- parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
    ```python
    def function(ham) :  ## parameter : ham
        return ham
    print(function(spam)) ## argument : spam
    ```

- Argument : 함수를 호출할 때, 넣어주는 값. parameter를 통해 전달.
  - argument는 소괄호 안에 할당 func_name(argument)

    - 필수 argument
    - 선택 argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

  - 위치에 따른 분류

    - positional arguments

      : 기본적으로 함수 호출 시 argument는 위치에 따라 함수 내에 전달됨

    - keyword argument

      * 직접 변수의 이름으로 특정 Argument를 전달할 수 있음. 
      
      * keyword argument 다음에 positional argument를 활용할 수 없음. 반대는 가능
      
        ```python
        add (2, y = 5)
        ```

  - default arguments values
    : 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함.  

    ```python
    def add(x, y=0) : 
        return x + y  
    ```

    👀근데 이러면 블록 안에서 값을 넣는 거랑 뭐가 다를까?

  - 정해지지 않은 개수의 arguments

    : 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용.

    - 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때 유용. Ex) print()
    - arguments는 튜플로 묶여 처리됨. 

  - 정해지지 않은 개수의 keyword arguments

    - 함수가 임의의 개수 argument를 keyword argument로 호출될 수 있도록 지정
    - argument들은 딕셔너리로 묶여 처리됨. 

    ```python
    def add(*args) :
        return args      ## 내부에서는 args를 튜플로 활용
    result = add(1, 2, 3)
    def add_2(**kwargs) :
        return kwargs   ## 내부에서는 kwargs를 딕셔너리로 활용
    ```
### 2.3. Scope
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
  - scope 
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
  - variable
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수
- 객체 수명주기
  - bulilt-in-scope
    : 파이썬이 실행된 이후부터 영원히 유지. ex) print, sum, len, ...
  - global scope
    : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지    ex) a = 3
  - local scope 
    : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
- 이름 검색 규칙(name resolution)
  - 파이썬에서 사용되는 이름(식별자)들은 이름공간에 저장되어 있음. 
  - 아래와 같은 순서로 이름을 찾아나가며, 이를 LEGB Rule이라고 부름
    1. Local scope
    2. Enclosed scope
    3. Global scope
    4. Built-in scope
  - 함수 내에서 바깥 scope의 변수에 접근은 가능하지만 수정은 불가능하다. (함수 내에서만 바꿔쓸 수 있다.)
    ```python
    sum = 5
    print(sum[1, 2, 3]) ## 오류가 남. sum -> global이 먼저 읽혔기 때문. 
    ```
### 2.4. Output 
- 함수는 반드시 하나의 값만을 리턴한다. 
  ```python
  def foo(x, y) :
      return x + y, x - y ## 된다.
      ## 타입을 찍어보면 튜플이 나온다. 
  ```
- 함수는 return과 동시에 실행이 종료된다. 
  ```python
  def foo(x, y) :     ## 실행은 되고, 위의 return 값만 반환된다.
      return x + y
      return x - y    ## 이 코드로의 접근이 불가능하다. 
  ```
  
- 함수를 선언했지만 return 코드를 작성하지 않으면 None을 반환한다. 
  ```python 
  ## print 함수는 출력을 해주고, Return 값은 없습니다. --- 좀 생각 해봐야겠다. 어떤식으로 돌아가는지. 
  a = print('hi')    # hi 가 출력된다.
  print(a, type(a))  # None, Nonetype
  ```
- return vs print
  : return은 함수 안에서 값을 반환하기 위해 사용되는 키워드이고, print는 출력을 위해 사용되는 함수이다. 차이점을 잘 생각해봐.  
## 3. 함수 응용
- map(function, iterable)
  
  : 순회가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환. 
  
  ```python
  <map object at 0x101287610> # 이미 함수가 적용된 상태임. 볼려면 list로 형변환해서 봐
  ```
  어떤 함수를 반복가능한 것들의 요소에 모두 적용시킨 결과! 결과는 map object

---

출처

강의 자료
