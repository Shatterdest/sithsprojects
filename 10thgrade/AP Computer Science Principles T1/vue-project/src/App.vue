<script setup>
import { pTable as table } from "./assets/table.js";
import Table from "./components/Table.vue";
import router from "./router";
</script>

<template>
  <div>
<router-view :table="table"/>    
  </div>
</template>

<style scoped>
.table {
  margin: 0 0 0 0;
}
</style>
