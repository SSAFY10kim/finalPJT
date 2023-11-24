![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,2,3&height=250&section=header&text=Simplify&animation=fadeIn&fontColor=d6ace6&fontSize=90)

> ## :alarm_clock: 개발기간

2023.11.16(목) ~ 2023.11.24(금)

> ## 🤝 팀원

| 이름   | 담당 영역                                                    |
| ------ | ------------------------------------------------------------ |
| 김동영 | ERD , 메인페이지, 회원 커스터 마이징, 환율 계산기, 근처 은행 검색, 커뮤니티, 프로필 페이지, CSS |
| 이장하 | 예적금 금리 비교, 금융 상품 추천 알고리즘, README            |

> ## :page_facing_up: 요약

금융 지식이 부족한 유저도 쉽게 사용할 수 있는 간편한 애플리케이션 제작

> ## :dart: 목표

- 금융상품 데이터 기반 예금 및 적금 금리 비교 서비스 구성
- 금융 상품 추천 알고리즘 구성
- 환율 정보 API를 활용한 환율 계산 서비스 구성
- 지도 API를 활용한 은행 검색 서비스 구성
- 커뮤니티 서비스 구성
- 서비스 관리 및 유지보수 목표

> ## :pencil2: 계획

|                    | Front-End                                                    | Back-End                                                     |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 메인 페이지        | 레이아웃 및 디자인                                           |                                                              |
| 예적금 금리 비교   | axios 활용하여 금융 상품 정보 받아오기<br /> 상품 상세 정보 화면 구현<br /> 관심상품 등록 기능 구현 | API를 이용한 금융 상품 정보 DB 저장<br /> 관심 상품 좋아요 기능 |
| 환율 계산기        | axios를 활용하여 보내 환율 정보 받아오기<br /> 환율 계산기 기능 구현 | API를 이용한 환율 정보 받아서 front로 넘기기                 |
| 지도               | API를 활용하여 Kakao 맵 화면 구현<br /> 키워드에 맞는 검색 결과 구현 |                                                              |
| 상품 추천 알고리즘 | 유저 금융 정보를 Back-End로 전송                             | K-means 클러스터링 알고리즘을 사용한<br />개인 맞춤 상품 추천 알고리즘 구현 |
| 게시판             | 게시글 작성 및 수정 삭제<br />댓글 작성 및 삭제 구현         | DB에 게시글 및 댓글 정보 저장                                |
| 회원 커스터 마이징 | 회원가입 및 유저 정보 입력 페이지<br />유저 금융 정보 입력   | 회원가입 Serializer 수정 및<br />유저 정보 DB 저장           |
| 프로필             | 개인 상세 프로필 및 관심 상품<br />알고리즘 추천 상품        | 상품 추천 알고리즘을 통한 추천 상품과<br />개인별 상세 정보 DB에서 넘겨줌 |
| 금융 상식          | axios를 통해 네이버 뉴스와<br />금융 상식에 대한 정보 작성   | 네이버 API를 이용해 뉴스를 <br />front로 넘김                |



> ## :white_check_mark: 필수 요구사항

1. 메인페이지
2. 회원 커스터마이징
   - 필수 필드 : 유저이름, 이메일, 가입한 상품 목록
3. 예적금 금리 비교 - 데이터 저장
   - 데이터 DB에 저장, 이미 존재하는 데이터는 새로 저장하지 않도록 구성
4. 환율 계산기
   - 국가 선택 기능
5. 근처 은행 검색
   - 위치와 은행을 선택할 수 있도록
6. 커뮤니티(게시판)
   - CRUD 필수
7. 프로필 페이지
   - 금융 상품 추천 알고리즘
8. README
   1. 팀원 정보 및 업무 분담 내역 
   2. 설계 내용(아키텍처 등) 및 실제 구현 정도
   3. 데이터베이스 모델링(ERD)
   4. 금융 상품 추천 알고리즘에 대한 기술적 설명
   5. 서비스 대표 기능들에 대한 설명
   6. 기타(느낀 점, 후기 등)

> ## :page_with_curl: 기능목록

- 메인 페이지
- 예적금 금리 비교
- 환율 계산기
- 근처 은행 찾기
- 금융 상식
- 게시판
- 프로필

> ## :books: 기술스택

<div align=center><h1>📚 STACKS</h1></div>
<div align=center>
    <img src="https://img.shields.io/badge/windows 10-0078D6?style=for-the-badge&logo=windows 10&logoColor=white">
    <img src="https://img.shields.io/badge/windows 11-0078D4?style=for-the-badge&logo=windows 11&logoColor=white">
    <br>
	<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css 3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
    <br>
    <img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white">
    <img src="https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white">
    <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
    <br>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
    <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
    <br>
    <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
    <br> 
</div>

> ## :link: API

<p align="center">   
    <img src="https://img.shields.io/badge/Kakao_Map-yellow?style=flat&logo=kakao&logoColor=white">    
    <img src="https://img.shields.io/badge/한국수출입은행-darkblue?style=flat">   <img src="https://img.shields.io/badge/금융감독원-skyblue?style=flat">   
    <img src="https://img.shields.io/badge/NAVER-lightgreen?style=flat&logo=naver">
</p>

> ## :black_circle: 아키텍쳐
![diagrams.drawio](assets/diagrams.drawio.png)

> ## :white_circle: 데이터베이스 모델링(ERD)

![Simplify_ERD](assets/Simplify_ERD.png)

> ## :red_circle: 컴포넌트 구조

![컴포넌트](assets/컴포넌트.png)

> ## :closed_book: 개발일지

![image](assets/image.png)

> ## :soccer: 금융 상품 추천 알고리즘 기술적 설명
- K-Means Clustering은 각 데이터 포인트가 가장 가까운 평균 또는 중심을 따르는 k 개의 서로 다른 군집으로 데이터 집합을 분할하는 데 사용되는 방법입니다. 주어진 데이터 공간에서 데이터 포인트의 유사성을 찾아 그룹화하는 것입니다.
- K-Means Clustering은 먼저 무작위로 K 개의 중심을 초기화합니다. 그런 다음 각 데이터 포인트를 유클리드 거리와 같은 거리 측정 기준을 기반으로 가장 가까운 중심에 할당합니다. 중심이 재계산되고 이러한 과정이 중심이 더 이상 크게 변하지 않을 때까지 반복됩니다. 또는 미리 정의된 조건이 충족될 때까지 계속됩니다.
- PCA기법을 사용하여 target을 분류할 때 몇개의 변수로 분류할 수 있는지 결론적으로 PCA의 본질은 차원 축소이다. 차원이 축소됐다는 것은 원본 데이터가 아니라 변환(projection) 된 데이터 == 주성분을 이용해 분석 혹은 모델링을 진행하겠다는 것이다. 
- K-means 클러스터링 k 결정
  - Elbow Method : 각 데이터들의 군집 중심과의 평균 거리, 학습 시간을 지표로 k 값을 계산해 줍니다.
  - 실루엣 계수 : 개별 데이터가 할당된 군집 내 데이터와 얼마나 가깝게 군집화 되어있는지, 그리고 다른 군집에 있는 데이터와는 얼마나 멀리 분리되어 있는지를 수치로 나타냅니다.

> ## :memo: 프로젝트 후기

> ## :rainbow: 참고페이지
[GPT]: https://chat.openai.com/
[마이뱅크]: https://www.mibank.me/
[뱅크샐러드]: https://www.banksalad.com/
[bootstrapDoc]: https://getbootstrap.com/
