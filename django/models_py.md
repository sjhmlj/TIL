## models.py

```python
from pyexpat import model
from django.db import models


class Todo(models.Model):
    content = models.CharField(max_length=80)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
```

- 테이블 다 만들었으면 DB에 반영

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

```python
## views.py
from django.shortcuts import render
from .models import Todo

def index(request):
    items = Todo.object.all()
    return render(request, 'index.html', {'items': items})

```





---

강의자료