```zsh
$ brew info sqlite
## echo 'export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"' >> ~/.zshrc 
## 이거 그대로 복붙
$ echo 'export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"' >> ~/.zshrc
$ echo &PATH
## 이거 하면 위의 /opt/homebrew/opt/sqlite/bin:$PATH 가 추가된 것을 볼 수 있음
## 근데 여기서 터미널 끄면 다시 초기화가 되서 
$ source ~/.zshrc	
## 새로고침(파일 실행)
```

- 시간 너무 오래 걸렸다. 좀 짜증났다. 

https://wnw1005.tistory.com/264 이거 안봤으면 못했을 듯. 

```zsh
$ echo 'export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"' >> ~/.zshrc
## 이 부분을 세번이나 반복하고 source 해서 
## 저게 3개나 들어가있다. 나중에 삭제하는 법 찾아봐야겠다.
```

- Mac에서 환경변수를 선언하는 방법에는 2가지가 있다.
  - [임시적 등록] Terminal 명령어
  - [영구 등록] zshrc / bashrc 에 직접 선언



#### vim 

- 모든 종류의 텍스트를 만들고 변경할 수 있도록 구성 가능한 텍스트 편집기이다.

- 대부분의 유닉스 시스템 및 apple os x에 'vi' 로 포함되어 있다. 	

- 네가지 모드

  - Normal mode : 기본모드이다. 다른 모드에서 ESC를 눌러 일반 모드로 돌아올 수 있다. 화살표 키 또는 h, j, k, l키를 이용하여 이동할 수 있다.
  - visual mode : 일반 모드와 유사하지만 텍스트 영역을 강조 표시하는 데 사용된다. 예를 들어 선택 영역을 이동하거나 편집하기 위해 강조 표시된 영역에서 일반 명령을 실행할 수 있다.
  - insert mode : 편집이 가능한 모드. 이 모드에서는 텍스트를 삽입하여 버퍼를 수정할 수 있다. 
  - Command-line : vim 창 하단에 단일 줄 입력을 지원한다. 명령이 완료되면 vim은 이전 모드로 돌아간다. 


```zsh
###MacOS 에서 vim을 이용하여 zsh 셸에서  환경 변수 설정하는 방법

$echo $SHELL
## 현재 사용중인 셸 확인
$vim ~/.zshrc
## vim 에디터 실행
$ i 
## <insert> 모드 진입
export PATH= ~~~~

## esc 눌러서 normal mode인 상태
:q   # 종료
:w   # 저장
:wq  # 저장 후 종료
:q!  # 저장하지 않고 종료
:wq! # 강제로 저장 후 종료

$source ~/.zshrc
## 업데이트 한 내용을 적용
```



---

https://wnw1005.tistory.com/264 

https://d-dual.tistory.com/8