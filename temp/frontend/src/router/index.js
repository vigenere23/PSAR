import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/widgets',
    name: 'widgets',
    component: () => import('@/views/Widgets.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
