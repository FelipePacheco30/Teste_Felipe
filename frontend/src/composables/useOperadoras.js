import { ref } from 'vue'
import api from '../services/api'

export function useOperadoras() {
  const operadoras = ref([])
  const loading = ref(false)
  const error = ref(null)

  const meta = ref({
    page: 1,
    limit: 10,
    total: 0
  })

  async function fetchOperadoras(params) {
    loading.value = true
    error.value = null

    try {
      const { data } = await api.getOperadoras(params)
      operadoras.value = data.data
      meta.value = data.meta
    } catch (err) {
      error.value = err
    } finally {
      loading.value = false
    }
  }

  return {
    operadoras,
    loading,
    error,
    meta,
    fetchOperadoras
  }
}
