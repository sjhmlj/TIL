# 모듈

- 다양한 기능을 하나의 파일로(=패키지)
- 패키지가 모여 있으면 라이브러리
- 패키지나 라이브러리를 관리하는 관리자 = pip
- 모듈 : 특정 기능을 하는 코드를 파일(.py) 단위로 작성한 것. 
- 패키지 : 
- 파이썬 표준 라이브러리 (PSL) : 파이썬에 기본적으로 설치된 모듈과 내장 함수. 

# PSL

```python
import datetime
now = datetime.datetime.now()
print(now)

from datetime import datetime        
now = datetime.now()
print(now)
```

```python
with open('test.txt', 'w', encoding = 'utf-8') as f:
    f.write('Happy Hacking!\n')
    for i in range(1, 5) :
        f.write(f'{i} 번째!\n')
```

```python
with open('test.txt', 'r', encoding = 'utf-8') as f:
 
    text = f.read()
    print(text, type(text))

```

# JSON

- 문자열 형식?
- 딕셔너리와 리스트를 조작
- 

---

<출처>

멀티캠퍼스 강의

https://wikidocs.net/28