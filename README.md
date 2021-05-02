# ab-homebooks-django
집에 있는 도서들의 정보를 저장하고 대출/반납을 관리하기 위한 벡엔드 django 구현 연습

## 사용스택
스택별로 나열하고 이유를 서술합니다
### 1. FRAMEWORK 

`django:3.2`를 사용. 

graphql 도입을 위해, 혹은 fastapi 서버를 사용하고 싶었는데, react 연습이 먼저라 restapi를 빠르게 구축하는 연습을 할겸, restframework 및 도합하여 django를 먼저 구현

### 2. IDE
`pycharm`을 사용.

vscode 가 제일 손에 익지만, 자동완성기능이 거의 없어서 pycharm을 써보려고 한다.

### 3. 가상환경

`pyenv` + `poetry`를 사용

pyenv는 activate 명령 없이도 추가적으로 쉘(zsh) 에서 자동적으로 바꿔준다. 이 점이 쉘을 많이 쓰는 입장에서 편리하였다.

poetry 는 추가적으로 npm이나 yarn 처럼 의존성을 관리하는 추가적인 파일을 생성하여 기존 pip 가 해결하지 못하는 의존성 문제를 해결하기 편리하다.

