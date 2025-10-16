<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <h2 class="text-xl font-semibold text-gray-800">Alunos</h2>
      <form @submit.prevent="add" class="flex gap-3">
        <input v-model="form.name" placeholder="Nome" class="input">
        <input v-model="form.cpf" placeholder="CPF" class="input">
        <input v-model="form.email" placeholder="Email" class="input">
        <button class="btn btn-primary">Adicionar</button>
      </form>
    </div>

    <div class="card overflow-hidden">
      <table class="table">
        <thead class="bg-gray-50">
          <tr>
            <th class="th">ID</th>
            <th class="th">Nome</th>
            <th class="th">CPF</th>
            <th class="th">Email</th>
            <th class="th">Ações</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100 bg-white">
          <tr v-for="s in students" :key="s.id">
            <td class="td">{{ s.id }}</td>
            <td class="td"><input v-model="s.name" class="input"></td>
            <td class="td"><input v-model="s.cpf" class="input"></td>
            <td class="td"><input v-model="s.email" class="input"></td>
            <td class="td">
              <div class="flex gap-2">
                <button class="btn btn-outline" @click="save(s)">Salvar</button>
                <button class="btn btn-outline" @click="del(s)">Excluir</button>
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

const students = ref([])
const form = reactive({ name:'', cpf:'', email:'' })

async function load() {
  const { data } = await API.get('/students/')
  students.value = data
}
async function add() {
  if(!form.name || !form.cpf) return
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
