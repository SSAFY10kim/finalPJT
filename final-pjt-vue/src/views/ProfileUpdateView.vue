<template>
  <div>

  </div>
</template>

<script setup>
import axios from 'axios';
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const store = useCounterStore();
const userdata = store.userInfo

const updateProfile = function() {
  axios({
    method: 'put',
    url: `${store.API_URL}/accounts/${userdata.username}/update/`,
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then(function (response) {
        console.log('updated profile');
      })
    .catch(function (error) {
        console.log(error);
      });
  
}



const username = ref(null)
const realname = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)
const gender = ref(null)
const bank = ref(null)

const signUp = function () {
const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    realname: realname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    gender: gender.value,
    bank: bank.value,
}
store.signUp(payload)
}

const genders = ['남자', '여자']

const banks = ["은행선택","국민은행","우리은행","신한은행","KEB하나은행","한국스탠다드차타드은행","외한은행","한국시티은행","경남은행","광주은행","대구은행","부산은행","전북은행","제주은행","기업은행","농협","수협","한국산업은행","한국수출입은행"]
</script>

<style scoped>

</style>