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
        <hr>
        <p>관심 예금</p>
        <ul class="link-list" v-if="userdata.like_deposit.length > 0">
          <router-link v-for=" deposit in userdata.like_deposit" :key="deposit.fin_prdt_nm" :to="{name: 'deposit_detail', params: {deposit_id : deposit.fin_prdt_cd} }" class="link-item">
            {{ deposit.fin_prdt_nm }}
          </router-link>
        </ul>
        <RouterLink v-else :to="{name: 'deposit'}">관심 예금 목록을 추가해주세요</RouterLink>
        <p>관심 적금</p>
        <ul class="link-list" v-if="userdata.like_saving.length > 0">
          <router-link v-for="saving in userdata.like_saving" :key="saving.fin_prdt_nm" :to="{name: 'saving_detail', params: {saving_id : saving.fin_prdt_cd}}" class="link-item">
            {{ saving.fin_prdt_nm }}
          </router-link>
        </ul>
        <RouterLink v-else :to="{name: 'saving'}">관심 적금 목록을 추가해주세요</RouterLink>
      </div>
      <hr>
      <!-- <p> {{ userdata }} </p> -->
    <RouterLink :to="{name: 'profile_update', params: {name: store.LoginName}}">프로필 수정</RouterLink>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, watch, nextTick, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink, RouterView, useRouter } from 'vue-router'

const store = useCounterStore();
const router = useRouter()
const userdata = computed(() => {
  return store.userInfo
})
// userdata.value = store.userInfo

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
.link-item {
  display: block;
}
</style>
