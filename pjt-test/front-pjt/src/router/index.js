import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DepositView from '@/views/DepositView.vue'
import SavingView from '@/views/SavingView.vue'
import ExchangeView from '@/views/ExchangeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/saving',
      name: 'saving',
      component: SavingView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
  ]
})

export default router
