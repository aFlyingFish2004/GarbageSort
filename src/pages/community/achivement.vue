<script setup>
import { useRouter } from 'vue-router';
import { reactive, onMounted, ref } from 'vue';
import axios from 'axios';

const data = reactive({
  items: [
    {
      url: '/src/images/xiyang098/96b01197c75773f6887c459149ea6e4b.png', 
      date: '2024.3.22',
      score: 100
    },
    {
      url: '/src/images/xiyang098/cc6a0475f9369ed4cf8407b75672d1f9.png',
      date: '2024.3.30',
      score: 500
    },
    {
      url: '/src/images/xiyang098/f07bec031843797f8179d410895d74b3.png', 
      date: '2024.4.15',
      score: 1000
    },
    {
      url: '/src/images/xiyang098/d2aae0de609478ffef63d38b76eaeee6.png', 
      date: '2024.5.3',
      score: 5000
    },
    {
      url: '/src/images/xiyang098/3133f5cd54c6626dce43099a0ece7ea2.png', 
      date: '2024.5.25',
      score: 10000
    }
  ]
    
});

const router = useRouter();
const goBack = () => {  
  router.back();  
}; 


const email = ref(localStorage.getItem('userEmail') || '');  
const myInfo = ref({})

onMounted(async () => {
  try {
    // console.log(111);
    const response = await axios.get(`https://10.122.210.57:8000/main/get-by-email/${email.value}/`)  // 发送GET请求到Django视图  
    myInfo.value = response.data  // 将返回的用户信息存储在响应式引用中 

  } catch (error) {
    console.error('Error fetching user info:', error)
  }
})


</script>

<template>
<div class="flex-col page">
  <div class="flex-col flex-1 group">
    <div class="flex-row items-center group_2">
      <img class="image" @click="goBack" src="../../images/xiyang098/a0826ba5fc994a76749cd5cb2d23b553.png" />
      <span class="text ml-126">成就勋章</span>
    </div>
    <div class="flex-col group_3">
      <div class="flex-col group_4">
        <div class="flex-col justify-start items-center self-stretch relative group_5">
          <span class="text_2">环保卫士</span>
          <img class="image_2 pos" src="../../images/xiyang098/21c156ae6b1a260a46a962dcbc812923.png" />
          <img class="image_3 pos_2" src="../../images/xiyang098/a2905898fecb1d55de08e853b81b4bb2.png" />
        </div>
        <div class="mt-4 self-center group_6">
          <span class="font text_3">累计</span>
          <span class="font text_4">{{ myInfo.score }}</span>
          <span class="font">积分</span>
        </div>
      </div>
      <div class="flex-col group_7 mt-25">
        <div class="flex-col">
          <div class="flex-row medal" v-for="(item, index) in data.items" :key="index">
            <img class="shrink-0 image_4" :src='item.url' :style="{filter: myInfo.score > item.score ? '' : 'grayscale(100%)'}"/>
            <div class="ml-28 flex-col flex-1 section"  :style="{backgroundColor: myInfo.score > item.score ? '' : '#e0e0e0'}">
              <span class="self-end font_2" v-if="myInfo.score > item.score">{{ item.date }}达成</span>
              <span class="self-end font_2" v-else>未达成</span>
              <div class="mt-12 self-start">
                <span class="font_3 text_5" :style="{color: myInfo.score > item.score ? '' : '#808080'}">{{ item.score }}</span>
                <span class="font">积分</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped lang="css">
.ml-126 {
  margin-left: 32.061vw;
}
.mt-25 {
  margin-top: 6.361vw;
}
.ml-33 {
  margin-left: 8.397vw;
}
.page {
  background-color: #ffffff;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;
}
.header {
  background-image: url('../../images/xiyang098/5f75d39751dd7fc3326ebb162726d3fa.png');
  background-position: 0% 0%;
  background-size: 100%, 100%;
  background-repeat: no-repeat;
  height: 11.705vw;
}
.group {
  overflow-y: auto;
}
.group_2 {
  padding: 7.125vw 8.651vw;
  border-bottom: solid 0.509vw #e0e0e033;
}
.image {
  width: 3.562vw;
  height: 2.799vw;
}
.text {
  color: #181d27;
  font-size: 3.562vw;
  font-family: DM Sans;
  line-height: 3.303vw;
}
.group_3 {
  margin-bottom: -21.12vw;
}
.group_4 {
  padding-top: 3.053vw;
}
.group_5 {
  padding: 3.053vw 0;
}
.text_2 {
  color: #000000;
  font-size: 6.616vw;
  font-family: STLiti;
  line-height: 4.453vw;
}

/* 两张 flash 图片 */
.image_2 {
  mix-blend-mode: SCREEN;
  width: 31.807vw;
  height: 8.397vw;

  animation: moveRight 1s ease-out;
}
.pos {
  position: absolute;
  left: 50%;
  top: 0;
  transform: translateX(-50%);
}
.image_3 {
  mix-blend-mode: SCREEN;
  width: 37.405vw;
  height: 8.397vw;

  animation: moveLeft 1s ease-out;
}
.pos_2 {
  position: absolute;
  right: 30.534vw;
  bottom: 0;
}

@keyframes moveRight {
  from {
    transform: translateX(calc(-50% - 20vw));
  }

  to {
    transform: translateX(-50%);
  }
}

@keyframes moveLeft {
  from {
    transform: translateX(20vw);
  }

  to {
    transform: translateX(0);
  }
}



.group_6 {
  line-height: 2.972vw;
}
.font {
  font-size: 3.053vw;
  font-family: Microsoft YaHei;
  line-height: 2.972vw;
  color: #666666;
}
.text_3 {
  line-height: 2.921vw;
}
.text_4 {
  color: #00b140;
  line-height: 2.399vw;
}
.group_7 {
  padding: 7.888vw 7.888vw 0;
  border-top: solid 0.509vw #e0e0e033;
}
.image_4 {
  width: 20.611vw;
  height: 20.611vw;
}
.section {
  margin-right: 3.562vw;
  padding: 2.545vw 3.053vw 5.089vw 5.089vw;
  background-color: #f8faf9;
  height: 20.611vw;
}
.font_2 {
  font-size: 3.053vw;
  font-family: STKaiti;
  line-height: 2.654vw;
  color: #666666;
}
.font_3 {
  font-size: 8.651vw;
  font-family: Microsoft YaHei;
  line-height: 6.656vw;
  color: #00b140;
}
.text_5 {
  line-height: 6.687vw;
}
.group_12 {
  padding: 0 1.018vw;
}
.image_5 {
  width: 18.575vw;
  height: 21.374vw;
}
.section_4 {
  margin-right: 2.29vw;
  margin-bottom: 0.763vw;
  background-color: #f8faf9;
  height: 20.611vw;
}

.medal {
  margin-bottom: 10vw;
}



</style>