<template>
<div class="articledetail">
  <div v-if="article">
    <div style="margin-top: 20px;">
    <span style="font-size: 30px; margin-right: 20px;">{{ article.id }}.</span>
    <span style="font-size: 30px">{{ article.title }}</span>
    </div>
    <!-- <p>제목 : {{ article.title }}</p> -->
    <div class="row">
      <b-card-group deck class="mb-3">
        <b-card col md="6" border-variant="dark" header="내용" align="left">
          <b-card-text>{{ article.content }}</b-card-text>
        </b-card>
        <!-- Add more cards if needed -->
      </b-card-group>
      <hr>
    </div>
    <!-- <p>작성일 : {{ article.created_at }}</p> -->
    <p class="float-right">작성일 : {{ formattedDate }}</p>
    <p>작성자 : {{ article.user_username }}</p>
    <div>
    <button class="btn btn-outline-secondary float-left" v-if="article.user_username === store.LoginName">
      <RouterLink :to="{name: 'article_update', params: {id: article.id}}" v-if="store.isLogin" style="text-decoration: none; color: black;">게시글 수정</RouterLink>
    </button>
    </div>
    <div v-if="article.user_username === store.LoginName">
      <button @click="confirmDelete(route.params.id)" v-if="store.isLogin" class="btn btn-outline-danger float-right">삭제</button>
    </div>
    </div>
    <div v-if="store.isLogin">
      <div class="mt-3">
        <b-input-group size="lg" style="width: 100%;">
          <b-input-group-prepend>
            <b-input-group-text>댓글</b-input-group-text>
          </b-input-group-prepend>
          
          <b-form-input v-model="comment_content"></b-form-input>
          
          <b-input-group-append >
            <b-button variant="outline-success" @click="createComment">등록</b-button>
          </b-input-group-append>
        </b-input-group>
      </div>
    </div>

    <p v-if="article" style="font-size: 20px; margin-top: 20px;">댓글 갯수 :  {{ article.comment_count }}개</p>
    <CommentsList :article-id="route.params.id" @commentDeleted="refreshArticle"/>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { routerKey, useRoute, useRouter, RouterLink } from 'vue-router'
import { onBeforeRouteLeave } from 'vue-router'
import CommentsList from '@/components/CommentsList.vue'
// import useCounterStore from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const comment_content = ref(null) 
const formattedDate = ref(null)

onMounted(() => {
axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    // headers: {
    //     Authorization: `Token ${store.token}`
    //   }
})
    .then((res) => {
    console.log(res.data)
    article.value = res.data
    
    const date = new Date(article.value.updated_at);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');

      formattedDate.value = `${year}-${month}-${day} ${hours}:${minutes}`;
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

<style scoped>
.articledetail {
  width: 85%;
  margin: 0 auto;
}

</style>
