<template>
  <tr>
    <td class="border-right">{{ article.id }}</td>
    <td class="border-right">
      <RouterLink :to="{ name: 'article_detail', params: { id: article.id }}">
        {{ article.title }}
      </RouterLink>
    </td>
    <td class="border-right">{{ article.user_username }}</td>
    <td>{{ formatDate(article.created_at) }}</td>
  </tr>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})

const formatDate = (timestamp) => {
  // Assuming timestamp is a string in the format "YYYY-MM-DDTHH:mm:ss.sssZ"
  return timestamp.substring(0, 10); // Extracts the first 10 characters (YYYY-MM-DD)
};
</script>

<style scoped>
.border-right {
  border-right: 1px solid #ddd; /* You can adjust the color and thickness as needed */
}
</style>