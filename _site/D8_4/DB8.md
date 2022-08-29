## QuerySet API

```python
print(~~~.query)
# sql문으로 보기. 
```



```sql
Entry.objects.filter(id__gt = 4)
SELECT ... WHERE id > 4;

Entry.objects.filter(id__gte = 4)
SELECT ... WHERE id >= 4;

Entry.objects.filter(id__in=[1, 2, 3])
SELECT ... WHERE id IN (1, 2, 3);

Eentry.objects.filter(headline__in = 'abc')
SELECT ... WHERE headline IN ('a', 'b', 'c');

Entry.objects.filter(headline__startswith = 'Lennnon')
SELECT ... WHERE healine LIKE 'Lennon%';

Entry.objects.filter(headline__istartswith = 'Lennon')
SELECT ... WHERE headline ILIKE 'Lennon%';
## 대소문자 구분 안함. 

Entry.objects.filter(headline__contains = 'Lennon')
SELECT ... WHERE headline LIKE '%Lennon%';

import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
SELECT ...WHERE pub_date
BETWEEN '2005-01-01' and '2005-03-31';

## 복합 활용
inner_qs = Blog.objects.filter(name__contains = 'Cheddar')
entries = Entry.objects.filter(blog__in=onner_qs)
SELECT ...
WHERE blog_id IN (SELECT id FROM ... WHERE name LIKE '%Cheddar%');

Entry.objects.all()[0]
SELECT ... LIMIT 1;

Entry.objects.order_by('id')
SELECT ... ORDER BY id;

Entry.objects.order_by('-id')
SELECT ... ORDER BY id DESC;


```

```python 
class Genre(models.Model) :
	name = models.CharField(max_length=30)

class Artist(models.Model) :
  name = models.CharField(max_length=30)
  debut = models.DateField()
  
class Album(models.Model) :
  name = models.CharField(max_length=30)
  genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
  ## 테이블에 genre_id로 됨. foreignkey의 기능임. 
  artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
```

- models.ForeignKey 필드

  - 2개의 필수 인자
    - Model class : 참조하는 모델
    - on_delete : 외개 키가 참조하는 객체가 삭제되었을 때 처리 방식
      - CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제
      - PROTECT : 삭제되지 않음 - 부모객체 삭제 불가
      - SET_NULL : NULL 설정
      - SET_DEFAULT : 기본 값 설정. 
- FK
  - 키를 사용하여 부모 테이블의 유일한 값을 참조한다(참조 무결성)
    - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
  
  - 왜래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 한다. 
  

```python
# FK 참조
artist = Artist.objects.get(id=1)
Genre = Genre.objects.get(id=1)

album = Album()
album.name = '앨범1'
album.artist = artist
# db 에는 artist_id로 되어있기 때문에 album.artist_id = 1 이렇게 저장할 수도 있음	
album.genre = genre
album.save()
```



```python
# N의 입장에서 1을 가져오기
> album = Album.objects.get(id=1)
> album.genre.name
# FK로 인스턴스가 들어가 있어서 이런 식으로 작동 가능. 
# 참조

#1의 입장에서 N을 가져오기
> g1 = Genre.objects.get(id=1)
> g1.album_set.all()
# 역참조
```



## 실습

- getattr()

  ```python
  getattr(Genre, 'name')
  # Gernre.name
  ```



---

강의자료

