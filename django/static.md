

- 웹 서버는 특정 위치(URL)에 있는 자원(resource)을 요청(HTTP request) 받아서 제공(serving)하는 응답(HTTP response)을 처리하는 것을 기본 동작으로 함
- 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource)를 제공

##  static files

- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일. (사용자의 요청에 따라 내용이 바뀌지 않음)

- 이미지, CSS, JS 등

- 활용

  ```django
  {% load static %}
  ## 사용자 정의 템플릿 태그 세트를 로드. 
  ## 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 불러옴
  <img src="{% static 'my_app/example.jpg' %}" alt="">
  ## 여기서 static은 폴더 명을 가리키는 게 아님. STATIC_ROOT에 저장된 정적 파일에 연결
  ## my_app/static/my_app/example.jpg
  ## static 폴더는 templates 폴더와 비슷한 개념
  ```

- STATIC_URL

  - STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
    - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 'app/static/' 경로 (기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색함. 
  - 실제 파일이나 디렉토리가 아니며, URL로만 존재

  ```python
  ## settings.py
  
  STATIC_URL = '/static/'
  ## 값 바꿔도 작동함. static file의 url만 달라짐. 
  ```

- STATICFILES_DIRS

  - 'app/static/' 디렉토리 경로를 사용하는 것외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
  - 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

  ```python
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```

- STATIC_ROOT

  - collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 정적 경로
  - django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
  - 개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음
    - 직접 작성해야 함. 
  - 실 서비스 환경(배포 환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함

  ```bash
  ## collecstatic 명령어
  $ python manage.py collectstatic
  ```

  ```python
  STATIC_ROOT = BASE_DIR / 'staticfiles'
  ```

  

---

강의자료

https://docs.djangoproject.com/en/3.2/howto/static-files/



