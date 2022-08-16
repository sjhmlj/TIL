# git_push,ignore,keep



## Remote Repository(원격저장소)

: 네트워크를 활용한 저장소. Ex) GitHub, GitLab, Bitbucket`

- RR도 버전(커밋)을 관리한다. 

- 명령어
  - push : local repository  -> remote repository
  - pull :   RR -> LR

- push 단계

  1. Github에서 new repository(RR) 만들기.

  2. 터미널에서 RR 정보를 추가  :    git remote add 'RR 이름 ex)origin' 'url'
  	RR 정보를 삭제할 때는  git remote rm 'RR 이름'

  3. RR의 정보 확인  :   $ git remote -v      ![](D3_git_push.assets/스크린샷 2022-07-06 오후 4.40.25.png)

  4. 커밋을 올려보자.   $ git push 'RR 이름 ex) origin' 'branch 이름 ex) master'

     이 과정에서 사용자 인증을 해야 한다. github의 ID와 Password 또는 Token을 발급받아 입력해서 진행한다. 

- push가 실패하는 경우
	- LR과 RR의 커밋 이력이 다른 경우 발생한다. 협업을 하면서 각각 커밋을 할 때를 예로 들 수 있다.   
	
	- 해결방법 : pull을 사용해서 RR의 커밋을 LR로 가져와서 병합하는 작업을 해야 한다. 이 때 추가 커밋이 발생한다. 
	
	- 커밋을 병합하는 작업은 branch와 관련이 있다고 한다.  
	
	  

## .gitkeep
- Git은 파일 단위로 보기 때문에 빈 폴더를 만들었다면 git이 반응하지 않는다. 만약 빈 폴더를 git에 올리고 싶다면 폴더 안에 touch. gitkeep을 한다. 이는 관용적인 작업이다. 



## .gitignore
- git은 폴더 내 파일의 수정이 일어날 때마다 추적을 한다. 이를 필요로 하지 않는 파일의 경우에 다음의 방법을 사용한다. 
- Git 저장소에 .gitinit 파일을 생성하고 예시로 다음과 같은 내용을 입력한다.
	- 특정 파일 :   a.txt(모든 a.txt), test/a.txt (test 폴더의 a.txt)
	- 특정 디렉토리 :  /secret
	- 특정 확장자 :  *.exe
	- 예외처리 :  !b.exe
- 이미 커밋된 파일은 삭제를 해야 .gitignore 에 적용될 수 있다.
- [gitignore.io](https://www.toptal.com/developers/gitignore/)

