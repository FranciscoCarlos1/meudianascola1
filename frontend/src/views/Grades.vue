<template>
  <div class="space-y-6">
    <h2 class="text-xl font-semibold text-gray-800">Notas</h2>

    <form @submit.prevent="add" class="card p-6 grid md:grid-cols-5 gap-3">
      <input v-model.number="student_id" placeholder="ID do Aluno" type="number" class="input">
      <input v-model.number="class_id" placeholder="ID da Turma" type="number" class="input">
      <input v-model="subject" placeholder="Disciplina" class="input">
      <input v-model.number="score" type="number" min="0" max="100" placeholder="Nota (0-100)" class="input">
      <button class="btn btn-primary">Adicionar</button>
    </form>

    <div class="card p-4 flex items-center gap-3">
      <label>Ver notas do aluno:</label>
      <input v-model.number="filter_student" type="number" placeholder="ID do Aluno" class="input max-w-[200px]">
      <button class="btn btn-outline" @click="load">Carregar</button>
    </div>

    <div class="card overflow-hidden">
      <table class="table">
        <thead class="bg-gray-50">
          <tr>
            <th class="th">ID</th>
            <th class="th">Aluno</th>
            <th class="th">Turma</th>
            <th class="th">Disciplina</th>
            <th class="th">Nota</th>
            <th class="th">Data</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100 bg-white">
          <tr v-for="g in grades" :key="g.id">
            <td class="td">{{ g.id }}</td>
            <td class="td">{{ g.student_id }}</td>
            <td class="td">{{ g.class_id }}</td>
            <td class="td">{{ g.subject }}</td>
            <td class="td">{{ g.score }}</td>
            <td class="td">{{ new Date(g.date_recorded).toLocaleString() }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import API from '../api'

const student_id = ref(1)
const class_id = ref(1)
const subject = ref('Matemática')
const score = ref(100)

const filter_student = ref(1)
const grades = ref([])

async function add() {
  const { data } = await API.post('/grades/', {
    student_id: student_id.value,
    class_id: class_id.value,
    subject: subject.value,
    score: score.value
  })
  if (data?.id) await load()
}

async function load() {
  const { data } = await API.get('/grades/' + filter_student.value)
  grades.value = data
}
</script>
