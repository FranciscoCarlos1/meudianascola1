<template>
  <div style="padding:20px">
    <h2>Notas</h2>
    <form @submit.prevent="add">
      <input v-model.number="student_id" placeholder="ID do Aluno" type="number">
      <input v-model.number="class_id" placeholder="ID da Turma" type="number">
      <input v-model="subject" placeholder="Disciplina">
      <input v-model.number="score" type="number" min="0" max="100" placeholder="Nota (0-100)">
      <button>Adicionar</button>
    </form>

    <div style="margin-top:20px">
      <label>Ver notas do aluno:</label>
      <input v-model.number="filter_student" type="number" placeholder="ID do Aluno">
      <button @click="load">Carregar</button>
    </div>

    <table border="1" cellpadding="6" style="margin-top:10px; width:100%">
      <thead><tr><th>ID</th><th>Aluno</th><th>Turma</th><th>Disciplina</th><th>Nota</th><th>Data</th></tr></thead>
      <tbody>
        <tr v-for="g in grades" :key="g.id">
          <td>{{ g.id }}</td>
          <td>{{ g.student_id }}</td>
          <td>{{ g.class_id }}</td>
          <td>{{ g.subject }}</td>
          <td>{{ g.score }}</td>
          <td>{{ new Date(g.date_recorded).toLocaleString() }}</td>
        </tr>
      </tbody>
    </table>
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
