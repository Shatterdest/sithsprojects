import { createRouter, createWebHistory } from 'vue-router'
import ArriveTimes from '@/views/ArriveTimes.vue'
import TheGraphs from '@/views/TheGraphs.vue'
import SecondGraph from '@/components/SecondGraph.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    
    {
      path: '/',
      component: ArriveTimes
    },
    {
      path: '/graphs',
      component: TheGraphs
    },
    {
      path:'/graphTwo',
      component: SecondGraph
    }
  ]
})

export default router
