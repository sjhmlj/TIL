 ## ORM (Object-Relational-Mapping)

- 객체 지향 프로그램이 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그램이 기술
- 파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크에서는 내장 Django ORM을 활용



```python
from django.db import migrations, models
class Genre(models.Model) :
  name = models.CharField(max_length=30)
```



## migration

- 모델의 변경 내역을 DB 에 적용시키는 장고의 방법이라고 한다. 
- models.py 와 클래스를 통해 DB 스키마를 생성하고 컨트롤하게 된다. 이 때 DB 스키마를 git처럼 버전으로 나눠서 관리 할 수 있게 해 주는 시스템이다. 

```python 
$python manage.py makemigrations [app_name]
# 마이그레이션을 생성하는 명령어. app_name을 입력하면 해당 app에 대해서만 마이그레이션을 생성하고, app_name을 생략하면 전체 app 에 대해서 마이그레이션을 생성함. 

$python manage.py migrate [app_name] [migration_name]
# 마이그레이션을 적용하는 명령어. 즉 실제 DB에 변경사항을 적용하는 명령어. 마이그레이션 파일의 이름을 지정하면 해당 번호(버전)의 마이그레이션을 적용하게 된다. 즉 이전 버전으로 되돌리는 것도 가능하다. 

$python manage.py showmigrations [app_name]
# 프로젝트의 마이그레이션에 대해 적용 여부를 한 눈에 보여줌

$python manage.py sqlmigrate app_name migration_name
# 해당 마이그레잉션 파일이 어떤 SQL 구문으로 실행되는지 보여줌. 
```



#### 주의

- 적용된 마이그레이션 파일은 절대로 삭제하면 안된다. 각 마이그레이션은 이전 버전에 대해 의존성을 가지기 때문이다. 마이그레이션 파일을 삭제하려면 반드시 적용을 해제하고 삭제해야 한다. 

## 실습

- manage.py 는 Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인의 유틸리티이다. 

  Django project directory를 만들면 default로 들어있으며, 프로젝트 패키지가 들어 있다. 

```python
$ python -m venv venv
# 가상환경 생성
$ . venv/bin/activate
# 가상환경 실행
# 가상환경 종료는 $ deactivate
$ pip install -r requirements.txt
$ python manage.py --version
# django 패키지 설치 확인
```

> 제공하는 폴더에서 실습해야 하는 줄 모르고, 나 혼자 막 이리저리 하다가 시간을 많이 소비했다.
>
> $ pip install -r requirements.txt 를 했는데, 텍스트 파일이 없길래
>
> $ pip freeze > requirements.txt 를 했다. 비어 있는 파일이었다. 여기서 좀 이상한걸 느꼈는데, 그냥 지나갔다. 
>
> 상식적으로 생각해보면 $ pip freeze > requirement.txt 가 어떻게 내게 필요한 파일을 알고 그 안에 정보를 담고 있겠냐. 이상하긴 했는데, 구글에서 다 이렇게 하라 그러니까 따라했다. 나중에 보니까 서버측과 클라이언트 측이 다른데, 나는 그 둘을 구글링에서 구별하지 못한 거였다. requirements.txt는 서버측에서 제공하는거다. 

```python
$python manage.py shell_plus
# 이 명령어를 치면 어디로 들어감. 

Genre.objects.all()
# class name / manager / QuereSet API

Genre.objects.get(id =1)

Genre.objects.filter(name = '주현')

## get 메서드는 하나만 리턴한다. 만약 get 조건에 부합하는 레코드가 여러개이면 에러가 뜬다.
## filter 메서드는 결과가 QuerySet으로 나온다. 일종의 리스트이다. 

genre = Genre.objects.all()
# 인스턴스 이용
genre1 = Genre.objects.get(id=1)
genre1.name = '힙합'
genre1.save()
# save 를 해야지 db에 반영됨
genre.delete()
# delete는 save 필요 없음. 
```

```python
# main.py 에 작성하고
# $python main.py 를 실행히도 됨. 
# 아래는 실습 main.py 파일에 들어 있던 구문.  
import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *
```



---

[개발하는 중생](https://tibetsandfox.tistory.com/24)

[초보몽키의 개발공부로그](https://wayhome25.github.io/django/2017/03/20/django-ep6-migrations/)

[docs.djangoproject](https://docs.djangoproject.com/ko/4.1/ref/django-admin/#cmdoption-settings)

