<template>
    <div>
        <h1>Home</h1>
        <!-- <RouterLink :to="{ name: 'deposit' }">
            [Deposit]
        </RouterLink>
        <RouterLink :to="{ name: 'saving' }">
            [Saving]
        </RouterLink>
        <RouterLink :to="{ name: 'exchange' }">
            [Exchange]
        </RouterLink> -->
    </div>
    <RouterView />
</template>

<script setup>
import { RouterLink } from 'vue-router'

</script>

<style scoped>

</style>
