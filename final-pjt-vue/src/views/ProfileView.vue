<template>
  <div class="profilepage">
    <MyProfile />
  </div>
  <RouterView />
</template>

<script setup>
import MyProfile from '@/components/MyProfile.vue'
import { RouterLink,RouterView, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue';

</script>

<style scoped>

</style>
