<template>
  <div>
    <h1>프로필</h1>
    <MyProfile />
  </div>
  <RouterView />
</template>

<script setup>
import MyProfile from '@/components/MyProfile.vue'
import { RouterLink,RouterView } from 'vue-router'
import { ref } from 'vue';

</script>

<style scoped>

</style>
