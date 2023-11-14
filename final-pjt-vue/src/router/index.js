import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import DepositInfoView from '@/views/DepositInfoView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import BankSearchView from '@/views/BankSearchView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ProfileView from '@/views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositInfoView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeRateView
    },
    {
      path: '/search',
      name: 'search',
      component: BankSearchView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    }

  ]
})

export default router
