<template>
  <div class="commonpage">
    <RouterLink :to="{name: 'common_news'}">경제 뉴스</RouterLink>
    <RouterLink :to="{name: 'common_card'}">카드 사용</RouterLink>
    
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
</style>
