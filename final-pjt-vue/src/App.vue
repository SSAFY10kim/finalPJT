<template>
  <div class="main">
    <!-- <h1>파이널 PJT - 금융비교상품 </h1>
    <RouterLink :to="{ name: 'main' }">[메인 페이지]</RouterLink> | 
    <RouterLink :to="{ name: 'deposit-info' }">[예적금 금리 비교]</RouterLink> | 
    <RouterLink :to="{ name: 'exchange' }">[환율 계산기]</RouterLink> | 
    <RouterLink :to="{ name: 'search' }">[근처 은행 찾기]</RouterLink> | 
    <RouterLink :to="{ name: 'community' }">[게시판]</RouterLink> | 
    <RouterLink :to="{ name: 'profile', params: {name: store.LoginName}}" v-if="store.isLogin">[프로필]</RouterLink> | 
    <header>
      <nav v-if="store.isLogin">
        <form @submit.prevent="store.logOut">
          <input type="submit" value="logOut">
        </form>
      </nav>
      <nav v-else>
        <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink> |
        <RouterLink :to="{ name: 'login' }">LogIn</RouterLink>
      </nav>
    </header> -->
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand class="custom-nav-brand">
        <RouterLink :to="{ name: 'main' }">Simplify</RouterLink>
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="mx-auto"> <!-- 변경된 부분 -->
          <b-button class="custom-nav-button" variant="link">
            <RouterLink :to="{ name: 'deposit-info' }">예적금 금리 비교</RouterLink>
          </b-button>
          <b-button class="custom-nav-button" variant="link">
            <RouterLink :to="{ name: 'exchange' }">환율 계산기</RouterLink>
          </b-button>
          <b-button class="custom-nav-button" variant="link">
            <RouterLink :to="{ name: 'search' }">근처 은행 찾기</RouterLink> 
          </b-button>
          <b-button class="custom-nav-button" variant="link">
            <RouterLink :to="{ name: 'common' }">금융 상식</RouterLink> 
          </b-button>
          <b-button class="custom-nav-button" variant="link">
            <RouterLink :to="{ name: 'community' }">게시판</RouterLink>
          </b-button>
        </b-navbar-nav>
        
        <b-navbar-nav>
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em v-if="store.isLogin">{{ store.LoginName }}</em>
              <em v-else>로그인 해주세요</em>
            </template>
            <b-dropdown-item v-if="store.isLogin">
              <RouterLink :to="{ name: 'profile', params: {name: store.LoginName}}">프로필</RouterLink>
            </b-dropdown-item>
            <b-dropdown-item v-if="store.isLogin">
              <form @submit.prevent="logOutWarning">
                <input type="submit" value="logOut" class="logout-warning">
              </form>
            </b-dropdown-item>
            <b-dropdown-item v-if="!store.isLogin">
              <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink>
            </b-dropdown-item>
            <b-dropdown-item v-if="!store.isLogin">
              <RouterLink :to="{ name: 'login' }">LogIn</RouterLink>
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue';
const store = useCounterStore()

// console.log(user)
const logOutWarning = function() {
  if (confirm("정말 로그아웃 하시겠습니까?")) {
    store.logOut()
  } else {
    return false
  }
}
</script>

<style scoped>
.navbar {
  background-color: #E6E6FA !important;
}

.custom-nav-brand {
  margin-left: 0%
}

.custom-nav-button {
  margin-left: auto;
  margin-right: auto;
  color: #000;
  text-decoration: none;
  transition: color 0.3s, font-size 0.3s;
}

.custom-nav-button:hover {
  font-size: 1.2em;
}

a:hover {
  color: #007bff;
}

a {
  text-decoration: none;
  color: black;
  font-weight: bold;
}

.logout-warning:hover {
  color: red;
}


.navbar-toggler {
  margin-right: 5%;
}


</style>

<style>
.main {
  width: 90%;
  margin: 0 auto;
}

</style>
