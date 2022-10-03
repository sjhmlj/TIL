## templates

- 앱 폴더 안에 templates 폴더를 직접 생성하고, templates 폴더 안에 필요한 html 파일을 생성한다. 

## template namespace

- Django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾을 수 있으며, settings.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링 함

```python
## settings.py
TEMPLATES = [
    {
        ...,
        'APP_DIRS': True,
        # 이 속성 값이 해당 경로를 활성화 하고 있음. 
        ...
	}, 
]
```

- Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 app_name/templates/app_name/ 형태로 변경

```python
def update(request, pk):
    item = myTodo.objects.get(id=pk)
    context = {
        "item": item,
        "pk": pk,
        "deadline": str(item.deadline),
    }
    return render(request, "todo/update.html", context)
```



## DTL(django template language)

```django html
<!-- for문 -->
{% for item in items %}
{% endfor %}
```



## base.html 

- html을 상속하는 방법이다. 

  1. 프로젝트 폴더 바로 아래 templates 폴더를 생성하고 그 안에 base.html을 생성한다. 
  2. settings.py에서 밑의 코드를 만든다.

  ```python
  # settings.py
  TEMPLATES = [
      {
          'DIRS': [BASE_DIR/'templates'],
      }
  ]
  ```

  ```html
  <!-- base.html -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body class="container mt-5 bg-lightblue">
    {% block content %}
      <!-- content 부분이 이름임. -->
    {% endblock %}
  </body>
  </html>
  ```

  ```django
  <!-- base.html을 상속받을 html -->
  {% extends 'base.html' %}
  {% block content %}
  <!-- 여기다 작성 --->
  {% endblock %}
  ```

  

---

강의자료