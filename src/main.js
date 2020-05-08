import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import Buefy from "buefy";
import VueI18n from "vue-i18n";
import i18n from "./i18n";
import Meta from "vue-meta";
import "./registerServiceWorker";

Vue.use(Buefy, {
  defaultIconPack: "fas"
});

Vue.use(VueI18n);
Vue.config.productionTip = false;
Vue.use(Meta);

new Vue({
  router,
  i18n,
  render: h => h(App)
}).$mount("#app");
