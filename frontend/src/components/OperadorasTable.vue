<template>
  <table border="1" width="100%" cellspacing="0" cellpadding="8">
    <thead>
      <tr>
        <th>CNPJ</th>
        <th>Razão Social</th>
        <th>UF</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="op in operadoras" :key="op.cnpj">
        <td>
          <router-link :to="`/operadoras/${op.cnpj}`">
            {{ op.cnpj }}
          </router-link>
        </td>
        <td>{{ op.razao_social }}</td>
        <td>{{ op.uf }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
defineProps({
  operadoras: {
    type: Array,
    required: true
  }
})
</script>
