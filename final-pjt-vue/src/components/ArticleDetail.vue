<template>
<div>
    <h1>Detail</h1>
    <div v-if="article">
    <p>{{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일 : {{ article.created_at }}</p>
    <p>수정일 : {{ article.updated_at }}</p>
    <p>{{ article.user_username }}</p>
    </div>
    <p v-if="article">댓글 갯수 :{{ article.comment_count }}</p>
    <div>
        <form @submit.prevent="createComment">
            <input type="text" v-model="comment_content">
            <input type="submit">
        </form>
    </div>
    <button @click="confirmDelete(route.params.id)">삭제
    </button>
    <CommentsList :article-id="route.params.id" @commentDeleted="refreshArticle()"/>
</div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { routerKey, useRoute, useRouter } from 'vue-router'
import { onBeforeRouteLeave } from 'vue-router'
import CommentsList from '@/components/CommentsList.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const comment_content = ref(null) 

onMounted(() => {
axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
        Authorization: `Token ${store.token}`
      }
})
    .then((res) => {
    console.log(res.data)
    article.value = res.data
    })
    .catch((err) => {
    console.log(err)
    
    })
})

const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    data: {
      content: comment_content.value
    },
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then((res) => {
      console.log(res)
      // router.push({ name: `community/articles/${route.params.id}` })
      store.getComments();
      comment_content.value = ''
      // 댓글 갯수 갱신 (재통신...?)
      axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
        headers: {
            Authorization: `Token ${store.token}`
          }
      })
        .then((res) => {
        console.log(res.data)
        article.value = res.data
        })
        .catch((err) => {
        console.log(err)
        })
    })
    .catch((err) => {
      console.log(err)
      console.log(comment_content.value)
    })
}

const confirmDelete = function (id) {
  if (window.confirm('정말로 삭제하시겠습니까?')) {
    deleteArticle(id);
  }
};

const deleteArticle = function(id) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/articles/${id}`,
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then((res) => {
      console.log(res)
      store.getArticles()
      router.push({name: 'community'})
    })
    .catch((err) => {
      console.log(err);
      alert('게시글 삭제 중 오류가 발생했습니다.');
    });
}

const refreshArticle = function() {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
        Authorization: `Token ${store.token}`
      }
})
    .then((res) => {
    console.log(res.data)
    article.value = res.data
    })
    .catch((err) => {
    console.log(err)
    
    })
}

defineProps({
  comment_list : String,
})
</script>

<style>

</style>
