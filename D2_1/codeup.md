- Input().split()
  ```python
  h, m = input().split(':') # input : 3:14. h = '3', m = '14'
  list_too = input().split(,) # input : 3,5. list_too = ['3', '5']
  ```
  
- print(a, b, sep = ' : ') 
  ` a : b `
  
  print 함수는 객체들을 str타입으로 형변환한 다음에 출력해준다. 
  
- a = int(input().split())
  
  ` TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'`

- ```python
  numbers = [3, 10, 20]
  n = int(numbers.split(', '))
      # 'list' object has no attribute 'split'
  ```

- ```python
  numbers = [3, 10, 20]
  for i in numbers : 
    ## 이러면 i 는 3, 10, 20 이 들어간다. 
  ```

- ```python
  for i in range(len(numbers_2)) :
      numbers_2.remove(l)  
      ## 이런식은 에러가 남. ValueError: list.remove(x): x not in list
      ## while 문이 적절한것 같다. 
  ```

- ```python
  word = list(input())
  word_2 = str(word) ### word_2는 스트링이긴 한데 '[]'꼴의 스트링이다. 
  ```

- ```python
  word = 'hello'             ## 스트링을 거꾸로 할 때 
  word_inverse = word[::-1]  ## 이런 활용을 못 떠올렸다. 순서가 있는 컨테이너는 다 이렇게 활용할 수 있는 것 같다. 
  ```

- ```python
   ## 문자열은 변경이 안된다고 생각해서 문자열을 만들 수 있다는 생각을 하지 못했다. 
  word = ''
  word += 'hello!'    ## 추가는 된다. 다시 생각해보면 print() 를 쓰는 과정에서 스트링을 이어 붙이는 것을 봤는데, 깊게 생각을 못했다. 
   ## 또한 문자열을 붙이는 과정에서 순서를 뒤집을 수 있다는 것이 새로웠다.  a + b = ab , b + a = ba
  ```

- ```python
  format(a, ".2f")  ## float a를 소수점 둘째자리까지 나타내는 것 같다. 
  ```

- ```python
  for i in word :
      
      dic.update( i = cnt) ## 이렇게 안되는 이유는 update 안의 i가 스트링으로 인식되기 때문인 것 같다. 
  ```

- ```python
  연산자 우선순위를 알고 코딩해. 
  ```

- ```python
  for i in word :
      cnt_i = 0           ## 이런 식으로 작동하지 않는다. 
  ```

- 