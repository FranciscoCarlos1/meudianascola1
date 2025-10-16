<template>
  <div>
    <h2 class="text-xl font-semibold text-gray-800 mb-6">Dashboard</h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="card p-6">
        <p class="text-gray-500 text-sm">Total de Alunos</p>
        <p class="text-3xl font-semibold text-gray-800">{{ counts.students }}</p>
      </div>
      <div class="card p-6">
        <p class="text-gray-500 text-sm">Total de Turmas</p>
        <p class="text-3xl font-semibold text-gray-800">{{ counts.classes }}</p>
      </div>
      <div class="card p-6">
        <p class="text-gray-500 text-sm">Última atualização</p>
        <p class="text-lg text-gray-700">{{ new Date().toLocaleString() }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, reactive } from 'vue'
import API from '../api'
const counts = reactive({ students: 0, classes: 0 })

onMounted(async () => {
  const [st, cl] = await Promise.all([
    API.get('/students/'),
    API.get('/classes/'),
  ])
  counts.students = st.data.length
  counts.classes = cl.data.length
})
</script>
