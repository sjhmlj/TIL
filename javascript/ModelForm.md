## ModelForm

- 사용하는 이유

  - DB 필드가 사실상 HTML의 Form과 같기 때문에 연동 시키는 거다.  DB 필드가 바뀌면 자동으로 연동되니까 편할거 같다. 
  - 유효성 검사: 서버 사이드에서는 사용자가 HTML Form을 통해 보낸 값이 DB의 데이터 형식과 일치하는지를 확인해야 한다. 
    - 통과: DB에 저장
    - 실패: 에러메세지 + 입력값을 사용자에게 리턴

- Model을 통해 Form class를 만들 수 있는 helper class이다. 

- ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용한다.

- 생성

  ```python
  ## articles/forms.py
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
    	class Meta:
        	model = Article
        	fields = "__all__"
       	 	## fields = ['title', 'content',]
        	## exclude = ('title',)
  ```

- ModelForm 객체를 context로 전달

  ```python
  from .forms import ArticleForm
  
  def new(request):
      form = ArticleForm()
      context ={
          'form' : form,
      }
      return render(request, 'articles/new.html', context)
  ```


- html에서 사용법. 

  ```html
  <!-- articles/new.html -->
  
  <form action = "~~" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
  </form>
  
  <!-- 출력 옵션 3가지. (label과 input 쌍)
  as_p
  as_ul - 각 필드가 li 태그로 감싸져서 렌더링. ul 태그는 직접 작성해야 함. 
  as_table - 각 필드가 tr 태그로 감싸져서 렌더링
  -->
  ```

- is_valid(), save()

  ```python
  ## views.py
  
  def create(request):
  	form = ArticleForm(request.POST)
  	if form.is_valid():
  		article = form.save()
  		return redirect('articles:detail', article.pk)
  	return redirect('articles:new')
  
  ## is_valid(): 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
  ## save(): form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 DB에 저장. ModelForm의 하위 클래스는 키워드 인자 instance가 제공되지 않으면 save()는 지정된 모델의 새 인스턴스를 만들고, instance가 제공되면 해당 인스턴스를 수정한다. 
  ```

- errors

  ```python
  ## is_valid()의 반환 값이 False인 경우 ModelForm 인스턴스의 errors 속성에 값이 작성되는데, 유효성 검증을 실패한 원인이 딕셔너리 형태로 저장된다. 
  ```

- 로직

- 