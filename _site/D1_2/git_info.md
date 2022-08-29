- 오전

  Git : 형상관리도구 / 프로젝트 버전관리 / 분산버전관리 시스템.

  git을 이용해서 github에 소스코드를 공유하고 관리할 수 있음.

  markdown : 2004년 존 그루버가 만든 텍스트 기반의 가벼운 마크업 언어(ex- HTML)

  [markdown_rule](./markdown_rule.md) 

- 오후

  - CLI : Command Line Interface.   < - > GUI : Graphic User Interface

    ​	CLI와 같은 인터페이스를 제공하는 프로그램을 명령 줄 해석기 또는 셸이라고 부른다. ex) bash, zsh

  - 프롬프트 기본 인터페이스 : 컴퓨터 정보, 디렉토리, $

  - 명령어

    ​	pwd(print working directory)

    ​	cd(change directory).    ‘.’ : 현재  ‘..’ : 상위

    ​	ls(list)

    ​	mkdir

    ​	touch

    ​	rm

    ​	rm -r  (뒤의 r은 recursive. 폴더를 삭제할 때 속의 파일을 삭제하기 위해 사용)

    

  - 버전 : 컴퓨터 소프트웨어의 특정 상태

  - Git :

    ​	코드의 버전을 관리하는 도구.

    ​	리눅스 커널을 위한 도구로 리누스 토르발스가 개발.

    ​	컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율.

  - 분산 버전 관리란?

    중앙집중식버전관리시스템은 중앙에서 버전을 관리하고 받아서 사용.

    분산버전관리시스템은 원격 저장소를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유.

    

  - 버전관리를 하는 이유 :

    ​	한 개의 파일로도 차이를 만들 수 있고, 수정 이유를 남길 수 있다. 현재 파일들을 안전한 상태로 과거 모습 그대로 복원도 가능하다.

    

  - git을 통한 버전관리

    

    ​	git init (로컬 저장소 만들기)	

    ​	git status

    ​	git log , git log -1, git log —oneline, git log -2 —oneline

    ​	git add ‘파일명’

    ​	git commit -m ‘커밋 메시지’

    ​	rm -rf .git으로 폴더 삭제할 수 있음(master 없어짐)

    

  - git 의 기본 흐름 :

    1. 작업하고 -Working directory
    2. add하여 staging area 모으고 -INDEX(staging area)
    3. commit으로 버전 기록 -HEAD

    

    ​	staging area는 내가 변경한 파일들을 각각 다른 버전으로 만들 수 있게 하는 도구임. 임시적인 공간.(저장하는 것은 아님)

    

    ​	commit :

    ​	staged 상태의 파일들을 커밋을 통해 버전으로 기록

    ​	SHA -1 해시를 사용하여 40자 길이의 체크섬을 생성하고, 이를 통해 고유한 커밋을 표기.

    ​	커밋 메시지는 변경 사항을 나타낼 수 있도록 명확하게 작성해야 함.

    

    ​	Git은 데이터를 파일 시스템의 스냅샷으로 관리하고 매우 크기가 작음.

    ​	파일이 달라지지 않으면 성능을 위해 파일을 새로 저장하지 않음

    ​	기존의 델타 기반 버전 관리시스템과 가장 큰 차이를 가짐.

    

  - git은 파일을 modified, staged, committed로 관리 (git 환경에서)

    ​	modified : 파일이 수정된 상태(add 명령을 통해 staging area로)

    ​	staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령을 통해 저장소로)

    ​	committed : 커밋이 된 상태	

    ​	unmodified : 커밋이 되었는데 수정되지 않은 상태.(committed과 동일한 듯)

    ​	untrackted : 한번도 커밋한 적인 없는 상태 (말 그대로 trackted된 적이 없음)

    

  - ‘head -> master는 해당 커밋이 master 브랜치의 마지막 커밋이라는 뜻입니다:)’

    

  - mac의 경우 git 폴더에서 (master)란 표시가 뜨게 할려면 vs Code를 이용해야 함. (구글링 해봐)