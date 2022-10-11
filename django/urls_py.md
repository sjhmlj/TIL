## urls.py

- url 요청은 http 요청이다. (path/메서드/헤더/프로토콜)

```python
## 기본
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
]
```

```python
## path 추가, 

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('welcome/<name>/', views.welcome),
    ## 변수를 name으로 받아와서 views.welcome에 넘긴다. 
    path('today-dinner/', views.dinner),
]

```

- 이름 붙이기

```python
## urls.py
from django.urls import path
from . import views


app_name = "todo"   

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("created/", views.create2, name="created"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
    path("updated/<int:pk>", views.updated, name="updated"),
    path("update2/<int:pk>", views.update2, name="update2"),
    path("test/", views.test, name="test"),
]
## app_name과 name을 만들면 django html에서 {% url 'todo:create' %}와 같이 사용할 수 있다. 
```

- 앱이 많을 때 url 설정하는 법

  1. 각 앱의 views 를 다른 이름으로 가져옴

  ```python
  from articles import views as articles_views
  from pages import views as pages_views
  
  urlpatterns = [
      ...,
      path('pages-index', pages_views.index)
  ]
  ```

  2. 각각의 앱에 urls.py를 만들고 매핑하기

  ```python
  # firstpjt/urls.py
  from django.contrib import admin
  from django.urls import path, include
  ## 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리하기 위해 include된 URLconf로 전달
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
      path('pages/', include('pages.urls')),
  ]
  
  # articles/urls.py
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('index/', views.index),
      path('greeting/', views.greeting),
      path('dinner/', views.dinner),
      path('throw/', views.throw),
      path('catch/', views.catch),
      path('hello/<str:name>/' views.hello),
  ]
  
  
  # pages/urls.py
  from django.urls import path
  urlpatterns = [
  ]
  ## 빈 리스트라도 있어야지 에러가 안난다. 
  ```

  

​	

---

강의자료