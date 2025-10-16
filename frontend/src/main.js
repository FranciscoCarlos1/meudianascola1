import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import { setToken } from './api'

const app = createApp(App)
app.use(createPinia())
app.use(router)

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next({ path: '/login' })
  } else {
    if (token) setToken(token)
    next()
  }
})

app.mount('#app')
