<template>
  <div class="profilepage">
    <h1>{{ userdata.realname }}님의 프로필</h1>
    <div class="userinfo">
      <table class="userinfo">
        <tr>
          <td style="text-align: center;">아이디</td>
          <td style="text-align: center;">{{ userdata.username }}</td>
        </tr>
        <tr>
          <td style="text-align: center;">이름</td>
          <td style="text-align: center;">{{ userdata.realname }}</td>
        </tr>
        <tr>
          <td style="text-align: center;">나이</td>
          <td style="text-align: center;">{{ userdata.age }}</td>
        </tr>
        <tr>
          <td style="text-align: center;">성별</td>
          <td style="text-align: center;">{{ userdata.gender }}</td>
        </tr>
        <tr>
          <td style="text-align: center;">자산</td>
          <td style="text-align: center;">{{ userdata.money }}</td>
        </tr>
        <tr>
          <td style="text-align: center;">연봉</td>
          <td style="text-align: center;">{{ userdata.salary }}</td>
        </tr>
        <tr>
          <td style="text-align: center;">주거래은행</td>
          <td style="text-align: center;">{{ userdata.bank }}</td>
        </tr>
      </table>
    </div>
        <hr>
        <div class="depositdiv">
        <p>관심 예금</p>
        <div class="link-list" v-if="userdata.like_deposit.length > 0">
          <router-link v-for=" deposit in userdata.like_deposit" :key="deposit.fin_prdt_nm" :to="{name: 'deposit_detail', params: {deposit_id : deposit.fin_prdt_cd} }" class="link-item">
            {{ deposit.fin_prdt_nm }}
          </router-link>
        </div>
        <RouterLink v-else :to="{name: 'deposit'}">관심 예금 목록을 추가해주세요</RouterLink>
        </div>
        <div class="savingdiv">
        <p>관심 적금</p>
        <div class="link-list" v-if="userdata.like_saving.length > 0">
          <router-link v-for="saving in userdata.like_saving" :key="saving.fin_prdt_nm" :to="{name: 'saving_detail', params: {saving_id : saving.fin_prdt_cd}}" class="link-item">
            {{ saving.fin_prdt_nm }}
          </router-link>
        </div>
        <RouterLink v-else :to="{name: 'saving'}">관심 적금 목록을 추가해주세요</RouterLink>
        </div>
      <hr>
    <div class="profileupdate">
      <button class="btn btn-outline-secondary"><RouterLink :to="{name: 'profile_update', params: {name: store.LoginName}}">프로필 수정</RouterLink></button>
    </div>
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
.profilepage {
  width: 85%;
  margin: 0 auto;
}

.profilepage h1 {
  text-align: center;
}

.profileupdate {
  text-align: center;
}

.depositdiv, .savingdiv {
  text-align: center;
}

.depositdiv a, .savingdiv a {
  text-decoration: none;
}

.profileupdate a {
  color: black;
  text-decoration: none;
}

.table {
  border-collapse: collapse;
  border: 1px solid black;
  margin-bottom: 20px;
}

th, td {
  border: 1px solid black;
  padding: 10px;
}

.userinfo {
  margin: 40px auto;
}
</style>
