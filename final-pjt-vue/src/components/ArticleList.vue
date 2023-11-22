<template>
  <div class="articlepage">
    <h1 class="text-center">자유 게시판</h1>
    <template v-if="store.articles.length > -1">
      <table class="table table-hover" style="width: 90%; margin: 10px auto;">
        <thead class="thead-strong">
          <tr>
            <th width="10%" class="border-right">번호</th>
            <th width="" class="border-right">제목</th>
            <th width="20%" class="border-right">작성자</th>
            <th width="20%">작성일</th>
          </tr>
        </thead>
        <tbody>
          <ArticleListItem 
            v-for="article in store.articles"
            :key="article.id"
            :article="article"
          />
        </tbody>
      </table>
      <RouterLink :to="{ name: 'article_create' }" v-if="store.LoginName" class="btn btn-outline-secondary float-right">
      글쓰기
    </RouterLink>
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
import { RouterLink } from 'vue-router'
const store = useCounterStore()

console.log(store.articles)
</script>

<style scoped>
.articlepage {
  width: 85%;
  margin: 0 auto;
}

.border-right {
  border-right: 1px solid #ddd; /* You can adjust the color and thickness as needed */
}

</style>