## admin

- Django의 가장 강력한 기능 중 하나인 automatic admin interface 
- “관리자 페이지” 
  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지 
  - 모델 class를 admin.py에 등록하고 관리 
  - 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음

```python
python manage.py createsuperuser
```

```python
## admin.py

from django.contrib import admin
from .models import Article

admin.site.register(Article)
```



