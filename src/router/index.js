import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/services",
    name: "Services",
    component: () => import("../views/Services.vue")
  },
  {
    path: "/libraries",
    name: "Libraries",
    component: () => import("../views/Libraries.vue")
  }
];

const router = new VueRouter({
  routes
});

export default router;
