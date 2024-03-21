<script setup>
import { useRoute } from "vue-router";
import { favorites } from "../assets/favorites.js";
import { ref } from "vue";
import NavBar from "../components/NavBar.vue";

const route = useRoute();

const props = defineProps(["table"]);
const table = props.table;
const element = table.elements[route.params.number - 1];
const favorited = ref(false);

if (favorites.value.includes(element.number)) {
  favorited.value = true;
} else {
  favorited.value = false;
}

const toggleFavorite = function () {
  if (favorites.value.includes(element.number)) {
    favorites.value.splice(favorites.value.indexOf(element.number), 1);
    console.log(favorites.value);
    favorited.value = false;
  } else {
    favorites.value.push(element.number);
    console.log(favorites.value);
    favorited.value = true;
  }
};
</script>

<template>
  <div class="container">
    <NavBar />
    <div class="title-container">
      <h1 class="title">{{ element.name }}, #{{ element.number }}</h1>
      <button v-if="favorited" class="button" @click="toggleFavorite()">
        Favorited!
      </button>
      <button v-else class="button" @click="toggleFavorite()">Favorite!</button>
    </div>
    <!-- <h1>{{ element }}</h1> -->

    <h2>Atomic Mass: {{ element.atomic_mass }}</h2>
    <h2>Appearance: {{ element.appearance }}</h2>
    <h2>Category: {{ element.category }}</h2>
    <h2>Electron configuration: {{ element.electron_configuration }}</h2>
    <h2>Block: {{ element.block.toUpperCase() }}</h2>
    <h2>Description: {{ element.summary }}</h2>
    <img :src="element.bohr_model_image" :alt="element.name" />
  </div>
</template>

<style scoped>


.container {
  height: 100vh;
  width: 100vw;
}
.title {
  font-size: 5rem;
  text-align: center;
  display: inline;
}
.button {
  font-size: 2rem;
  border: var(--color-text) solid 5px;
  border-radius: 15px;
  padding: .5rem 1.5rem;
  transition: 0.3s all;
  color: black;
  margin-left: 3%;
}
.button:hover {
  color: white;
  background-color: var(--color-background);
}

.title-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%
}

img {
  height: auto;
  width: 30vw;
  margin: 1rem auto;
}
</style>
