<template>
<div>
    <h1>Signup</h1>
    <form @submit.prevent="signUp">
        <label for="username">아이디 : </label>
        <input type="text" id="username" v-model.trim="username"><br>
        <label for="password1">비밀번호 : </label>
        <input type="password" id="password1" v-model.trim="password1"><br>
        <label for="password2">비밀번호 확인 : </label>
        <input type="password" id="password2" v-model.trim="password2"><br>
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
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
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

<style>

</style>
