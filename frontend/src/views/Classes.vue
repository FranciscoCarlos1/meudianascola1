<template>
  <div style="padding:20px">
    <h2>Turmas</h2>
    <form @submit.prevent="add">
      <input v-model="form.name" placeholder="Nome da Turma">
      <input v-model.number="form.year" placeholder="Ano" type="number">
      <button>Adicionar</button>
    </form>
    <table border="1" cellpadding="6" style="margin-top:10px; width:100%">
      <thead><tr><th>ID</th><th>Nome</th><th>Ano</th><th>Ações</th></tr></thead>
      <tbody>
        <tr v-for="c in classes" :key="c.id">
          <td>{{ c.id }}</td>
          <td><input v-model="c.name"></td>
          <td><input type="number" v-model.number="c.year"></td>
          <td>
            <button @click="save(c)">Salvar</button>
            <button @click="del(c)">Excluir</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'
import API from '../api'

const classes = ref([])
const form = reactive({ name:'', year: new Date().getFullYear() })

async function load() {
  const { data } = await API.get('/classes/')
  classes.value = data
}
async function add() {
  await API.post('/classes/', form)
  form.name=''; form.year=new Date().getFullYear()
  await load()
}
async function save(c) {
  await API.put('/classes/' + c.id, c)
  await load()
}
async function del(c) {
  await API.delete('/classes/' + c.id)
  await load()
}

onMounted(load)
</script>
