<template>
  <section>
    <input
      v-model="search"
      placeholder="Buscar por Razão Social ou CNPJ"
    />
    <button @click="load()">Buscar</button>

    <p v-if="loading">Carregando...</p>
    <p v-if="error">{{ error }}</p>

    <OperadorasTable :operadoras="operadoras" />

    <Pagination
      :page="meta.page"
      :limit="meta.limit"
      :total="meta.total"
      @change="changePage"
    />
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useOperadoras } from '../composables/useOperadoras'
import OperadorasTable from '../components/OperadorasTable.vue'
import Pagination from '../components/Pagination.vue'

const search = ref('')
const { operadoras, loading, error, meta, fetchOperadoras } = useOperadoras()

function load(page = 1) {
  fetchOperadoras({
    page,
    search: search.value
  })
}

function changePage(page) {
  load(page)
}

onMounted(() => load())
</script>
