<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home' }">
        [Home]
      </RouterLink>
      <RouterLink :to="{ name: 'deposit' }">
        [Deposit]
      </RouterLink>
      <RouterLink :to="{ name: 'saving' }">
        [Saving]
      </RouterLink>
      <RouterLink :to="{ name: 'exchange' }">
        [Exchange]
      </RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
