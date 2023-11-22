<template>
  <div class="mainpage">
    <img src="@/assets/Simplify.png" alt="Simplify Image" class="center-image">
  </div>
  <div class="card-container">
    <b-card
      title="예금"
      tag="article"
    >
      <b-card-text>
        통장에 돈을 넣어놓고 '정해진 기간 동안 찾지 않는 예금'. 찾을 경우 이자를 손해봄. 쉽게 말하면 목돈을 넣어 놓고 매달 돈을 타 먹는 통장
      </b-card-text>
    </b-card>
    <b-card
      title="적금"
      tag="article"
    >
      <b-card-text>
        매월 약속한 날짜에 꼬박꼬박 돈을 넣어서 목돈을 만들 때 이용하는 통장. 
      </b-card-text>
    </b-card>
    <b-card
      title="단리: "
      tag="article"
    >
      <b-card-text>
        원금에만 이자가 붙어요
      </b-card-text>
    </b-card>
    <b-card
      title="복리"
      tag="article"
    >
      <b-card-text>
        이자에도 이자가 붙어요
      </b-card-text>
    </b-card>
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

.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

article {
  max-width: 25%;
  margin: auto;
  padding: auto;
}


</style>