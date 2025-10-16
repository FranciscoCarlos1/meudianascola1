<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <h2 class="text-xl font-semibold text-gray-800">Turmas</h2>
      <form @submit.prevent="add" class="flex gap-3">
        <input v-model="form.name" placeholder="Nome da Turma" class="input">
        <input v-model.number="form.year" placeholder="Ano" type="number" class="input">
        <button class="btn btn-primary">Adicionar</button>
      </form>
    </div>

    <div class="card overflow-hidden">
      <table class="table">
        <thead class="bg-gray-50">
          <tr>
            <th class="th">ID</th>
            <th class="th">Nome</th>
            <th class="th">Ano</th>
            <th class="th">Ações</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100 bg-white">
          <tr v-for="c in classes" :key="c.id">
            <td class="td">{{ c.id }}</td>
            <td class="td"><input v-model="c.name" class="input"></td>
            <td class="td"><input type="number" v-model.number="c.year" class="input"></td>
            <td class="td">
              <div class="flex gap-2">
                <button class="btn btn-outline" @click="save(c)">Salvar</button>
                <button class="btn btn-outline" @click="del(c)">Excluir</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
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
