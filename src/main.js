import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import Buefy from "buefy";
import vueHeadful from "vue-headful";
import VueI18n from "vue-i18n";
import i18n from "./i18n";


Vue.use(Buefy, {
  defaultIconPack: "fas",
});

Vue.use(VueI18n);
Vue.config.productionTip = false;
Vue.component("vue-headful", vueHeadful);

new Vue({
  router,
  i18n,
  render: h => h(App)
}).$mount("#app");
