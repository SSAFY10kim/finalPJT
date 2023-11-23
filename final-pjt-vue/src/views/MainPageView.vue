<template>
  <div class="mainpage">
    <div class="image-container">
      <img src="@/assets/Simplify.png" alt="Simplify Image" class="center-image">
      <div class="text-overlay">
        <h2>Simplify</h2>
        <p>예적금 금리 비교, 환율 계산기, 금융 상식, 그리고 더 많은 기능으로 </p><p>여러분의 금융을 더욱 편리하게 만나보세요.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.mainpage {
  width: 85%;
  margin: 0 auto;
  margin-top: 30px;
}

.image-container {
  position: relative;
}

.center-image {
  display: block;
  margin: 0 auto;
  width: 80%;
  max-width: 100%;
}

.text-overlay {
  position: absolute;
  top: 100%; /* 상단 여백을 조절하여 수직 가운데 정렬합니다. */
  left: 50%; /* 좌측 여백을 조절하여 수평 가운데 정렬합니다. */
  transform: translate(-50%, -50%); /* 수평, 수직 정렬을 위한 변형을 적용합니다. */
  text-align: center; /* 텍스트를 가운데 정렬합니다. */
  color: #c1c1ff; /* 텍스트 색상을 설정합니다. */
  font-weight: bold;
}

.text-overlay h2 {
  font-size: 3em; /* 제목의 글자 크기를 조절합니다. */
  margin-bottom: 10px; /* 제목과 단락 사이의 여백을 조절합니다. */
}

.text-overlay p {
  font-size: 1.2em; /* 단락의 글자 크기를 조절합니다. */
}
</style>
