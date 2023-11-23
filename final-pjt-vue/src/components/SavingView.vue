<template>
    <div class="savingpage">
        <h1><i class="bi bi-card-list"></i> 적금 상품 리스트</h1>
        <SavingProduct
            v-for="saving in store.savings"
            :key="saving.id"
            :saving="saving"
            :id="saving.fin_prdt_cd"
        />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

import SavingProduct from '@/components/SavingProduct.vue'

const store = useCounterStore()

onMounted(() => {
  store.getSavings()
})
</script>

<style scoped>
.savingpage {
    width: 85%;
    margin: 0 auto;
}

h1 {
    text-align: center;
}
</style>
