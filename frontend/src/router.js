import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import Dashboard from './views/Dashboard.vue'
import Students from './views/Students.vue'
import Classes from './views/Classes.vue'
import Attendance from './views/Attendance.vue'
import Grades from './views/Grades.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/students', component: Students },
  { path: '/classes', component: Classes },
  { path: '/attendance', component: Attendance },
  { path: '/grades', component: Grades },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
