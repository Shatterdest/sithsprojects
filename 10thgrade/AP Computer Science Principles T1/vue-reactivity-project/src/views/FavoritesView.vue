<template>
  <div>
    <NavBar />
    <h1 class="title">Favorite Elements!</h1>
    <div v-if="favoriteElements.length > 0">
      <Element
        v-for="element in favoriteElements"
        :key="element.number"
        :element="element"
        @click="openElementView(element.number)"
      />
    </div>
    <p v-else>you have no favorite elements :(</p>
  </div>
</template>

<script setup>
import { favorites } from "../assets/favorites";
import { pTable } from "../assets/table.js";
import router from "../router/index.js";
import Element from "../components/Element.vue";
import NavBar from "../components/NavBar.vue";

const favoriteElements = [];
pTable.elements.forEach((element) => {
  if (favorites.value.includes(element.number)) {
    favoriteElements.push(element);
  }
});

const openElementView = function (i) {
  router.push({ name: "element", params: { number: i } });
};
</script>

<style scoped>
@import url("../assets/base.css");

.button {
  font-size: 2.5rem;
  border: white solid 5px;
  border-radius: 15px;
  margin-bottom: 1rem;
  margin-left: 10rem;
  margin-top: 5rem;
  padding: 1rem 1rem;
  transition: 0.3s all;
  color: rgb(190, 190, 190);
}
.button:hover {
  color: black;
  background-color: white;
  z-index: 500;
}

.title {
  font-size: 3rem;
  color: white;
}
</style>
