<template>
  <nav>
    <RouterLink class="button" to="/">Home</RouterLink>
    <RouterLink class="button" to="/graphs">Graphs</RouterLink>
    <button class="button" @click="fetchData('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm')">Refresh Data</button>
  </nav>
</template>

<script setup>
import { fetchData } from '@/stores/store';
</script>

<style lang="css" scoped>

@import url('../assets/base.css');
  nav {
    font-size: 2rem;
  }

  .button {
    color: var(--color-heading);
    transition: 0.5s all;
  }

  .button:hover {
    background-color: var(--color-bg-anti);
    color: var(--color-text-anti)
  }
</style>
