<template>
  <div class="min-h-screen flex">
    <!-- Sidebar -->
    <aside class="hidden md:flex w-64 flex-col bg-white border-r border-slate-200">
      <div class="px-5 py-4 border-b border-slate-100">
        <div class="flex items-center gap-2">
          <div class="h-9 w-9 rounded-xl bg-brand-600 grid place-items-center text-white font-bold">ME</div>
          <div>
            <p class="font-semibold">Meu Dia na Escola</p>
            <p class="text-xs text-slate-500">Painel</p>
          </div>
        </div>
      </div>
      <nav class="p-4 space-y-1">
        <RouterLink v-for="item in items" :key="item.to" :to="item.to"
          class="block px-3 py-2 rounded-lg font-medium"
          :class="$route.path===item.to ? 'bg-brand-50 text-brand-700' : 'text-slate-700 hover:bg-slate-50'">
          <component :is="item.icon" class="w-5 h-5 inline-block mr-2 -mt-1" />
          {{ item.label }}
        </RouterLink>
      </nav>
      <div class="mt-auto p-4">
        <button class="btn btn-ghost w-full" @click="$emit('logout')">Sair</button>
      </div>
    </aside>

    <!-- Content -->
    <div class="flex-1 flex flex-col">
      <!-- Topbar -->
      <header class="bg-white border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
          <button class="md:hidden btn btn-ghost" @click="open = !open">Menu</button>
          <h1 class="text-lg font-semibold">{{ title }}</h1>
          <div class="flex items-center gap-3">
            <span class="hidden sm:block text-sm text-slate-600">Admin</span>
            <button class="btn btn-primary" @click="$emit('logout')">Sair</button>
          </div>
        </div>
      </header>

      <main class="max-w-6xl mx-auto w-full p-4 md:p-6">
        <slot />
      </main>
    </div>
  </div>

  <!-- Mobile drawer -->
  <div v-if="open" class="fixed inset-0 bg-black/30 md:hidden" @click="open=false"></div>
  <div v-if="open" class="fixed top-0 left-0 bottom-0 w-72 bg-white p-4 space-y-2 md:hidden">
    <RouterLink v-for="item in items" :key="item.to" :to="item.to"
      class="block px-3 py-2 rounded-lg font-medium"
      :class="$route.path===item.to ? 'bg-brand-50 text-brand-700' : 'text-slate-700 hover:bg-slate-50'"
      @click="open=false">
      <component :is="item.icon" class="w-5 h-5 inline-block mr-2 -mt-1" />
      {{ item.label }}
    </RouterLink>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { HomeIcon, UserGroupIcon, AcademicCapIcon, ClipboardDocumentCheckIcon, ChartBarIcon } from '@heroicons/vue/24/outline'

const route = useRoute()
const open = ref(false)
const map = {
  '/dashboard': 'Dashboard',
  '/students': 'Alunos',
  '/classes': 'Turmas',
  '/attendance': 'Frequência',
  '/grades': 'Notas'
}
const title = computed(() => map[route.path] ?? 'Meu Dia na Escola')

const items = [
  { to: '/dashboard', label: 'Dashboard', icon: HomeIcon },
  { to: '/students',  label: 'Alunos',    icon: UserGroupIcon },
  { to: '/classes',   label: 'Turmas',    icon: AcademicCapIcon },
  { to: '/attendance',label: 'Frequência',icon: ClipboardDocumentCheckIcon },
  { to: '/grades',    label: 'Notas',     icon: ChartBarIcon }
]
</script>
