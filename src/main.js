import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { axiosPlugin } from './api/index.js'

const app = createApp(App);
app.use(axiosPlugin)
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
app.use(ElementPlus);

app.use(router);

app.mount('#app');