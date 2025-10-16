<template>
  <div class="min-h-screen bg-gradient-to-b from-primary-50 to-white flex items-center justify-center p-4">
    <div class="card w-full max-w-md p-8">
      <div class="flex items-center gap-3 mb-6">
        <div class="h-12 w-12 rounded-xl bg-primary-600 text-white flex items-center justify-center font-bold text-lg">ME</div>
        <div>
          <h2 class="text-xl font-semibold text-gray-800">Meu Dia na Escola</h2>
          <p class="text-sm text-gray-500 -mt-1">Acesse sua conta</p>
        </div>
      </div>

      <form @submit.prevent="login" class="space-y-4">
        <div>
          <label class="text-sm font-medium text-gray-700">E-mail</label>
          <input v-model="email" class="input" placeholder="admin@escola.local">
        </div>
        <div>
          <label class="text-sm font-medium text-gray-700">Senha</label>
          <input type="password" v-model="password" class="input" placeholder="admin123">
        </div>
        <button class="btn btn-primary w-full">Entrar</button>
      </form>
      <p class="text-xs text-gray-500 mt-4">Use o admin inicial: <strong>admin@escola.local</strong> / <strong>admin123</strong></p>
    </div>
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
