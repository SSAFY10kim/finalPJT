<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      <label for="username">아이디 : </label>
      <input type="text" v-model.trim="username"><br>
      <label for="password">비밀번호 : </label>
      <input type="password" v-model.trim="password"><br>
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style>

</style>
