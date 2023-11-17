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
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, realname, age, money, salary, gender, bank
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
        console.log(gender)
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
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
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
  const getKeyword = function (data1, data2, data3, data4) {
    searchKeyword.value = 'data1' + ' ' + 'data2' + ' ' + 'data3' + ' ' + 'data4'
  }

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin, logOut,
          deposits, savings, getDeposits, getSavings, getComments, comments, searchKeyword, getKeyword
            }
}, { persist: true })
