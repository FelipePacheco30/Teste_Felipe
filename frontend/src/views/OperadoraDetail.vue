<template>
  <section>
    <p v-if="loading">Carregando...</p>
    <p v-if="error">{{ error }}</p>

    <div v-if="operadora">
      <h2>{{ operadora.razao_social }}</h2>
      <p><strong>CNPJ:</strong> {{ operadora.cnpj }}</p>
      <p><strong>UF:</strong> {{ operadora.uf }}</p>

      <h3>Despesas por UF</h3>
      <DespesasChart :dados="despesas" />
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'
import DespesasChart from '../components/DespesasChart.vue'

const props = defineProps({
  cnpj: {
    type: String,
    required: true
  }
})

const operadora = ref(null)
const despesas = ref([])
const loading = ref(false)
const error = ref(null)

onMounted(async () => {
  loading.value = true
  try {
    operadora.value = (await api.getOperadora(props.cnpj)).data
    despesas.value = (await api.getDespesas(props.cnpj)).data
  } catch (err) {
    error.value = err
  } finally {
    loading.value = false
  }
})
</script>
