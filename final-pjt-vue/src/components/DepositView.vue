<template>
    <div class="depositpage">
        <h1><i class="bi bi-card-list"></i> 예금 상품 리스트</h1>
        <DepositProduct
            v-for="deposit in store.deposits"
            :key="deposit.id"
            :deposit="deposit"
            :id="deposit.fin_prdt_cd"
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
.depositpage {
    width: 85%;
    margin: 0 auto;
}

h1 {
    text-align: center;
}
</style>
