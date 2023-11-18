<template>
  <div>
    <h1>파이널 PJT - 금융비교상품 </h1>
    <RouterLink :to="{ name: 'main' }">[메인 페이지]</RouterLink> | 
    <RouterLink :to="{ name: 'deposit-info' }">[예적금 금리 비교]</RouterLink> | 
    <RouterLink :to="{ name: 'exchange' }">[환율 계산기]</RouterLink> | 
    <RouterLink :to="{ name: 'search' }">[근처 은행 찾기]</RouterLink> | 
    <RouterLink :to="{ name: 'community' }">[게시판]</RouterLink> | 
    <RouterLink :to="{ name: 'profile', params: {name: store.LoginName}}" v-if="store.isLogin">[프로필]</RouterLink> | 
    <header>
      <nav v-if="store.isLogin">
        <form @submit.prevent="store.logOut">
          <input type="submit" value="logOut">
        </form>
      </nav>
      <nav v-else>
        <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink> |
        <RouterLink :to="{ name: 'login' }">LogIn</RouterLink>
      </nav>
    </header>

  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue';
const store = useCounterStore()

// console.log(user)
</script>

<style scoped>

</style>
