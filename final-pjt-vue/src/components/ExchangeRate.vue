<template>
  <div>

  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue';
import axios from 'axios'

const store = useCounterStore()

const MONEY_API_KEY = import.meta.env.VITE_MONEY_API_KEY
const API_URL = `https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=${MONEY_API_KEY}&data=AP01`

const createExchangeMoney = function () {
  axios({
    method: 'get',
    url: API_URL,
  })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.error(err)
    })
}
onMounted(() => {
  createExchangeMoney()
})

</script>

<style scoped>

</style>
