<template>
  <div>
    <h1>프로필 수정</h1>
    <form @submit.prevent="updateProfile">
        <label for="username">아이디 : </label>
        <input type="text" id="username" v-model.trim="username"><br>
        <label for="realname">이름 : </label>
        <input type="text" id="realname" v-model.trim="realname"><br>
        <label for="age">나이 : </label>
        <input type="number" id="age" v-model.trim="age"><br>
        <label for="money">현재 재산 : </label>
        <input type="number" id="money" v-model.trim="money"><br>
        <label for="salary">연봉 : </label>
        <input type="number" id="salary" v-model.trim="salary"><br>
        <label for="gender">성별 : </label>
        <input type="text" id="gender" v-model.trim="gender"><br>
        <label for="bank">주거래 은행 : </label>
        <select id="bank" v-model="bank">
            <option v-for="b in banks" :value="b">{{ b }}</option>
        </select>
        <input type="submit">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const store = useCounterStore();
const userdata = store.userInfo
const router = useRouter()



const username = ref(userdata.username)
const realname = ref(userdata.realname)
// const password1 = ref(userdata.password1)
// const password2 = ref(null)
const age = ref(userdata.age)
const money = ref(userdata.money)
const salary = ref(userdata.salary)
const gender = ref(userdata.gender)
const bank = ref(userdata.bank)

const updateProfile = function() {
  axios({
    method: 'put',
    url: `${store.API_URL}/accounts/profile/${userdata.username}/update/`,
    data: {
        username: username.value,
        realname: realname.value,
        age: age.value,
        money: money.value,
        salary: salary.value,
        gender: gender.value,
        bank: bank.value
      },
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then(function (response) {
        console.log('updated profile', response.data);
        console.log(username, realname, age, money, salary, gender, bank)
        // router.push({name: 'main'})
        router.push({ name: 'profile', params: {name: store.LoginName}})
        // router.replace({ name: 'profile', params: {name: store.LoginName}}) 
      })
    .catch(function (error) {
        console.log(123123123)
        console.log(error);
      });
  
}

const genders = ['남자', '여자']

const banks = ["은행선택","국민은행","우리은행","신한은행","KEB하나은행","한국스탠다드차타드은행","외한은행","한국시티은행","경남은행","광주은행","대구은행","부산은행","전북은행","제주은행","기업은행","농협","수협","한국산업은행","한국수출입은행"]
</script>

<style scoped>

</style>