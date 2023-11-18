<template>
  <div>
    <template v-for="comment in store.comments" :key="comment.id">
      <li v-if="comment.article === Number(props.articleId)">
        <span>{{ comment.user_username }}</span> : <span>{{ comment.content }}</span>
        <button @click="confirmDelete(comment.id)" class="delete-button">삭제</button>
      </li>
    </template>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import axios from 'axios';

const store = useCounterStore();

const props = defineProps({
  articleId: String,
});

const emit = defineEmits(['commentDeleted'])

const confirmDelete = function (id) {
  if (window.confirm('정말로 삭제하시겠습니까?')) {
    deleteComment(id);
  }
};


const deleteComment = function (id) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/comments/${id}/`,
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then((res) => {
      console.log(res);
      // 게시글 디테일로 emit
      emit('commentDeleted')
      // 삭제 성공 시, 다시 댓글 목록을 갱신
      store.getComments();
    })
    .catch((err) => {
      console.log(err);
      alert('댓글 삭제 중 오류가 발생했습니다.');
    });
};
</script>

<style scoped>
.delete-button {
  margin-left: 8px;
  color: red; /* 삭제 버튼에 적절한 스타일 적용 */
  cursor: pointer;
}
</style>
