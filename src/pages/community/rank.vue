<script setup>
import { useRouter } from 'vue-router';
import { reactive, ref, onMounted } from 'vue';
import axios from 'axios';
import { fetchImage, fetchMessage } from '@/api/api';

import backIcon from '@/images/xiyang098/a0826ba5fc994a76749cd5cb2d23b553.png';
import flashIcon1 from '@/images/xiyang098/21c156ae6b1a260a46a962dcbc812923.png';
import flashIcon2 from '@/images/xiyang098/a2905898fecb1d55de08e853b81b4bb2.png';
import medalGold from '@/images/xiyang098/5f1e6d5d26580e087eb10e58fa55f044.png';
import medalSilver from '@/images/xiyang098/9c38658efe1093c625626f0eca4d6bd1.png';
import medalBronze from '@/images/xiyang098/17c22384c7704bf8632c3e669a02f599.png';

const data = reactive({
  items: [null, null, null, null, null, null, null],
  rank: [
    {
      avatarUrl: '/src/images/xiyang098/32bffa27f862e68b6bd6505f0693d1de.png',
      nickName: 'aFlyingFish',
      score: 5000
    },
    // more items...
  ]
});

const router = useRouter();
const goBack = () => {
  router.back();
};

const userInfo = ref(null);

axios.get('https://garbage.sa1ge.ink/main/userInfo/')
  .then(response => {
    userInfo.value = response.data;
    console.log(userInfo.value);
  })
  .catch(error => {
    console.error(error);
  });

const email = ref(localStorage.getItem('userEmail') || '');  
const myInfo = ref({});
let userRank = 1; // 排名通常从1开始  
const avatar_url = ref('');
const avatar = ref('');

async function fetchUserMessage() {
  try {
    const response = await fetchMessage(email.value);
    avatar_url.value = response.data.avatar_url;
  } catch (error) {
    console.error('Failed to fetch user name:', error);
  }
}

const fetchAndDisplayImage = async (imageName) => {
  try {
    const response = await fetchImage(imageName);
    const blob = await response.data;
    return URL.createObjectURL(blob);
  } catch (error) {
    console.error('Error fetching image:', error);
  }
};

onMounted(async () => {
  try {
    const response = await axios.get(`https://garbage.sa1ge.ink/main/get-by-email/${email.value}/`);
    myInfo.value = response.data;
    
    await fetchUserMessage();
    avatar.value = await fetchAndDisplayImage(avatar_url.value);

    userInfo.value.forEach(async(user) => {
      try {
        const avatarData = await fetchAndDisplayImage(user.avatar_url);
        user.avatar = avatarData;
      } catch (error) {
        console.error(`Error fetching avatar for ${user.user_name}:`, error);
      }
    });

    const targetUserName = myInfo.value.user_name;

    for (const user of userInfo.value) {
      if (user.user_name === targetUserName) {
        break;
      }
      userRank++;
    }
  } catch (error) {
    console.error('Error fetching user info:', error);
  }
});
</script>

<template>
  <div class="page">
    <div class="top">
      <img class="back" @click="goBack" :src="backIcon" alt="back">
      <div class="title">积分榜</div>
      <img class="flash1" :src="flashIcon1" alt="flash1">
      <img class="flash2" :src="flashIcon2" alt="flash2">
    </div>
    <div class="rank-item myrank">
      <div class="left">
        <div class="rank" v-if="userRank === 1"><img :src="medalGold" alt="medal" class="medal"></div>
        <div class="rank" v-else-if="userRank === 2"><img :src="medalSilver" alt="medal" class="medal"></div>
        <div class="rank" v-else-if="userRank === 3"><img :src="medalBronze" alt="medal" class="medal"></div>
        <div class="rank" v-else>{{ userRank }}</div>
        <div class="user">
          <img :src="avatar" alt="avatar" class="avatar">
          <p class="nickName">{{ myInfo.user_name }}</p>
        </div>
      </div>
      <p class="right">{{ myInfo.score }}<span> 分</span></p>
    </div>
    <div class="rank-list">
      <div class="rank-item" v-for="(item, index) in userInfo" :key="index">
        <div class="left">
          <div class="rank" v-if="index + 1 === 1"><img :src="medalGold" alt="medal" class="medal"></div>
          <div class="rank" v-else-if="index + 1 === 2"><img :src="medalSilver" alt="medal" class="medal"></div>
          <div class="rank" v-else-if="index + 1 === 3"><img :src="medalBronze" alt="medal" class="medal"></div>
          <div class="rank" v-else>{{ index + 1 }}</div>
          <div class="user">
            <img :src="item.avatar" alt="avatar" class="avatar">
            <p class="nickName">{{ item.user_name }}</p>
          </div>
        </div>
        <p class="right">{{ item.score }} <span>分</span></p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page {
  background-color: #ffffff;
  width: 100%;
  height: 100%;
  overflow-y: auto;
}

.top {
  position: relative;
  width: 100%;
  height: 15vw;
  text-align: center;
  line-height: 15vw;
  border-bottom: solid 0.509vw #e0e0e033;
  background-color: #fff;
}

.back {
  position: absolute;
  left: 5vw;
  top: 50%;
  transform: translateY(-50%);
  width: 3.562vw;
  height: 2.799vw;
}

.title {
  font-size: 6.616vw;
  font-family: STLiti;
}

.flash1 {
  position: absolute;
  left: 50%;
  top: 0;
  transform: translate(-50%, 1vw);
  mix-blend-mode: screen;
  width: 31.807vw;
  height: 8.397vw;
  animation: moveRight 1s ease-out;
}

.flash2 {
  position: absolute;
  right: 30.534vw;
  bottom: 0;
  transform: translate(2vw, -2vw);
  mix-blend-mode: screen;
  width: 37.405vw;
  height: 8.397vw;
  animation: moveLeft 1s ease-out;
}

@keyframes moveRight {
  from {
    transform: translate(calc(-50% - 15vw), 1vw);
  }
  to {
    transform: translate(-50%, 1vw);
  }
}

@keyframes moveLeft {
  from {
    transform: translate(calc(2vw + 15vw), -2vw);
  }
  to {
    transform: translate(2vw, -2vw);
  }
}

.rank-item {
  padding: 0 5vw 3vw;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 5.089vw;
  font-family: DM Sans;
  color: #000000;
}

.myrank {
  border-bottom: solid 0.509vw #e0e0e033;
  padding-top: 2vw;
  padding-bottom: 2vw;
  margin-bottom: 2vw;
}

.rank-item .left {
  display: flex;
  align-items: center;
}

.left .rank {
  text-align: center;
  width: 10vw;
  margin-right: 5vw;
}

.left .user {
  display: flex;
  align-items: center;
}

.left .user .avatar {
  border-radius: 50%;
  width: 12.468vw;
  height: 12.468vw;
  margin-right: 5vw;
}

.rank-item .right span {
  font-size: 3.562vw;
  font-family: DM Sans;
  line-height: 3.226vw;
  color: #999999;
}

.medal {
  width: 8.906vw;
  height: 10.941vw;
}
</style>
