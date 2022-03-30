import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCodemirror from 'vue-codemirror'
import { Container, Footer, Switch, Col, Main } from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// import ElementUI from 'element-ui'

Vue.use(VueCodemirror)
Vue.use(Container)
Vue.use(Main)
Vue.use(Footer)
Vue.use(Switch)
Vue.use(Col)
// Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')