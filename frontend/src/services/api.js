import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 10000
})

api.interceptors.response.use(
  response => response,
  error => {
    const message =
      error.response?.data?.detail ||
      'Erro inesperado ao comunicar com a API'
    return Promise.reject(message)
  }
)

export default {
  getOperadoras(params) {
    return api.get('/operadoras', { params })
  },

  getOperadora(cnpj) {
    return api.get(`/operadoras/${cnpj}`)
  },

  getDespesas(cnpj) {
    return api.get(`/operadoras/${cnpj}/despesas`)
  },

  getEstatisticas() {
    return api.get('/estatisticas')
  }
}
