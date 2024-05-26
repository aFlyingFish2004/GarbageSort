import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { axiosPlugin } from './api/index.js'
// 我的
import tabBar from './pages/public_component/tabBar.vue'

const app = createApp(App);
app.use(axiosPlugin)
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
app.use(ElementPlus);

app.use(router);

// 我的
app.component("tabBar", tabBar)

app.mount('#app');