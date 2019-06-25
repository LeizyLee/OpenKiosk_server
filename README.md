# OpenKiosk_server
- 본 프로젝트의 핵심이 되는 기능을 우선적으로 구현
+ 핵심 기능
  - Amazon API를 활용한 리뷰 분석
  - 리뷰에 대한 통계 도출(긍정,부정 평가)
  - 매출 통계
---
## 자바 환경변수
- JAVA_HOME 추가 = 설치 경로
- ex\) C:\Program Files\Java\jdk1.8.0_131
- Path 수정 = %JAVA_HOME%\bin
- CLASSPATH 추가 = %JAVA_HOME%\lib
---
## TomCat 설치 후 프로젝트 생성
- 톰캣 설치시 jre 필요
- 설치 후 Intellij에서 web 프로젝트 생성
![logo](https://i.kym-cdn.com/entries/icons/original/000/013/564/doge.jpg)

- 프로젝트 설정시 Tomcat 설치 위치 지정
- 프로젝트 이름을 설정하고 Finish  
---
### 2019-06-24
- 프로젝트 생성 및 Hello world 출력
![test](./readmeImg/helloworld.JPG)
### 2019-06-25
- 처음 실행하면 못보던 폴더인 out 폴더가 생성
- 이는 run하는 과정에서 war 파일이 풀어지면서 배포 가능한 형태로 생성되는 것
- 이는 Project Structure 에서 몇가지 옵션을 건들면 잡다하게 파일을 생성하는게 아닌 zip 파일 하나로 만들수도 있음  

![01](./readmeImg/Project_Structure.JPG)

![02](./readmeImg/Project_Structure_02.JPG)

![03](./readmeImg/war_zip.JPG)
