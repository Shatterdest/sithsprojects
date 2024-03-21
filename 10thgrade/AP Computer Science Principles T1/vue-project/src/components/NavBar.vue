<template>
  <div class="nav-container">
    <router-link class="button" to="/">Home</router-link>
    <router-link class="button" to="/favorites">Favorites</router-link>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
const router = useRouter();


</script>

<style lang="css" scoped>
.nav-container {
  display: block;
  padding: 0 0;
  margin: 0 0;
}
.button {
  color: white;
  font-size: 2rem;
  transition: 0s all;
}

.button:hover {
  color: black;
  background-color: white;
}
</style>
