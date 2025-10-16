<template>
  <div style="padding:20px">
    <h2>Frequência</h2>
    <form @submit.prevent="save">
      <input v-model.number="class_id" placeholder="ID da Turma" type="number">
      <input v-model.number="student_id" placeholder="ID do Aluno" type="number">
      <input v-model="date" type="date">
      <select v-model="status">
        <option value="present">Presente</option>
        <option value="absent">Faltou</option>
        <option value="late">Atraso</option>
      </select>
      <button>Lançar</button>
    </form>

    <h3 style="margin-top:20px">Registros</h3>
    <ul>
      <li v-for="a in items" :key="a.id">
        {{ a.date }} - aluno {{ a.student_id }} na turma {{ a.class_id }}: {{ a.status }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import API from '../api'

const class_id = ref(1)
const student_id = ref(1)
const date = ref(new Date().toISOString().slice(0,10))
const status = ref('present')
const items = ref([])

async function load() {
  if (!class_id.value) return
  const { data } = await API.get('/attendance/' + class_id.value)
  items.value = data
}

async function save() {
  await API.post('/attendance/', {
    class_id: class_id.value,
    student_id: student_id.value,
    date: date.value,
    status: status.value
  })
  await load()
}

watch(class_id, load, { immediate: true })
</script>
