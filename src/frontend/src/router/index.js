import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import SignUp from '../components/SignUp.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login', 
    component: {
      default: Login
    }
  },
  {
    path: '/signup', 
    component: {
      default: SignUp
    }
  }
  ]
  
  const router = new VueRouter({
    mode: 'history',
    routes
  })

  export default router