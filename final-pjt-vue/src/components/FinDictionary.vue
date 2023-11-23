<template>
    <!-- <div class="card-container">
      <b-card
        title="예금"
        tag="article"
      >
        <b-card-text>
          통장에 돈을 넣어놓고 '정해진 기간 동안 찾지 않는 예금'. 찾을 경우 이자를 손해봄. 쉽게 말하면 목돈을 넣어 놓고 매달 돈을 타 먹는 통장
        </b-card-text>
      </b-card>
      <b-card
        title="적금"
        tag="article"
      >
        <b-card-text>
          매월 약속한 날짜에 꼬박꼬박 돈을 넣어서 목돈을 만들 때 이용하는 통장. 
        </b-card-text>
      </b-card>
      <b-card
        title="단리: "
        tag="article"
      >
        <b-card-text>
          원금에만 이자가 붙어요
        </b-card-text>
      </b-card>
      <b-card
        title="복리"
        tag="article"
      >
        <b-card-text>
          이자에도 이자가 붙어요
        </b-card-text>
      </b-card>
    </div> -->
    <div class="container">
      <div class="card">
        <div class="card-title">예금</div>
        <div class="card-text">통장에 돈을 넣어놓고 '정해진 기간 동안 찾지 않는 예금'. 찾을 경우 이자를 손해봄. 쉽게 말하면 목돈을 넣어 놓고 매달 돈을 타 먹는 통장</div>
      </div>
      <div class="card">
        <div class="card-title">적금</div>
        <div class="card-text">매월 약속한 날짜에 꼬박꼬박 돈을 넣어서 목돈을 만들 때 이용하는 통장</div>
      </div>
      <div class="card">
        <div class="card-title">단리</div>
        <div class="card-text">원금에만 이자가 붙어요</div>
      </div>
      <div class="card">
        <div class="card-title">복리</div>
        <div class="card-text">이자에도 이자가 붙어요</div>
      </div>
      <div class="card">
        <div class="card-title">정액적립</div>
        <div class="card-text">계약기간 동안 정해진 일자, 정해진 금액을 납입하는 방식</div>
      </div>
      <div class="card">
        <div class="card-title">자유적립</div>
        <div class="card-text">일정한 기간을 정하고 금액 및 횟수에 제한없이 자유롭게 납입하여 기간 만료시 이자를 계산하여 원금과 함께 지급하는 상품입니다</div>
      </div>
      <div class="card">
        <div class="card-title">이자</div>
        <div class="card-text">이자란 ‘돈을 빌려 준 사람에게 건네는 감사의 마음’을 뜻합니다. 예를 들어 친구에게 100만원을 빌리고, 1년 뒤 감사의 마음 10만원을 합쳐서 총 110만원을 갚았다고 합시다. 이자란 바로 이 때 전한 감사의 마음 10만원을 말합니다</div>
      </div>
      <div class="card">
        <div class="card-title">금리</div>
        <div class="card-text">이자가 차지하는 비율. 예)원금 10000원에 이자1000원을 받는다면 금리는 10% (이자율 = 금리, 단 금리는 돈을 거래 할 때만 사용)</div>
      </div>
      <div class="card">
        <div class="card-title">우대금리</div>
        <div class="card-text">우대조건을 만족할때 적용되는 금리</div>
      </div>
      <div class="card">
        <div class="card-title">세후이자</div>
        <div class="card-text">일반 과세의 경우는 이자금액의 연 15.4% (이자소득 14% + 주민세 1.4%)가 징수됩니다</div>
      </div>
      <div class="card">
        <div class="card-title">매매기준율</div>
        <div class="card-text">매매기준율은 일종의 ‘원가’나 ‘도매가격’에 해당합니다. 예를 들어 매매기준율이 ‘1달러= 1,000원’이라면 은행이 1달러를 구해온 원가가 1,000원이었다는 이야기입니다</div>
      </div>
      <div class="card">
        <div class="card-title">환율</div>
        <div class="card-text">외국 돈과 우리 돈의 교환 비율. 환율이 100원 내렸다는 것은 정치·경제·사회·문화를 모두 고려한 대한민국의 국력이 100원어치만큼 강해졌다는 이야기이기 때문입니다</div>
      </div>
      <div class="card">
        <div class="card-title">외국통화표시법</div>
        <div class="card-text">외국통화표시법은 환율을 ‘1달러=1,000원’으로 표시하는 게 아니라 ‘1원=0.001달러’로 표시하는 방법입니다. 우리 돈 하나를 사기 위해서 외국 돈이 얼마나 필요한가를 표시해주는 방법이죠</div>
      </div>
      <div class="card">
        <div class="card-title">확정금리형상품</div>
        <div class="card-text">확정금리형 상품은 예금을 할 때 금리가 확정되고, 외계인이 처들어 오지 않는 이상 원금을 보장해주는 금융상품을 가리키는 말입니다. 대체로 ‘00예금, 00적금, 00저축’이라는 말이 붙어 있으면 확정금리형 상품입니다</div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { RouterLink, RouterView } from 'vue-router'
  </script>
  
  <style scoped>

  /* .card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  article {
    max-width: 25%;
    margin: auto;
    padding: auto;
  } */
  
.container {
    display: flex;
    justify-content: center;
    margin-top: 50px;
}
.card {
    border: 1px solid #000;
    margin: 0 5%;
    padding: 20px;
    flex-basis: 50%; /* 카드의 기본 너비, 필요에 따라 조정 */
}
.card-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}
.card-text {
    font-size: 16px;
}
  </style>