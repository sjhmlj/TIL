## table

- table의 각 영역을 명시하기 위해 \<thead>, \<tbody>, \<tfoot> 요소를 사용한다. ![스크린샷 2022-09-05 오후 1.32.25](web6.assets/스크린샷 2022-09-05 오후 1.32.25.png)
- 각 row는 \<tr>로 구성하고 내부는 \<th>와 \<td>로 셀을 구성한다. 
- 위의 그림처럼 '2명' 셀은 2개의 칸을 차지한다. 이런 경우 colspan, rowspan을 사용한다. 
- caption은 표를 설명하거나 제목을 나타낸다. 

```html
<table>
    <thead>
    	<th>ID</th>
        <th>Name</th>
        <th>Major</th>
    </thead>
    <tbody>
    	<tr>
        	<td>1</td>
            <td>홍길동</td>
            <td>Computer Science</td>
        </tr>
        ...
    </tbody>
    <tfoot>
    	<tr>
        	<td>총계</td>
            <td colspan="2">2명</td>
        </tr>
    </tfoot>
    <caption>1반 학생 명단</caption>
</table>  
```

## form

- \<form>은 데이터를 서버에 전달하기 위해 사용되는 태그이다. 
- 속성
  - action: form을 처리할 서버의 url
  - method: form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
  - enctype: method가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded: 기본값
    - multipart/form-data: 파일 전송시 (input type이 file인 경우)

## input : 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공된다.

- 속성
  - name: form control에 적용되는 이름(이름/값 페어로 전송됨)
  - value: form control에 적용되는 값
  - required, readonly, autofocus, autocomplete, disabled 등

```html
<form action="/search">
    <input type="text" name="q">
    
</form>
```

- input label
  - label을 클릭하여 input 에 초점을 맞추거나 활성화시킬 수 있다. 
    - 사용자는 선택할 수 있는 영역이 늘어나서 편하게 사용할 수 있다. 
    - label과 input 입력의 관계가 시작적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 한다. 
  - \<input>에 id 속성을, \<label>에는 for 속성을 활용하여 상호 연관을 시킨다. 

```html
<body>
  <h1>form 실습</h1>
  <form action="/search">
    <div>
      <label for="userid">아이디</label>
    </div>
    <input type="text" name="userid">
    <div>
      <label for="password">비밀번호</label>
    </div>
    <input type="password" name="password">
    <div>
      <input type="submit" name="제출">
    </div>
  </form>
</body>
```

- input type
  - text, password, email, number, file,  등
  - checkbox, radio - 일반적으로 label 태그와 함께 사용한다. name, value를 지정해야 한다. 
  - color, date, hidden 등

## Bootstrap

- front-end open source
- css class를 그냥 갖다 쓰면 된다.

```html
<div class="mt-3 ms-5">bootstrap-spacing</div> 
```

[bootstrap docs](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

- 여기에 많은 정보가 있다. 필요하면 보고 써. 

