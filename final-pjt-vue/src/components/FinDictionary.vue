<template>
  <div class="dictionarypage text-center">
    <h1><i class="bi bi-book"></i> 금융 사전</h1>
    <div class="row justify-content-center" style="margin: 30px auto">
      <div class="col-sm-7">
        <div id="cardCarousel" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div v-for="(card, index) in cards" :key="index" :class="{ 'carousel-item': true, 'active': index === 0 }">
              <div class="card h-100">
                <h5 class="card-header">{{ card.title }}</h5>
                <div class="card-body">
                  <!-- <p class="card-text">{{ card.description }}</p> -->
                  <p class="card-text" v-html="card.description.replace(/\n/g, '<br>')"></p>
                </div>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#cardCarousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#cardCarousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
    <div class="description text-center">
      <h2><i class="bi bi-question-circle-fill"></i> 왜 금융 용어를 알아야 하나요?</h2>
      <p v-html="description.replace(/\n/g, '<br>')"></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const cards = ref([
  { title: '예금', description: "통장에 돈을 넣어놓고 '정해진 기간 동안 찾지 않는 예금'.<br> 찾을 경우 이자를 손해봄.<br> 쉽게 말하면 목돈을 넣어 놓고 매달 돈을 타 먹는 통장" },
  { title: '적금', description: '매월 약속한 날짜에 꼬박꼬박 돈을 넣어서<br> 목돈을 만들 때 이용하는 통장' },
  { title: '단리', description: '원금에만 이자가 붙어요.<br> 단리는 이자가 계산되는 기간에 원금만 고려하고,<br> 그 외 이자가 계산되는 기간에 대한 고려가 없습니다.' },
  { title: '복리', description: '이자에도 이자가 붙어요.<br> 복리는 이자가 계산되는 기간에 원금과 누적된 이자가 함께 고려됩니다.' },
  { title: '정액적립', description: '계약기간 동안 정해진 일자, 정해진 금액을 납입하는 방식.<br> 매월 또는 정기적으로 일정한 금액을 저축하는 방법 중 하나입니다.' },
  { title: '이자', description: "이자란 ‘돈을 빌려 준 사람에게 건네는 감사의 마음’을 뜻합니다.<br> 예를 들어 친구에게 100만원을 빌리고,<br> 1년 뒤 감사의 마음 10만원을 합쳐서 총 110만원을 갚았다고 합시다.<br> 이자란 바로 이 때 전한 감사의 마음 10만원을 말합니다." },
  { title: '금리', description: '이자가 차지하는 비율.<br> 예) 원금 10,000원에 이자 1,000원을 받는다면 금리는 10%<br> (이자율 = 금리, 단 금리는 돈을 거래 할 때만 사용)' },
  { title: '우대금리', description: '우대조건을 만족할 때 적용되는 금리' },
  { title: '세후이자', description: '일반 과세의 경우 이자금액의<br> 연 15.4% (이자소득 14% + 주민세 1.4%)가 징수됩니다.' },
  { title: '매매기준율', description: '매매기준율은 일종의 ‘원가’나 ‘도매가격’에 해당합니다.<br> 예를 들어 매매기준율이 ‘1달러= 1,000원’이라면<br> 은행이 1달러를 구해온 원가가 1,000원이었다는 이야기입니다.' },
  { title: '환율', description: '외국 돈과 우리 돈의 교환 비율.<br> 환율이 100원 내렸다는 것은 정치·경제·사회·문화를 모두 고려한<br> 대한민국의 국력이 100원어치만큼 강해졌다는 이야기이기 때문입니다.' },
  { title: '외국통화표시법', description: '외국통화표시법은 환율을 ‘1달러=1,000원’으로 표시하는 게 아니라<br> ‘1원=0.001달러’로 표시하는 방법입니다. <br>우리 돈 하나를 사기 위해서 외국 돈이 얼마나 필요한가를 표시해주는 방법이죠.' },
  { title: '확정금리형상품', description: '확정금리형 상품은 예금을 할 때 금리가 확정되고,<br> 외계인이 처들어 오지 않는 이상 원금을 보장해주는 금융상품을 가리키는 말입니다.<br> 대체로 ‘00예금, 00적금, 00저축’이라는 말이 붙어 있으면 확정금리형 상품입니다.' },
  // Add more cards as needed
]);

const description = '금융 용어를 이해하는 것은 개인 재무 건강을 책임지고 지속적인 경제 발전을 위해 중요합니다.<br> 용어 이해는 금융 거래 및 투자 시 착오를 줄이고, 효율적인 예산 및 저축 습관을 형성하는 데 도움이 됩니다.<br> 또한 금융 뉴스와 대화에 능숙하면 개인 및 사회 경제 동향을 파악하고 미래를 대비할 수 있습니다.<br> 이는 안정된 경제 기반을 쌓아 나가는데 도움이 되며, 개인과 사회가 금융적 독립성을 확보하는 핵심입니다.'
</script>

<style scoped>
.dictionarypage {
  width: 85%;
  margin: 0 auto;
  column-gap: 30px;
}

/* 위아래 간격 조절을 위한 스타일 */

/* 카드의 높이를 100%로 설정하여 세로 길이를 일정하게 유지 */
.h-100 {
  height: 100%;
}
</style>