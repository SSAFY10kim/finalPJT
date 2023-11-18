<template>
  <div>
    <div class="userinfo">
      <p>아이디 {{ userdata.username }}</p>
      <p>이름 {{ userdata.realname }}</p>
      <p>나이 {{ userdata.age }}</p>
      <p>성별 {{ userdata.gender }}</p>
      <p>자산 {{ userdata.money }}</p>
      <p>연봉 {{ userdata.salary }}</p>
      <p>주거래은행 {{ userdata.bank }}</p>
      <p>구독 저축 {{ userdata.like_deposit }}</p>
      <p>구독 적금 {{ userdata.like_saving }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();

onMounted(async () => {
  await store.getUser();
});

const userdata = store.userInfo
console.log(userdata)

</script>

<style scoped>

</style>
