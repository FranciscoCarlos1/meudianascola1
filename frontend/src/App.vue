<template>
  <div>
    <nav v-if="token" style="padding:10px; border-bottom:1px solid #ddd; display:flex; gap:10px">
      <router-link to="/dashboard">Dashboard</router-link>
      <router-link to="/students">Alunos</router-link>
      <router-link to="/classes">Turmas</router-link>
      <router-link to="/attendance">Frequência</router-link>
      <router-link to="/grades">Notas</router-link>
      <a href="#" @click.prevent="logout" style="margin-left:auto">Sair</a>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { setToken } from './api'
const token = ref(localStorage.getItem('token'))
onMounted(() => setToken(token.value))
function logout () {
  localStorage.removeItem('token')
  setToken(null)
  window.location.href = '/login'
}
</script>
