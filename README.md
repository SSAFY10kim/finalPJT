# Simplify

## 개발기간

2023.11.16(목) ~ 2023.11.24(금)

## 팀원

| 이름   | 담당 영역                                                    |
| ------ | ------------------------------------------------------------ |
| 김동영 | ERD , 메인페이지, 회원 커스터 마이징, 환율 계산기, 근처 은행 검색, 커뮤니티, 프로필 페이지, CSS |
| 이장하 | 예적금 금리 비교, 금융 상품 추천 알고리즘, README            |

## 요약

금융 지식이 부족한 유저도 쉽게 사용할 수 있는 간편한 애플리케이션 제작

## 목표

## 계획

|                    | Front-End                                                    | Back-End                                                     |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 메인 페이지        | 레이아웃 및 디자인                                           |                                                              |
| 예적금 금리 비교   | axios 활용하여 금융 상품 정보 받아오기<br /> 상품 상세 정보 화면 구현<br /> 관심상품 등록 기능 구현 | API를 이용한 금융 상품 정보 DB 저장<br /> 관심 상품 좋아요 기능 |
| 환율 계산기        | axios를 활용하여 보내 환율 정보 받아오기<br /> 환율 계산기 기능 구현 | API를 이용한 환율 정보 받아서 front로 넘기기                 |
| 지도               | API를 활용하여 Kakao 맵 화면 구현<br /> 키워드에 맞는 검색 결과 구현 |                                                              |
| 상품 추천 알고리즘 |                                                              |                                                              |
| 게시판             |                                                              |                                                              |
| 회원 커스터 마이징 |                                                              |                                                              |
| 프로필             |                                                              |                                                              |
| 금융 상식          |                                                              |                                                              |



## 필수 요구사항

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

## 기능목록

- 메인 페이지
- 예적금 금리 비교
- 환율 계산기
- 근처 은행 찾기
- 금융 상식
- 게시판
- 프로필

## 기술스택

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

## API

<p align="center">   
    <img src="https://img.shields.io/badge/Kakao_Map-yellow?style=flat&logo=kakao&logoColor=white">    
    <img src="https://img.shields.io/badge/한국수출입은행-darkblue?style=flat">   <img src="https://img.shields.io/badge/금융감독원-skyblue?style=flat">   
    <img src="https://img.shields.io/badge/NAVER-lightgreen?style=flat&logo=naver">
</p>

## 아키텍쳐

![diagrams.drawio](assets\diagrams.drawio.png)

## 데이터베이스 모델링(ERD)

![Simplify_ERD](assets\Simplify_ERD.png)



## 컴포넌트 구조

![컴포넌트](assets\컴포넌트.png)



## 개발일지

![image](assets\image.png)



## 참고페이지

[GPT]: https://chat.openai.com/
[마이뱅크]: https://www.mibank.me/
[뱅크샐러드]: https://www.banksalad.com/
[bootstrapDoc]: https://getbootstrap.com/



