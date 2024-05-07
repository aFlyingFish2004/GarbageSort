import { createRouter, createWebHistory } from 'vue-router';
import Log_in from '../pages/log_in/log_in.vue';
import Feedback from '../pages/feedback/feedback.vue';
import Photograph from '../pages/photograph/photograph.vue';
import Home from '../pages/home/home.vue';
import Recognize_result from '../pages/recognize_result/recognize_result.vue';
import Account from '../pages/account/account.vue';
import My from '../pages/my/my.vue';
import Sign_up from '../pages/sign_up/sign_up.vue';

const routes = [
  {
    path: '/',
    name: 'log_in',
    component: Log_in,
  },
  {
    path: '/feedback',
    name: 'feedback',
    component: Feedback,
  },
  {
    path: '/photograph',
    name: 'photograph',
    component: Photograph,
  },
  {
    path: '/home',
    name: 'home',
    component: Home,
  },
  {
    path: '/recognize_result',
    name: 'recognize_result',
    component: Recognize_result,
  },
  {
    path: '/account',
    name: 'account',
    component: Account,
  },
  {
    path: '/my',
    name: 'my',
    component: My,
  },
  {
    path: '/sign_up',
    name: 'sign_up',
    component: Sign_up,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;