<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue' 
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  import { useRouter, useRoute } from 'vue-router'
  
  const title = ref('')
  const content = ref('')
  const store = useCounterStore()
  const router = useRouter()
  const route = useRoute()
  
  onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
    })
      .then((res) => {
        title.value = res.data.title
        content.value = res.data.content
      })
      .catch((err) => {
        console.log(err)
      })
  })

  const updateArticle = function () {
    axios({
      method: 'put',
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
      data: {
        title: title.value,
        content: content.value
      },
      headers: {
          Authorization: `Token ${store.token}`
        }
    })
      .then((res) => {
        console.log(res)
        router.push({ name: 'community' })
      })
      .catch((err) => {
        console.log(err)
        console.log('111')
      })
  }
  
  
    
  </script>
  
  <style>
  
  </style>
  