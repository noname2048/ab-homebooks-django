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



## 개발환경

4가지 stage 로 나누어 구분합니다.

1. develope statge
   모든 통신과 설정은 개발자 컴퓨터 내부에서 일어납니다. docker-compose를 통해 구성합니다.
2. intermediate stage
   벡엔드 서버를 제외한 database와 cache와 같은 자원을 외부환경에서 사용합니다.
3. product stage
   실제 클라우드에서 immutable 객체로 띄워지는 서버에 대한 설정값을 가집니다.

각 단계에 대한 설정값은 homebooks/homebooks/settings 에 저장합니다.



## 클라우드 계획

5.28 일까지 MS Azure 프리티어가 있기 때문에 최대환 이를 활용할 계획입니다.

