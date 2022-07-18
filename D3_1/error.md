## 디버깅

#### 어느 부분을 중점적으로 봐야 할까?
---

- branches 
  - 모든 조건이 원하는대로 동작하는지

- for loops
  - 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
- while loops
  - for loops와 동일, 종료조건이 제대로 동작하는지
- function
  - 함수 호출 시, 함수 파라미터, 함수의 결과

#### 어떤 방식으로?
---

- *"코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅 도구는 없습니다."*

- print 함수 활용
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
  - Breakpoint, 변수 조회 등
- Python tutor  활용(단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅

---

- 에러 메시지가 발생하는 경우
  - 해당하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
  - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해 보기
    - 전체 코드를 살펴보기
    - 휴식 하기
    - 누군가에게 설명해보기

### 문법 에러(Syntax Error)

---

- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음. 

- 파일 이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿 기호(^)를 표시![스크린샷 2022-07-18 오후 1.35.22](hihi.assets/스크린샷 2022-07-18 오후 1.35.22.png)

- 종류

  - EOL(End of Line)

    ```python
      File "/Users/seojuhyeon/Desktop/TIL/D3_1/test.py", line 2
        print('a
                ^
    SyntaxError: EOL while scanning string literal
    ```

  - EOF(End of File)

    ```python
        
        ^
    SyntaxError: unexpected EOF while parsing
    ```

  - Invailid syntax

    ```python
        while
             ^
    SyntaxError: invalid syntax
    ```

  - assign to literal

    ```python
        5 = 3
        ^
    SyntaxError: cannot assign to literal
    ```

    

### 예외(Exception)

---

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
  
- 실행 중에 감지되는 에러들을 예외(exception)라고 부름

- 예외는 여러 타입으로 나타나고, 타입이 메시지의 일부로 출력됨
  - NameError, TypeError 등은 발생한 예외 타입의 종류
  
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐

- 사용사 정의 예외를 만들어 관리할 수 있음. 

- 종류

  - ZeroDivisionError : 0으로 나누고자 할 때 발생

  - NameError : namespace 상에 이름이 없는 경우

  - TypeError : 해당 타입의 수행가능한 작업이 아닐 때, argument 수가 맞지 않을 때, ...

    ```python
        1 + '1'
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    ```

    ```python
        round('3.5')
    TypeError: type str doesn't define __round__ method
    ```

    ```python
        random.sample(1, 2)
      File "/Users/seojuhyeon/.pyenv/versions/3.9.13/lib/python3.9/random.py", line 433, in sample
        raise TypeError("Population must be a sequence.  For dicts or sets, use sorted(d).")
    TypeError: Population must be a sequence.  For dicts or sets, use sorted(d).
    ```

  -  ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우

    ```python
        int('7.7')
    ValueError: invalid literal for int() with base 10: '7.7'
    ```

  - IndexError 

  - KeyError

  - ModuleNotFoundError

  - ImportError : Module은 있으나 존재하지 않는 클래스/ 함수를 가져오는 경우

  - IdentationError 

    ```python
    IndentationError: expected an indented block
    ```

  - KeyboardInterrupt
  - [파이썬 내장예외 계급도](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)

### 예외처리

---

- try문(statement) / except 절을 이용하여 예외 처리를 할 수 있음
- try문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생하지 않으면 except 없이 실행 종료
- except문
  - 예외가 발생하면 except 절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

  ```python
  try :           ## 오류가 발생할 가능성이 있는 코드를 실행. try 문은 반드시 한 개 이상의 except 문이 필요!!
    ## 
  except :        ## try 문에서 예외가 발생 시 실행함
    ##            ## except 는 elif 처럼 쌓을 수 있음. 
  else :          ## try 문에서 예외가 발생하지 않으면 실행함
    ##
  finally :       ## 예외 발생 여부와 관계없이 항상 실행함. 
    ##
  ```

```python
try : 
    num = input('숫자 입력 : ')
    print(f'입력하신 숫자는 {int(num)}입니다.')

except ValueError :
    print('숫자를 입력해 주세요')
```



![스크린샷 2022-07-18 오후 2.15.37](hihi.assets/스크린샷 2022-07-18 오후 2.15.37.png)

### 예외 발생 시키기

---

- raise를 통해 예외를 강제로 발생 
  - raise <표현식>(메시지). <표현식>에는 예외 타입 지정. 

