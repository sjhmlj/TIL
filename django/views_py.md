## views.py

```python
from django.shortcuts import render

def index(request):
    ## request는 dir로 확인할 수 있다. 
    ## 보통 html의 form 태그에서 보낸 값이 들어온다. 
    ## request.GET.get('name')
    return render(request, 'index.html')
```

```python
from django.shortcuts import render

def index(request):
	context={
        'a': 1,
        'b', 2, 
    }
    return render(request, 'index.html', context)
## render의 세번째 인자로 딕셔너리를 넣을 수 있다. 딕셔너리의 내용이 html에 전달된다. 
```

- redirect

  ```python
  from django.shortcuts import render, redirect
  
  def index(request):
      
      return redirect('article/index')
  ```

  





---

강의자료