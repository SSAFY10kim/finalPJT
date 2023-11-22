<template>
  <div>
    <ArticleList />
  </div>
  <RouterView />
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink,RouterView } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>
