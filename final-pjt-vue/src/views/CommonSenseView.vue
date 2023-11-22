<template>
  <div>
    <NaverNews />
  </div>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router';
import NaverNews from '@/components/NaverNews.vue';

</script>

<style scoped>

</style>
