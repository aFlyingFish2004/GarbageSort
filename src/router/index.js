import { createRouter, createWebHistory } from 'vue-router';
import Log_in from '../pages/log_in/log_in.vue';
import Feedback from '../pages/feedback/feedback.vue';
import Photograph from '../pages/photograph/photograph.vue';
import Home from '../pages/home/home.vue';
import Recognize_result from '../pages/recognize_result/recognize_result.vue';
import Account from '../pages/account/account.vue';
import My from '../pages/my/my.vue';
import Sign_up from '../pages/sign_up/sign_up.vue';
import My_model from '../pages/my_model/my_model.vue';

//
import community from '../pages/community/community.vue';
import search from '../pages/search/search.vue';
import voice from '../pages/voice/voice.vue';
import rank from '../pages/community/rank.vue';
import achivement from '../pages/community/achivement.vue';
import comment from '../pages/comment/comment.vue';

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
  {
    path:'/my_model',
    name:'my_model',
    component:My_model,
  },
  {
    path: '/community',
    name: 'community',
    component: community,
  },
  {
    path: '/search',
    name: 'search',
    component: search,
  },
  {
    path: '/voice',
    name: 'voice',
    component: voice,
  },
  {
    path: '/rank',
    name: 'rank',
    component: rank,
  },
  {
    path: '/achievement',
    name: 'achivement',
    component: achivement,
  },
  {
    path: '/comment',
    name: 'comment',
    component: comment,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;