## JavaScript란 무엇일까? 적용방법은? 

**javascript** : 웹에서 복잡한 동작을 수행하는 프로그래밍 언어이다. 클라이언트 사이드 언어이지만 Node.js를 통해 서버 사이드 에서도 사용할 수 있다.

```javascript
let randomNumber = Math.floor(Math.random() * 100) + 1;

const guesses = document.querySelector('.guesses');
const lastResult = document.querySelector('.lastResult');
const lowOrHi = document.querySelector('.lowOrHi');

const guessSubmit = document.querySelector('.guessSubmit');
const guessField = document.querySelector('.guessField');

let guessCount = 1;
let resetButton;
guessField.focus();
```

---

API는 javascript의 동작을 돕는다. 

- 브라우저 API는 
  - DOM API
  - Geolocation API
  - 오디오 API 등이 있다.
- javascript는 DOM API를 통해 html, css를 동적으로 수정하고, 사용자 인터페이스를 업데이트 하는 데에 가장 많이 쓰인다. 

---

javascript를 적용하는 방법을 보자

```html
1. 바디나 헤드에 script 태그를 만든다. 
<script>
 여기에 쓴다.
</script>

2. <script src="~~"></script> 외부에 js파일을 만들어 가져온다.

3. 인라인에서도 쓸 수 있지만 권장하지 않는다.
<button onclick="~~">
</button>
```

페이지의 모든 html은 순서대로 읽기 때문에 script의 위치에 따라 문제가 생길 수 있다. 

이에 대한 방법으로 script에 특성 defer, async를 추가하거나

```html
<script defer></script>     
<script async></script>
```

> defer와 async는 둘 다 script를 다운 받으면서 페이지 렌더링을 진행한다. 
>
> defer는 모든 콘텐츠를 불러온후 script를 실행하는 반면
>
> async는 script가 다운완료되면 바로 실행한다.  

고전적인 방법으로는 \</body> 바로 위에 script를 넣는 방법을 쓴다. --> 대형 사이트의 경우 느려진다.   



## 변수

```javascript
// 변수 선언
var name;

// 변수 초기화
name='seo';
```

데이터 타입 

- 숫자, 문자열, boolean, array, object

## 연산자

comparison operator

- === , !==
- 등

## 문자열

```javascript
var browserType = 'mozilla';

browserType.length;
// 7

browserType[0];
// m
browserType[browserType.length - 1];
// a

browserType.indexOf('zilla');
// 2
browserType.indexOf('vanilla');
// -1

browserType.slice(0, 3);
// moz

browserType.replace('moz', 'van');
// vanilla

var radData = 'My NaMe Is MuD';
radData.toLowerCase();
radData.toUpperCase();

var myString = '123';
var myNum = Number(myString);
myNum;
// 123
var myNum = 123;
var MyString = myNum.toString();
myString;
// '123'
```

## 배열

```javascript
var sequence = [1, 1, 2, 3, 5, 8, 13];

sequence.length;
// 7

var myData = 'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle';

var myArray = myData.split(',');
myArray;
// (6) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle']

var myNewString = myArray.join(',');
myNewString;
// 'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle'

var dogNames = ['Rocket','Flash','Bella','Slugger'];
dogNames.toString(); 
// 'Rocket,Flash,Bella,Slugger'

myArray.push('Cardiff');
myArray.pop();
myArray.unshift('Edinburgh');
myArray.shift();
// shift 는 왼쪽에서 작동. 네개 다 .length를 리턴
```

