<template>
  <div style="margin-top: 16px">
    <button
      :disabled="page === 1"
      @click="$emit('change', page - 1)"
    >
      Anterior
    </button>

    <span style="margin: 0 12px">
      Página {{ page }}
    </span>

    <button
      :disabled="page * limit >= total"
      @click="$emit('change', page + 1)"
    >
      Próxima
    </button>
  </div>
</template>

<script setup>
defineProps({
  page: Number,
  limit: Number,
  total: Number
})
</script>
