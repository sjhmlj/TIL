#### 개요
- Heap, Set

- 우선순위 큐를 구현하는 방법 
  - 배열
  
  - 연결 리스트
  
  - 힙
  
    |                   | enqueue | dequeue |
    | ----------------- | ------- | ------- |
    | 배열              | O(1)    | O(n)    |
    | 정렬된 배열       | O(n)    | O(1)    |
    | 연결 리스트       | O(1)    | O(n)    |
    | 정렬된 연결리스트 | O(n)    | O(1)    |
    | 힙                | O(logn) | O(logn) |
  
    
## 힙(Heap)
- 힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한다.
  - max heap : 부모의 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
  - min heap : 부모의 노드의 키값이 자식 노드의 키값보다 항상 큰 힙
- 이러한 속성으로 인해 힙에서는 가장 낮은(혹은 높은) 우선순위를 가지는 노드가 항상 루트에 오게 되고 이를 이용해 우선순위 큐와 같은 추상적 자료형을 구현할 수 있다. 이때 형제노드 사이에는 대소 관계가 정해지지 않는다. 
- 파이썬 heapq 모듈은 heapq(priority queue) 알고리즘을 제공한다. (최소 힙)
  ```python
  heapq.heappush(heap, item) ## item을 heap에 추가
  heapq.heappop(heap) ## heap에서 가장 작은 원소를 pop &리턴. 비어 있는 경우 IndexError가 호출됨
  heapq.heapify(x) ## 리스트 x를 즉각적으로 heap으로 변환함. (O(n))
  
  import heapq
  
  heap = []
  heapq.heappush(heap, 50)
  heapq.heappush(heap, 10)
  heapq.heappush(heap, 20)
  
  print(heap)
  ## [10, 50, 20]
  
  ```
- 최대 힙 구현을 위해서는 힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다. 
  ```python
  import heapq
  heap_items = [1, 3, 5, 7, 9]
  
  max_heap =  []
  for item in heap_items :
    heapq.heappush(max_heap, (-item, item))
  
  print(max_heap)
  ## [(-9, 9), (-7, 7), (-3, 3), (-2, 2), (-5, 5)]
  ```
  
- 구현 예시(내 임의)
  ```python
  T = 13
  L = [n for n in range(1, 8)]
  
  import heapq
  
  def my_heap_example(T, L) :
      heapq.heapify(L)
      answer = 'Yes'
      while L[0] < T :
          num = heapq.heappop(L) + heapq.heappop(L)
          heapq.heappush(L, num)
          if len(L) < 2 :
              if L[0] < T :
                  answer = 'No'   
              break
  
      return answer, L
  
  result = my_heap_example(T, L)
  print(result)
  ```

- |             | heap    | list           |
  | ----------- | ------- | -------------- |
  | get item    | O(1)    | O(1)           |
  | insert item | O(logn) | O(1) 또는 O(n) |
  | delete item | O(logn) | O(1) 또는 O(n) |
  | search item | O(n)    | O(n)           |

## 셋(Set)

- 셋은 수학에서의 '집합'을 나타내는 데이터 구조이다. 

- 셋은 언제 사용해야 할까?
  - 데이터의 중복이 없어야 할 때
  - 정수가 아닌 데이터의 삽입/삭제/탐색이 빈번히 필요할 때

- 셋의 연산
  |            |           |                                |      |
  | ---------- | --------- | ------------------------------ | ---- |
  | 탐색       | .add()    |                                | O(1) |
  | 제거       | .remove() |                                | O(1) |
  | 합집합     | +, \|     | set.union(a, b)                | O(1) |
  | 교집합     | &         | set.intersection(a, b)         | O(n) |
  | 차집합     | -         | set.difference(a, b)           | O(n) |
  | 대칭차집합 | ^         | Set.symmetric_difference(a, b) | O(n) |

  - 추가적으로 메서드 _update()도 있음. 

    ```python
    a = {1, 2, 3, 4}
    a.intersection_update({0, 1, 2, 3})
    ## {1, 2, 3}
    ```

- 부분집합과 상위집합 확인하기

  - <= , a.issubset()
  - <
  - \>= , a.issuperset()
  - \>

- 겹치지 않는지 확인 -> a.isdisjoint()



---
[아기여우 블로그](https://littlefoxdiary.tistory.com/3)
[파이썬_](https://docs.python.org/2/library/heapq.html)
강의 자료