<template>
    <div>
        <h1>Saving List</h1>
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

</style>
