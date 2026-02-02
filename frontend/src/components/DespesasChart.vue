<template>
  <canvas ref="canvas"></canvas>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Chart from 'chart.js/auto'

const props = defineProps({
  dados: {
    type: Array,
    required: true
  }
})

const canvas = ref(null)

onMounted(() => {
  new Chart(canvas.value, {
    type: 'bar',
    data: {
      labels: props.dados.map(d => d.uf),
      datasets: [
        {
          label: 'Total de Despesas',
          data: props.dados.map(d => d.total),
          backgroundColor: '#42b983'
        }
      ]
    }
  })
})
</script>
