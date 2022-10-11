## Django Auth



- Django authentication system(인증 시스템)은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공(처리)하고 있음
  - User
  - 권한 및 그룹
  - 암호 해시 시스템
  - Form 및 View 도구
  - 기타 적용가능한 시스템
- 필수 구성은 settings.py의 INSTALLED_APPS에서 확인 가능
  - django.contrib.auth 
- Authnetication(인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorizatino(권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

## 방법

1. accounts app 생성 및 등록

2. url 분리 및 맵핑

3. ```python
   ## models.py
   from django.contrib.auth.models import AbstractUser
   
   class User(AbstractUser):
       pass
   ```

4. ```python
   ## setting.py
   
   AUTH_USER_MODEL = 'accounts.User'
   ## 등록
   ## 기존 값은 'auth.User'임. global_settings.py에 있음. settings.py는 이걸 상속받음. 
   ```
   
5. 기존 User 모델이 아니기 때문에 admin에 등록을 해줘야 함. 

   ```python
   ## admin.py
   from django.contrib import admin
   from django.contrib.auth.admin import UserAdmin
   from .models import User
   
   admin.site.register(User, UserAdmin)
   ```

6. ```python
   ## forms.py
   from django.contrib.auth import get_user_model
   from django.contrib.auth.forms import UserCreationForm
   
   class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
               model = get_user_model()
   ```

   - get_user_model()
     - 현재 프로젝스테어 활성화된 사용자 모델을 반환. 
     - django에서는 User 클래스는 커스텀을 통해 변경 가능하여, 직접 참조하는 대신 get_user_model()을 사용할 것을 권장함.

7. ```python
   ## views.py
   
   def ex0():
       form = CustomUserCreationForm()
       return 
   def ex1():
       item = get_user_model().objects.all()
       return
   ## 이런 식으로 사용
   ```

8. ```python
   ## admin.py
   from django.contrib import admin
   from django.contrib.auth.admin import UserAdmin
   from django.contrib.auth import get_user_model
   
   admin.site.register(get_user_model())
   ## 강사님이 이렇게 바꿨음. 안바꿔도 돌아갈듯
   ```

   

