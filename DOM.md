## 웹 브라우저

HTML 문서와 그림, 멀티미디어 파일 등 월드와이드웹을 기반으로 한 인터넷의 컨텐츠를 검색 및 열람하기 위한 응용 프로그램의 총칭이다. 



## 하는 일

1. DOM 조작
2. BOM 조작
3. JavaScript Core(ECMAScript)



## DOM(Document Object Model)

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스이다. 

- 문서를 구조화하고, 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델이다. 

- 단순한 속성 접근, 메서드 활용 뿐만이 아니라 프로그래밍 언어적 특성을 활용한 조작이 가능하다. 

- 주요 객체

  - window : DOM을 표현하는 창이다. 가장 최상위 객체이다.
  - document : 페이지 컨텐츠의 Entry Point 역할을 하며, \<body> 등과 같은 수많은 다른 요소들을 포함한다. 
  - navigator, location, history, screen

- DOM 객체의 상속 구조

  ![dom_상속](브라우저.assets/dom_상속.png)

  → 모든 노드 객체는 `Object` > `EventTarget` > `Node`를 상속받음

  - **문서 노드 `Document`**
    - DOM트리의 최상단에 있는 **루트 노드**, 하나의 HTML문서 당 **하나**
    - 아래 서술될 노드들이 모두 이 문서 노드의 자식 노드 이므로 접근을 위해서는 이 문서 노드를 꼭 거쳐야 함
    - 브라우저 상 전역객체인 window의 document 프로퍼티에 바인딩 되어있어
      `window.(생략가능)document`로 참조
  - **요소 노드 `Element`**
    - 문서의 구조 표현
      ![55285bb6-353e-4d1b-a8ab-cea4628a2034](브라우저.assets/55285bb6-353e-4d1b-a8ab-cea4628a2034.png)
  - **어트리뷰트 노드 `Attr`**
    - HTML 요소의 어트리뷰트 정보들을 포함하고 있는 객체
    - 해당 요소 노드에 연결 되어있음
      따라서 어트리뷰트 노드에 접근하려면 먼저 요소 노드 접근이 필수적
  - **텍스트 노드 `CharacterData`**
    - HTML 요소의 텍스트 컨텐츠를 가리키는 객체
    - 자식노드 없음, **리프 노드**
    - 공백 텍스트 노드
      - HTML요소 사이의 공백문자` \n\r\t` 들에 의해 생성
      - 특별한 역할을 하진 않지만 노드 탐색시 주의해야함

#### DOM 선택

- DOM 선택 - 선택 관련 메서드(1/2) [(link)](https://developer.mozilla.org/ko/docs/Web/API/Document#methods)

  - ```javascript
    document.querySelector(selector)
    ```

    - 제공한 선택자와 일치하는 element 하나 선택
    - selector 를 만족하는 첫 번째 element 객체를 반환 (없다면 null)

  - ```javascript
    document.querySelectorAll(selector)
    ```

    - 제공한 선택자와 일치하는 여러 element 를 선택
    - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 selector 를 인자(문자열)로 받음
    - 지정된 셀렉터에 일치하는 NodeList 를 반환

- DOM 선택 - 선택 관련 매서드(2/2) [(link)](https://developer.mozilla.org/ko/docs/Web/API/Document#methods)
  - `getElementById(id)`
  - `getElementsByTagName(name)`
  - `getElementsByClassName(names)` <br><br>
- DOM 선택 - HTMLCollection & NodeList
  - 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열)
  - HTMLCollection
    - name, id, index 속성으로 각 항목에 접근 가능
  - NodeList
    - index로만 각 항목에 접근 가능
    - 단, HTMLCollection 과 달리 배열에서 사용하는 `forEach` 메서드 및 다양한 메서드 사용
  - 둘 다 Live Collection 으로 DOM의 변경사항을 실시간으로 반영하지만, `querySelectorAll()` 으로 반환되는 NodeList는 Static Collection으로 실시간 반영되지 않음

## BOM(Browser Object Model)

- 자바스크립트가 브라우저와 소통하기 위한 모델이다. 
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 한다.
  - 버튼, URL 입력 창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능하다. 

 <img src="브라우저.assets/스크린샷 2022-09-19 오후 2.11.58.png" alt="스크린샷 2022-09-19 오후 2.11.58" style="zoom:50%;" />

---

강의자료

https://velog.io/@zmin9/JavaScript-DOM%EA%B3%BC-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8