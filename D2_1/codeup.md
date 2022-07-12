- Input().split()
  ```python
  h, m = input().split(':') # input : 3:14. h = '3', m = '14'
  list_too = input().split(,) # input : 3,5. list_too = ['3', '5']
  ```
  
- print(a, b, sep = ' : ') 
  ` a : b `
  
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

- 