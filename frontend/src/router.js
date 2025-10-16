import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import Dashboard from './views/Dashboard.vue'
import Students from './views/Students.vue'
import Classes from './views/Classes.vue'
import Attendance from './views/Attendance.vue'
import Grades from './views/Grades.vue'

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/students', component: Students, meta: { requiresAuth: true } },
  { path: '/classes', component: Classes, meta: { requiresAuth: true } },
  { path: '/attendance', component: Attendance, meta: { requiresAuth: true } },
  { path: '/grades', component: Grades, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
