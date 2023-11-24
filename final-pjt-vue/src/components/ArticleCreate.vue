<template>
  <div class="text-center">
    <!--  html 전체 영역을 지정하는 container -->
    <div id="container">
      <!--  create 폼 영역을 -->
      <div id="createBox">
      
        <!-- 로그인 페이지 타이틀 -->
        <div id="createBoxTitle">게시글 작성</div>
        <!-- 아이디, 비번, 버튼 박스 -->
        <div id="inputBox">
          <b-input-group prepend="제목" class="mt-3">
            <b-form-input v-model="title"></b-form-input>
          </b-input-group>
          <b-input-group prepend="내용" class="mt-3">
            <b-form-textarea v-model="content"></b-form-textarea>
          </b-input-group>
          <div class="button-login-box" >
            <button type="button" class="btn btn-primary" style="width:30%; height: 50px; background-color: #E6E6FA; border: none;" @click="createArticle">작성</button>
          </div>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'community' })
    })
    .catch((err) => {
      console.log(err)
      console.log('111')
    })
}


  
</script>

<style scoped>
#container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 100%;
}

#createBox {
  width: 70%;
  text-align: center;
  background-color: #ffffff;
}

#createBoxTitle {
  color:#000000;
  font-weight: bold;
  font-size: 32px;
  text-transform: uppercase;
  padding: 5px;
  margin-bottom: 20px;
  background: linear-gradient(to right, #270a09, #8ca6ce);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
#inputBox {
  margin: 10px;
}

#inputBox > div.button-login-box > button {
  margin-top: 30px;
  padding: 3px 5px;
  width: 30px;
}

</style>
