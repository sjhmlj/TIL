# list comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

- [\<expression> for \<변수> in \<iterable>]

 ```python
  cubic_list = []
  for number in range(1, 4) :
    cubic_list.append(number**3)
  ## 밑에랑 같다. 
  multi3_list = [number**3 for number in range(1, 4)]
  even_list = [i for i in range(10) if i % 2 == 0]    ## 이렇게 뒤에 조건식도 추가할 수 있다. 
 ```

  



# dictionary comprehension

- {\<key> : \<value> for \<변수> in \<iterable>}

```python
{number : number**3 for number in range(1, 4)}
```

# lambda 

- 람다 함수
  - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
  - lambda \<parameter> : 표현식
- 특징
  - return 문을 가질 수 없음
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용 가능

```python
number = [1, 2, 3, 4, 5]
print(list(map(lambda n : n*3, numbers)))
## [3, 6, 9, 12, 15]
print(list(filter(lambda n: n%3==0, numbers)))
## [3]
```

# filter

- filter(function, iterable)

- iterable한 오브젝트에 fuc를 적용하고, 그 결과가 True인 것들을 filter object로 반환

  ```python
  numbers = [1, 2, 3, 4, 5, 6, 9, 10, 12]
  print(list(filter(lamda n : n % 3 == 0, numbers)))
  ```

# 어노테이션

```python
a : int = 3
print(a)

def add(x: int, y : int) -> int :       ## 어노테이션. 팁, 메모 같은 개념. 
  print(x+y)
```



# 파이썬 개발환경

## 파이썬 패키지 관리자(pip)

- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
- 패키지는 최신버전 / 특정 버전/ 최소 버전을 명시하여 설치할 수 있음
- 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음
- pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

```python
$ pip install SomePackage
$ pip install SomePackage==1.0.5
$ pip install 'SomePackage>=1.0.4'

$ pip uninstall SomePackage

$ pip list
$ pip show SomePackage
$ pip freeze                 ## 설치된 패키지의 목록을 pip install에서 활용되는 형식을 출력
     			 									## 해당하는 목록을 requirements.txt(관습)으로 만들어 관리함
  
$ pip freeze > requirements.txt
$ pip install -r requirements.txt      ## 둘 다 뭔지 모르겠음
```

## 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야 함.

- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음

  - 과거 외주 프로젝트 -django 버전 2.x
  - 신규 회사 프로젝트 -django 버전 3.x
  - 이런 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음. 

- 파이썬은 특정 경로에 있는 프로그램을 실행시키는 것임

- venv : 가상 환경을 만들고 관리하는데 사용되는 모듈(Python 3.5부터)

  - 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음. 
    - 특정 폴더에 가상환경(패키지 집합 폴더 등)이 있고
    - 실행 환경에서 가상환경을 활성화 시켜서 
    - 해당 폴더에 있는 패키지를 관리/사용함

  - 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨![스크린샷 2022-07-21 오후 9.27.40](python.assets/스크린샷 2022-07-21 오후 9.27.40.png)

- ```python
  # 프로젝스 폴더 생성. 
  
  $ python -m venv venv(<폴더명)            # 가상환경 생성
  
  $ source venv/Scripts/activate    # 가상환경 실행
  # (venv) -> 가상환경
  
  ## 이 프로젝트 폴더에 파이썬 실행/패키지 등등을 만든다. 그리고 이걸로 실행할 수 있게 해준다.
  ```
## 좀 새로웠던 것
---

```python
def is_3(n) :           ## 두개는 동일한 코드. 
  return n % 3 == 0

def is_3_1(n) :
  if n % 3 == 0 :
    return True
  else :
    return False
```

---

> 패키지 버전 vs 파이썬 버전???????????????????

![스크린샷 2022-07-21 오전 11.52.32](python.assets/스크린샷 2022-07-21 오전 11.52.32.png)

---

강의자료

