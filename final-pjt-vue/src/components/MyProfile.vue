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
      <p> {{ userdata }} </p>
    <RouterLink :to="{name: 'profile_update', params: {name: store.LoginName}}">프로필 수정</RouterLink>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, watch, nextTick } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink, RouterView, useRouter } from 'vue-router'

const store = useCounterStore();
const router = useRouter()
const userdata = ref(store.userInfo)

// const fetchData = () => {
//   // 비동기 작업 예시 (예: API 호출)
//   setTimeout(() => {
//     store.getUser();
//     userdata.value = store.userInfo;
//   }, 1000); // 1초 뒤에 데이터 갱신
// };


onMounted(async () => {
  // fetchData()
  store.getUser();
  userdata.value = store.userInfo
  await nextTick();

});


console.log(userdata.value)
watch(userdata, () => {
  userdata.value = store.userInfo
})

</script>

<style scoped>

</style>
