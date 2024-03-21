<template>
  <div class="main">
    <NavBar />
    <h1 class="title">The Periodic Table of Vuelements</h1>
    <section id="periodic-table">
      <Element
        v-for="element in elements"
        :key="element.number"
        :element="element"
        :style="{ 'grid-column': element.xpos, 'grid-row': element.ypos }"
        @click="openElementView(element.number)"
      />
    </section>
  </div>
</template>

<script setup>
import Element from "./Element.vue";
import { useRouter } from "vue-router";
import { favorites } from "../assets/favorites.js";
import NavBar from "./NavBar.vue";

const props = defineProps(["table"]);
const table = props.table;
const elements = table.elements;

const router = useRouter();

const openElementView = function (i) {
  router.push({ name: "element", params: { number: i } });
};
</script>

<style lang="css" scoped>

.main {
  height: 100vh;
  width: 100vw;
}

.title {
  font-size: 5vw;
  color: white;
  text-align: center;
  margin-right: 10%;
}
#periodic-table {
  display: grid;
  grid-template-columns: repeat(18, auto) 1fr;
  gap: 0.1vw;
  margin: 0;
  top: 50%;
  left: 50%;
}
</style>
