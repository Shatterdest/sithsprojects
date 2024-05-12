<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { fetchData } from './stores/store'
import { usedata as data } from './stores/store';
import { onBeforeMount } from 'vue';

onBeforeMount(() => {
  fetchData('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm')
})
</script>

<template>
  <h1 class="title">Graph API Project</h1>
  <header>
    <div class="wrapper flex flex-row justify-center m-auto w-full">
      <nav class="flex justify-center m-auto">
        <button class="mr-10 bg-slate-300 border-2 border-black hover:bg-slate-600 hover:text-gray-50">
          <RouterLink to="/" class=" ">Home</RouterLink>
        </button>

        <button class="bg-slate-300 border-2 border-black hover:bg-slate-600 hover:text-gray-50">
          <RouterLink to="/graphs" class="]"> Graph 1</RouterLink>
        </button>
        <button class="bg-slate-300 border-2 border-black hover:bg-slate-600 hover:text-gray-50">
          <RouterLink to="/graphTwo" class="]"> Graph 2</RouterLink>
        </button>
      </nav>
    </div>
  </header>
  <RouterView :data="data"/>
</template>

<style scoped>
.title {
  font-size: 5rem;
  text-align: center;
}

</style>
