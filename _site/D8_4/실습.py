

<3>
directors = [
    ("봉준호","1993-01-01","KOR"),
    ("김한민","1999-01-01","KOR"),
    ("최동훈","2004-01-01","KOR"),
    ("이정재","2022-01-01","KOR"),
    ("이경규","1992-01-01","KOR"),
    ("한재림","2005-01-01","KOR"),
    ("Joseph Kosinski","1999-01-01","KOR"),
    ("김철수","2022-01-01","KOR"),
]

for director in directors:
    name_ = director[0]
    debut_ = director[1]
    country_ = director[2]
    Director.objects.create(name=name_, debut=debut_, country=country_)

genres = ["액션","드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()


<4>
director =  Director.objects.get(id=1)
col = ['id', 'name', 'debut', 'country']

for i in col :
    result = getattr(director, i)
    print(i, ':', result)

<5>
genre = Genre.objects.get(title = '드라마')

print('id :',genre.id)
print('title :',genre.title)

<6>
import datetime
director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

movie = Movie()
movie.director = director_
movie.genre = genre_
movie.title = '기생충'
movie.opening_date= datetime.date(2019, 5, 30)
movie.running_time = 132
movie.screening = False
movie.save()

<7>
movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]
### 여긴 실패!-----------------------------------
# col = ['director', 'genre', 'title', 'opening_date', 'running_time', 'screening']
# for i in movies :
#     movie = Movie()
#     for k in range(1, 3) :
#         if k == 1 :
#             director_ = Director.objects.get(name = i[k])
#             a = director_
#         else :
#             genre_ = Genre.objects.get(title = i[k])
#             a = genre_
#         getattr_ = getattr(movie, col[j])
#         getattr_ = a
#     for j in range(3, 5) :
#         getattr_ = getattr(movie, col[j])
#         getattr_ = i[j]
#     movie.save()
#-------------------------------------------------
for i in movies :
    director_ = Director.objects.get(name = i[0])
    genre_ = Genre.objects.get(title = i[1])
    movie = Movie()
    movie.director = director_
    movie.genre = genre_
    movie.title = i[2]
    movie.opening_date = i[3]
    movie.running_time = i[4]
    movie.screening = i[5]
    movie.save()        

<8>
movie = Movie.objects.all()
col = ['director', 'genre', 'title', 'opening_date', 'running_time', 'screening']
for i in movie :
    result = []
    for j in col :
        result.append(getattr(i, j))
        
    print(*result)

<9>

movie = Movie.objects.all()
col = ['director', 'genre', 'title', 'opening_date', 'running_time', 'screening']
for i in movie :
    result = []
    for j in col :
        if j =='director' :
            result.append(getattr(i, j).name)
        else :
            result.append(getattr(i, j))
        
    print(*result)

<10>
movie = Movie.objects.all()
col = ['director', 'genre', 'title', 'opening_date', 'running_time', 'screening']
for i in movie :
    result = []
    for j in col :
        if j =='director' :
            result.append(getattr(i, j).name)
        elif j == 'genre' :
            result.append(getattr(i, j).title) 
        else :
            result.append(getattr(i, j))
        
    print(*result)    

<11>

movie = Movie.objects.order_by('-opening_date')
for i in movie :
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)

<12>
movie = Movie.objects.order_by('-opening_date')[0]
print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)    

<13>
movie = Movie.objects.filter(screening = True).order_by('opening_date')
for i in movie :
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)

<14>
bong = Director.objects.all().filter(name = '봉준호')
movie = Movie.objects.filter(director__in = bong).order_by('opening_date')
for i in movie :
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)

<15>
bong = Director.objects.all().filter(name = '봉준호')
movie = Movie.objects.filter(director__in = bong).order_by('opening_date')[1]
i = movie
print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)

<16> 
movie = Movie.objects.filter(running_time__gt =119).order_by('running_time')
for i in movie :
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)

<17>
16번과 중복

<18>
movie = Movie.objects.filter(opening_date__gt = '2022-01-01').order_by('opening_date')
for i in movie :
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)

<19>
bong = Director.objects.all().filter(name = '봉준호')
drama = Genre.objects.all().filter(title = '드라마')
movie = Movie.objects.filter(director__in = bong, genre__in = drama).order_by('opening_date')
for i in movie :
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)


<20>
bong = Director.objects.all().filter(name = '봉준호')
movie = Movie.objects.exclude(director__in = bong).order_by('opening_date')
for i in movie :
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)