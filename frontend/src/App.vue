<template>
  <div>
    <div v-if="!token">
      <router-view />
    </div>
    <div v-else class="min-h-screen flex">
      <aside class="hidden md:flex md:w-64 bg-white border-r border-gray-200">
        <div class="w-full p-5">
          <div class="flex items-center gap-2 pb-6">
            <div class="h-10 w-10 rounded-xl bg-primary-600 text-white flex items-center justify-center font-bold">ME</div>
            <div>
              <p class="font-semibold text-gray-800 leading-none">Meu Dia na Escola</p>
              <p class="text-xs text-gray-500">Admin</p>
            </div>
          </div>
          <nav class="space-y-1">
            <RouterLink to="/dashboard" class="block px-3 py-2 rounded-lg hover:bg-gray-100" active-class="bg-primary-50 text-primary-700">Dashboard</RouterLink>
            <RouterLink to="/students" class="block px-3 py-2 rounded-lg hover:bg-gray-100" active-class="bg-primary-50 text-primary-700">Alunos</RouterLink>
            <RouterLink to="/classes" class="block px-3 py-2 rounded-lg hover:bg-gray-100" active-class="bg-primary-50 text-primary-700">Turmas</RouterLink>
            <RouterLink to="/attendance" class="block px-3 py-2 rounded-lg hover:bg-gray-100" active-class="bg-primary-50 text-primary-700">Frequência</RouterLink>
            <RouterLink to="/grades" class="block px-3 py-2 rounded-lg hover:bg-gray-100" active-class="bg-primary-50 text-primary-700">Notas</RouterLink>
          </nav>
        </div>
      </aside>

      <div class="flex-1 flex flex-col">
        <header class="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-4 md:px-8">
          <div class="flex items-center gap-3">
            <button class="md:hidden btn btn-outline" @click="open = !open">Menu</button>
            <h1 class="font-semibold text-gray-800">Painel</h1>
          </div>
          <div class="flex items-center gap-3">
            <button class="btn btn-outline" @click="logout">Sair</button>
          </div>
        </header>

        <main class="p-4 md:p-8 bg-gray-50 min-h-[calc(100vh-4rem)]">
          <router-view />
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { setToken } from './api'
const token = ref(localStorage.getItem('token'))
const open = ref(false)
onMounted(() => setToken(token.value))
function logout(){
  localStorage.removeItem('token')
  setToken(null)
  window.location.href = '/login'
}
</script>
