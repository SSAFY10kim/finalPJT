<template>
  <div>
    <h1>파이널 PJT - 금융비교상품 </h1>
    <RouterLink :to="{ name: 'main' }">[메인 페이지]</RouterLink><br>
    <RouterLink :to="{ name: 'deposit' }">[예적금 금리 비교]</RouterLink><br>
    <RouterLink :to="{ name: 'exchange' }">[환율 계산기]</RouterLink><br>
    <RouterLink :to="{ name: 'search' }">[근처 은행 찾기]</RouterLink><br>
    <RouterLink :to="{ name: 'community' }">[게시판]</RouterLink><br>
    <RouterLink :to="{ name: 'profile' }">[프로필]</RouterLink><br>

  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>
