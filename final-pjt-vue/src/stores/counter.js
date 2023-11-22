import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const articles = ref([])
  const comments = ref([])
  const searchKeyword = ref('')
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const LoginName = ref(null)
  const userInfo = ref([])
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        articles.value = []
        console.log(err)
      })
  }
  
  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/comments`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((res) => {
      console.log(res)
      comments.value = res.data
    }).catch((err) => {
      console.log(err)
    })

  }

  const signUp = function (payload) {
    const { username, password1, password2, realname, age, money, salary, gender, bank } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, realname, age, money, salary, gender, bank
      }
    })
      .then((res) => {
        console.log(res)
        console.log('123123')
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        LoginName.value = payload.username
        getUser()
        router.push({ name: 'main' })
        
      })
      .catch((err) => { 
        console.log(err)
      })
  }

  const getUser = function () {
    if (isLogin.value === true) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/${LoginName.value}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log(res.data)
        userInfo.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }}

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        LoginName.value = null
        userInfo.value = []
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const deposits = ref([])
  const savings = ref([])

  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/deposit/`,
    })
      .then((res) => {
        deposits.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const getSavings = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/saving/`, 
    })
      .then((res) => {
        savings.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const recommended = ref([])

  const getRecommended = function () {
    if (isLogin.value === true) {
    // console.log(userInfo.value.username)
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/${LoginName.value}/recommended/`,
      params: { username: userInfo.value.username },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        recommended.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }


  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin, logOut,
          deposits, savings, getDeposits, getSavings, getComments, comments, searchKeyword,
          getUser, LoginName, userInfo, recommended, getRecommended }
}, { persist: true })
