<template>
  <div class="commonpage text-center">
    <h1><i class="bi bi-newspaper"></i> 경제 뉴스</h1>
    <div class="Fnews text-center">
      <div style="border-bottom: 1px solid black;"><h2>경제 뉴스</h2></div>
      <p v-for="news in newsList">
        <a :href="news.link" target="_blank" v-html=news.title style="text-decoration: none; color: black;"></a>
      </p>
    </div>
    <div class="description text-center">
      <h2><i class="bi bi-question-circle-fill"></i> 왜 뉴스를 챙겨봐야 하나요?</h2>
      <p v-html="description.replace(/\n/g, '<br>')"></p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter, RouterLink } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const router = useRouter()
const newsList = ref([])

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/navernews/`
  })
    .then((response) => {
      newsList.value = response.data.items
      // console.log(response)
    })
    .catch((error) => {
      // console.error(error)
    })
})

const description = '경제 뉴스를 이해하는 것은 일상생활, 투자, 기업 상황, 정책 영향, 글로벌 동향을 파악하는데 도움이 됩니다.<br> 경제 지표와 정책은 소비자, 기업, 투자자에게 직접적인 영향을 미치며, 글로벌 경제의 연결성과 시민의 책임에도 영향을 줍니다.<br> 이를 통해 미래에 대한 결정을 내릴 수 있고, 사회에 미치는 영향을 이해할 수 있습니다.'

</script>


<style scoped>
.commonpage {
  width: 85%;
  margin: 0 auto;
}
.Fnews {
  border: 1px solid black;
  width: 80%;
  margin: 10px auto;
}
</style>
