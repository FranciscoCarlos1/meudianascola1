<template>
  <div class="space-y-6">
    <h2 class="text-xl font-semibold text-gray-800">Frequência</h2>

    <form @submit.prevent="save" class="card p-6 grid md:grid-cols-5 gap-3">
      <input v-model.number="class_id" placeholder="ID da Turma" type="number" class="input md:col-span-1">
      <input v-model.number="student_id" placeholder="ID do Aluno" type="number" class="input md:col-span-1">
      <input v-model="date" type="date" class="input md:col-span-1">
      <select v-model="status" class="input md:col-span-1">
        <option value="present">Presente</option>
        <option value="absent">Faltou</option>
        <option value="late">Atraso</option>
      </select>
      <button class="btn btn-primary md:col-span-1">Lançar</button>
    </form>

    <div class="card p-0 overflow-hidden">
      <table class="table">
        <thead class="bg-gray-50">
          <tr>
            <th class="th">ID</th>
            <th class="th">Data</th>
            <th class="th">Aluno</th>
            <th class="th">Turma</th>
            <th class="th">Status</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100 bg-white">
          <tr v-for="a in items" :key="a.id">
            <td class="td">{{ a.id }}</td>
            <td class="td">{{ a.date }}</td>
            <td class="td">{{ a.student_id }}</td>
            <td class="td">{{ a.class_id }}</td>
            <td class="td capitalize">{{ a.status }}</td>
          </tr>
        </tbody>
      </table>
    </div>
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
