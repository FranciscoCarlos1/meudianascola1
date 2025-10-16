<template>
  <div style="padding:20px">
    <h2>Alunos</h2>
    <form @submit.prevent="add">
      <input v-model="form.name" placeholder="Nome">
      <input v-model="form.cpf" placeholder="CPF">
      <input v-model="form.email" placeholder="Email">
      <button>Adicionar</button>
    </form>
    <table border="1" cellpadding="6" style="margin-top:10px; width:100%">
      <thead><tr><th>ID</th><th>Nome</th><th>CPF</th><th>Email</th><th>Ações</th></tr></thead>
      <tbody>
        <tr v-for="s in students" :key="s.id">
          <td>{{ s.id }}</td>
          <td><input v-model="s.name"></td>
          <td><input v-model="s.cpf"></td>
          <td><input v-model="s.email"></td>
          <td>
            <button @click="save(s)">Salvar</button>
            <button @click="del(s)">Excluir</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'
import API from '../api'

const students = ref([])
const form = reactive({ name:'', cpf:'', email:'' })

async function load() {
  const { data } = await API.get('/students/')
  students.value = data
}
async function add() {
  await API.post('/students/', form)
  form.name=''; form.cpf=''; form.email=''
  await load()
}
async function save(s) {
  await API.put('/students/' + s.id, s)
  await load()
}
async function del(s) {
  await API.delete('/students/' + s.id)
  await load()
}

onMounted(load)
</script>
