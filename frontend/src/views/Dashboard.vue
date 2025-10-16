<template>
  <div style="padding:20px">
    <h2>Dashboard</h2>
    <ul>
      <li>Total de alunos: {{ counts.students }}</li>
      <li>Total de turmas: {{ counts.classes }}</li>
    </ul>
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
