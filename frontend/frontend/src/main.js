import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementPlus from "element-plus";
import "../node_modules/element-plus/dist/index.css";

createApp(App).use(store).use(router).use(ElementPlus).mount("#app");
