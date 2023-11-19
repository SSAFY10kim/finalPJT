import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import DepositInfoView from '@/views/DepositInfoView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import BankSearchView from '@/views/BankSearchView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ArticleList from '@/components/ArticleList.vue'
import ArticleListItem from '@/components/ArticleListItem.vue'
import ArticleDetail from '@/components/ArticleDetail.vue'
import ArticleCreate from '@/components/ArticleCreate.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import SavingView from '@/components/SavingView.vue'
import DepositView from '@/components/DepositView.vue'
// import CommentsList from '@/components/CommentsList.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView
    },
    {
      path: '/depositinfo',
      name: 'deposit-info',
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
      path: '/profile/:name',
      name: 'profile',
      component: ProfileView,
      meta: {
        reload:true
      },
    },
    {
      path: '/community/articles',
      name: 'article_list',
      component: ArticleList,
    },
    {
      path: '/community/articles/:id',
      name: 'article_detail',
      component: ArticleDetail
    },
    {
      path: '/community/articles/create',
      name: 'article_create',
      component: ArticleCreate
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
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
    // {
    //   path: '/comments',
    //   name: 'comments',
    //   component: CommentsList,
    // },
    {
      path: '/profile/:name/update',
      name: 'profile_update',
      component: ProfileUpdateView
    }

  ]
})

import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'ArticleView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }
})

export default router
