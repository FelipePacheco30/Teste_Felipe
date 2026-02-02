import { createRouter, createWebHistory } from 'vue-router'
import OperadorasList from '../views/OperadorasList.vue'
import OperadoraDetail from '../views/OperadoraDetail.vue'

const routes = [
  {
    path: '/',
    name: 'operadoras',
    component: OperadorasList
  },
  {
    path: '/operadoras/:cnpj',
    name: 'operadora-detalhe',
    component: OperadoraDetail,
    props: true
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
