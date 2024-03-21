import { createRouter, createWebHistory } from "vue-router";
import ElementView from "../views/ElementView.vue";
import Table from "../components/Table.vue"
import FavoritesView from "../views/FavoritesView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", name: "table", component: Table },
    {
      path: "/element/:number",
      name: "element",
      component: ElementView,
    },{
      path: "/favorites",
      name:"favorites",
      component: FavoritesView
    }
  ],
});

export default router;
