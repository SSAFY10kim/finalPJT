<template>
    <div>
        <h1>Deposit List</h1>
        <DepositProduct
            v-for="deposit in store.deposits"
            :key="deposit.id"
            :deposit="deposit"
        />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

import DepositProduct from '@/components/DepositProduct.vue'

const store = useCounterStore()

onMounted(() => {
  store.getDeposits()
})
</script>

<style scoped>

</style>
