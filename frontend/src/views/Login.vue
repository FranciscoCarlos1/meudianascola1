<template>
  <div style="max-width:400px; margin:50px auto">
    <h1>Meu Dia na Escola</h1>
    <p><strong>Login</strong></p>
    <form @submit.prevent="login">
      <label>Email</label>
      <input v-model="email" placeholder="admin@escola.local" style="width:100%;padding:8px;margin:4px 0">
      <label>Senha</label>
      <input type="password" v-model="password" placeholder="admin123" style="width:100%;padding:8px;margin:4px 0">
      <button style="padding:10px;margin-top:8px">Entrar</button>
    </form>
    <p style="margin-top:10px; font-size:14px; color:#555">
      Use o admin padrão inicial: admin@escola.local / admin123
    </p>
  </div>
</template>

<script setup>
import API, { setToken } from '../api'
import { ref } from 'vue'

const email = ref('admin@escola.local')
const password = ref('admin123')

async function login () {
  const form = new FormData()
  form.append('username', email.value)
  form.append('password', password.value)
  const { data } = await API.post('/auth/login', form)
  localStorage.setItem('token', data.access_token)
  setToken(data.access_token)
  window.location.href = '/dashboard'
}
</script>
