<!-- <template>
  <div class="commonpage">
    <RouterLink :to="{name: 'common_news'}">경제 뉴스</RouterLink>
    <RouterLink :to="{name: 'common_card'}">카드 사용</RouterLink>
    <RouterLink :to="{name: 'common_dictionary'}">경제 사전</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router';
import NaverNews from '@/components/NaverNews.vue';

</script>

<style scoped>
.commonpage {
  width: 85%;
  margin: 0 auto;
}
</style> -->
<template>
  <div class="commonpage text-center">
    <h1><i class="bi bi-question-circle"></i> 금융 상식</h1>
    <p>
금융 상식은 개인의 재무 안정과 더불어 경제 이해를 높여 효과적인 금전 관리와 투자를 가능케하며, 미래에 대한 불확실성에 대비할 필요성이 있습니다.</p>
    <div class="card-container">
      <b-card
        title="경제 뉴스"
        img-src="data:image/png;base64,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"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 25rem;"
      >
        <b-card-text>
          <p v-html="description1.replace(/\n/g, '<br>')"></p>
        </b-card-text>

        <b-button>
          <RouterLink :to="{name: 'common_news'}">경제 뉴스</RouterLink>
        </b-button>
      </b-card>

      <b-card
        title="카드 사용"
        img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2WSlYCEPh2rwaEYywr-CNCHCtO4lIWuLZTA&usqp=CAU"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 25rem;"
      >
        <b-card-text>
          <p v-html="description2.replace(/\n/g, '<br>')"></p>
        </b-card-text>

        <b-button>
          <RouterLink :to="{name: 'common_card'}">카드 사용</RouterLink>
        </b-button>
      </b-card>

      <b-card
        title="경제 사전"
        img-src="data:image/png;base64,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"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 25rem;"
      >
        <b-card-text>
          <p v-html="description3.replace(/\n/g, '<br>')"></p>
        </b-card-text>

        <b-button>
          <RouterLink :to="{name: 'common_dictionary'}">경제 사전</RouterLink>
        </b-button>
      </b-card>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

const description1 = ' 금융 시장 동향, 정책 변화 등을 다루어<br> 경제 상황을 신속하게 파악할 수 있는 <br>중요한 정보원으로 활용됩니다.'
const description2 = '신용카드와 체크카드는 소비 스타일과<br> 금융상황에 따라 다르게 활용됩니다.<br> 이를 이해하면 지출 관리와<br> 금융안정에 도움이 됩니다.'
const description3 = '개인과 사회의 금융 이해를 높이고,<br> 효율적인 금융 거래와 투자에 도움을 줍니다.'
</script>

<style scoped>
.commonpage {
  width: 85%;
  margin: 0 auto;
}

.card-container {
  display: flex;
  justify-content: center;
  gap: 10%;
  margin-top: 3%;
}

button {
  background-color: #E6E6FA;
  border: none;
}

article {
  width: 100%;
}

a {
  color: black;
  text-decoration: none;
}
</style>
