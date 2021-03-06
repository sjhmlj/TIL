# 프로젝트 02
- json은 텍스트다. 파이썬은 parsing을 통해 json을 파이썬의 객체에 맞게 변환하여 사용함
## API(Application Programming Interface)
#### 개념
- API는 정의 및 프로토콜 집합을 사용하여 두 소프트웨어 구성 요소가 서로 통신할 수 있게 하는 메커니즘이다. 
예를 들어 기상청의 소프트웨어 시스템에는 일일 기상 데이터가 들어 있다. 휴대폰의 날씨 앱은 API를 통해 이 시스템과 '대화'하고 휴대폰에 매일 최신 날씨 정보를 표시한다. 
- API의 맥락에서 application은 고유한 기능을 가진 모든 소프트웨어를 나타낸다. interfacesms 두 애플리케이션 간의 서비스 계약이라고 할 수 있다. 이 계약은 요청과 응답을 사용하여 두 애플리케이션이 서로 통신하는 방법을 정의한다. API 문서에는 개발자가 이러한 요청과 응답을 구성하는 방법에 대한 정보가 들어 있다(specification). 
- 작동
  - API 아키텍쳐는 일반적으로 클라이언트와 서버 측면에서 설명 된다. 요청을 보내는 애플리케이션을 클라이언트라고 하고 등답을 보내는 애플리케이션을 서버라고 한다. 
  - 작동 방식
    - SOAP API
    - RPC API
    - Websocket API
    - REST API


#### REST API (Representational State Transfer API)
- API는 기본적으로 '프로그래밍 인터페이스'인 만큼, API를 사용하는 것은 주로 프로그램 내부 단에서 이루어진다. 하지만 보다 다양한 분야에 쓰일 수 잏도록 '네트워크'와 '웹'에 맞춰진 API 통신 아키텍쳐가 등장했는데, 그게 바로 REST다. 
- 조건
  - Client-Server : 클라이언트와 서버로 분리되어야 하며 서로 의존성이 없어야 한다.
  - Stateless(무상태성) - 상태를 따로 저장하지 않으며, 이용자가 누구인지 혹은 어디서 접근하는지와 관계 없이 결과가 무조건 동일해야 한다. 따라서 REST API는 필연적으로 오픈될 수 밖에 없다.
  - Cache - HTTP를 비롯한 네트워크 프로토콜에서 제공하는 캐싱 기능을 적용할 수 있어야 한다. 
  - Uniform Onterface - 데이터가 표준 형식으로 전송될 수 있도록 구성 요소 간 통합 인터페이스를 사용한다. REST API 태반이 HTTP를 사용하기 때문에 HTTP 표준인 URL과 응답 코드, Request-Response Method 등을 사용한다.
  - Layered System - API는 REST 조건을 만족하면 필연적으로 오픈될 수밖에 없기 때문에, 요청된 정보를 검색하는데 있어 계층 구조로 분리되어야 한다. 
  - Self-descriptiveness - API를 통해 전송되는 내용은 별도 문서 없이 쉽게 이해될 수 있도록 자체 표현 구조를 지녀야 한다. 마찬가지로 웹 표준인 JSON과 XML이 절찬리에 사용중이다. 
- REST는 클라이언트가 서버 데이터에 액세스하는 데 사용할 수 있는 get, post, put, delete 등의 함수 집합을 정의한다. 클라이언트와 서버는 HTTP를 사용하여 데이터를 교환한다. 
- 프로그래밍에서 말하는 API와 비교를 해 보자. 둘 다 상호작용을 위한 인터페이스라는 점에서는 동일하다. 차이점은, REST API는 네트워크에서 '데이터'를 받아오기 위한 것이고 프로그램에서의 API는 '코드' 나아가 코드 뭉치인 라이브러리를 받아오는 것이다. 

---
출처
[아마존 ~~](https://aws.amazon.com/ko/what-is/api/)
[나무위키](https://namu.wiki/w/API)
강의 자료