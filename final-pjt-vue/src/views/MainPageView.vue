<template>
  <div class="mainpage">
    <img src="@/assets/Simplify.png" alt="Simplify Image" class="center-image">
    
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.mainpage {
  width: 85%;
  margin: 0 auto;
  margin-top: 30px;
}

/* 이미지 스타일을 추가하고 싶다면 아래와 같이 스타일을 지정할 수 있습니다. */
.center-image {
  display: block; /* 가운데 정렬을 위해 블록 요소로 설정합니다. */
  margin: 0 auto; /* 좌우 여백을 자동으로 설정하여 가운데 정렬합니다. */
  width: 80%; /* 이미지의 너비를 조절합니다. */
  max-width: 100%; /* 이미지의 최대 너비를 설정합니다. */
}

h1 {
  text-align: center;
}
</style>