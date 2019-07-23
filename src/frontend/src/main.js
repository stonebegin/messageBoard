import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// import router from '../src/router'
import App from './App.vue'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(VueAxios, axios)


new Vue({
  el: '#app',
  // router,
  render: h => h(App)
})
