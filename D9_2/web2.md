## CSS 기본 스타일

## > 크기 단위

- px

  - 모니터 해상도의 한 화소인 '픽셀' 기준

  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위

- %
  - 백분율 단위
  - 가변적인 레이아웃에서 주로 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  - html의 기본 font-size : 16px

- viewport
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax

## > 색상 단위

- 색상 키워드
  - 대소문자를 구분하지 않음
  - red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상
  - '#' + 16진수 표기법
  - rgb() 함수형 표기법
- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
- +a : 투명도
  - ex) rgba, hsla

## > 문서 표현

- 텍스트
  - 서체(font-family), 서체 스타일(font-style, font-weight 등)
  - 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height)
- 컬러, 배경(background-image, background-color)
- 기타 HTML 태그별 스타일링
  - 목록(li)
  - 표(table) 등

## CSS 선택자

- 선택자 유형

  - 기본 선택자
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자
  - 결합자(combinators)
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자

  - 의사 클래스/요소(Pseudo Class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

- CSS 적용 우선순위(cascading order)

  1. !important : 이거 사용하면 전체 코드의 우선순위가 망가질 수 있다고 한다. 

     > 그러면 어떨 때 사용하는 걸까? 외부 라이브러리에서 사용한다고 한다. 

  2. 우선순위(Specificity)

     - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element

  3. CSS 파일 로딩 순서

- CSS 상속

  - 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  - 상속되는 것 : Text 관련 요소(font, color, text-align), opacity, visibility 등
  - 상속되지 않는 것 : Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), positon 관련 요소(position, top/right/bottom/left, z-index) 등

  ```html
  <style>
    p {
      color: red;
      /* 상속됨 */
      border: 3px solid black;
      /* 상속 안됨 */
    }
    span {
    }
  </style>
  
  <body>
    <p>
      안녕하세요 <span>테스트!</span>입니다.
    </p>
  </body>
  <!-- /* 확인해봐 */ -->
  ```

## CSS Box model

**CSS 원칙 1. 모든 요소는 박스 모델(네모)이고, 위에서부터 아래로, 왼족에서 오른쪽으로 쌓인다. **

- 모든 HTML 요소는 box 형태로 되어 있다.

- 하나의 박스는 네 부분으로 이루어진다. 

  - margin, border, padding, content

  ![스크린샷 2022-08-30 오후 2.04.36](web2.assets/스크린샷 2022-08-30 오후 2.04.36.png)

  ```html
  .margin-1{
  margin:10px;
  }
  <!-- ... -->
  .margin-4{
  margin: 10px 20px 30px 40px;
  }
  <!-- 시계방향이고 지정 안하면 맞은편과 같다. -->
  .border{
  border-width: 2px;
  border-style: dashed;
  border-color: black;
  }
  ```

  ```html
  <style>
      }
      .box{
        margin: 10px;
        border: 1px solid black;
        padding: 20px;
        /*color :bisque;*/
        background-color: bisque;
  
      }
  </style>
  ```

- box-sizing

  - 기본적으로 모든 요소의 box-sizing은 content-box
    - padding을 제외한 순수 contents 영역만을 box로 지정한다. 
  - border를 포함한 사이즈를 원하면 box-sizing을 border-box로 설정하면 된다. 

## CSS Display

**CSS 원칙 2. display에 따라 크기와 배치가 달라진다.**

- display : block

  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다. (block의 기본 너비는 가질 수 있는 너비의 100%)
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

  ```html
  margin-left: auto;
  <!-- 가장 오른쪽으로 붙는다. -->
  text-align : center;
  <!-- text 정렬 -->
  ```

  

- display : inline

  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다. 
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다. 

- block, inline 요소 구분

  - block : div / ul, ol, li / p / hr / form 등
  - inline : span/ a / img / input, label / b, em, i, strong 등

- display : inline-block

  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline 처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음

- display : none

  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility : hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다. 
  - https://developer.mozilla.org/ko/docs/Web/CSS/display



---

강의자료