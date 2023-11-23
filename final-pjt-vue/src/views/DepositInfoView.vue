<template>
  <div class="finpage">
    <h1 style="margin-bottom: 20px;"><i class="bi bi-piggy-bank"></i> 예적금 금리 비교</h1>
    <p>예적금 금리 비교는 최상의 수익을 찾기 위해 중요합니다. 높은 금리로 선택하면 더 많은 이자 수익을 얻어 재무 목표를 효과적으로 달성할 수 있습니다.</p>
    <div class="card-container">
      <b-card
        title="예금"
        img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUQNTw90-R7xrftCQTA2-lK0eKfgBvHGEtSQ&usqp=CAU"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 25rem;"
      >
        <b-card-text>
          <p v-html="description1.replace(/\n/g, '<br>')"></p>
        </b-card-text>

        <b-button>
          <RouterLink :to="{ name: 'deposit' }">예금</RouterLink>
        </b-button>
      </b-card>

      <b-card
        title="적금"
        img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkJ1JDWH3KIxaEKQybnmrXIj0_JNK1of6vZQ&usqp=CAU"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 25rem;"
      >
        <b-card-text>
          <p v-html="description2.replace(/\n/g, '<br>')"></p>
        </b-card-text>

        <b-button>
          <RouterLink :to="{ name: 'saving' }">적금</RouterLink>
        </b-button>
      </b-card>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

const description1 = '자유롭게 돈을 입출금할 수 있는 금융 상품으로,<br> 일상 소비용으로 활용됩니다.<br> 예금 통장에서는 언제든지 필요한 만큼의 금액을<br> 인출하거나 입금할 수 있어 편리하게<br> 자금을 운용할 수 있습니다.'
const description2 = '정해진 기간 동안 정기적인 납입을 통해<br> 저축하는 상품으로, <br>목돈을 만들거나 계획적인 저축에 활용됩니다.<br> 만기에는 원금과 이자를 수령할 수 있어 장기적인 목표를 위한 안정적인 저축 수단으로 선택됩니다.'
</script>

<style scoped>
.finpage {
  width: 85%;
  margin: 0 auto;
  text-align: center;
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
