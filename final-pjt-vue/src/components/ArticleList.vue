<template>
  <div>
    <h3>Article List</h3>
    <template v-if="store.articles.length > 0">
      <ArticleListItem 
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
      />
    </template>
    <template v-else>
      <p>No articles available</p>
    </template>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'
import { onMounted } from 'vue';

const store = useCounterStore()

console.log(store.articles)
</script>
