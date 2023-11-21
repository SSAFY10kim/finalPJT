<template>
  <div class="finpage">
    <h1>예적금 금리 비교 페이지</h1>
    <div class="card-container">
      <b-card
        title="예금"
        img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUQNTw90-R7xrftCQTA2-lK0eKfgBvHGEtSQ&usqp=CAU"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
      >
        <b-card-text>
          예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명예금 설명
        </b-card-text>

        <b-button>
          <RouterLink :to="{ name: 'saving' }">예금</RouterLink>
        </b-button>
      </b-card>

      <b-card
        title="적금"
        img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkJ1JDWH3KIxaEKQybnmrXIj0_JNK1of6vZQ&usqp=CAU"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
      >
        <b-card-text>
          적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명적금 설명
        </b-card-text>

        <b-button>
          <RouterLink :to="{ name: 'deposit' }">적금</RouterLink>
        </b-button>
      </b-card>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
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
  gap: 20%;
  margin-top: 8%;
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
