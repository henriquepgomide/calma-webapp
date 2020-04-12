import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import Buefy from "buefy";
import vueHeadful from "vue-headful";

Vue.use(Buefy);
Vue.config.productionTip = false;
Vue.component("vue-headful", vueHeadful);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
