<template>
  <div>
    <h1>예적금 금리 비교 페이지</h1>
    <RouterLink :to="{ name: 'saving' }">예금</RouterLink> | 
    <RouterLink :to="{ name: 'deposit' }">적금</RouterLink>
  </div>
  <RouterView /> 
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>
