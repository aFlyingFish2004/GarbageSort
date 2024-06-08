<script setup>
import { useRouter } from 'vue-router';
import { ref, reactive, onMounted } from 'vue';
import globalState from '@/globalState';
import { fetchMessage, fetchImage } from '@/api/api';

const props = defineProps({});
const data = reactive({});
const router = useRouter();

//用户相关数据
const search = ref('')
const email = ref(localStorage.getItem('userEmail') || ''); // 从LocalStorage获取email
const name = ref('aFlyingFish')
const avatar_url = ref('')
const avatar = ref('')

const flag = ref(true);
function handleAnimationEnd() {
  flag.value = false; // 将flag设置为false
  console.log('Animation ended, flag is now', flag.value);
}


async function fetchUserMessage() {
  try {
    const response = await fetchMessage(email.value);
    name.value = response.data.name;
    avatar_url.value = response.data.avatar_url;
  } catch (error) {
    console.error('Failed to fetch user name:', error);
  }
}

const fetchAndDisplayImage = async (imageName) => {
  try {
    const response = await fetchImage(imageName);
    const blob = await response.data;
    avatar.value = URL.createObjectURL(blob);
  } catch (error) {
    console.error('Error fetching image:', error);
  }
};

function onClick() {
  router.push({ name: 'photograph' });
}

function onClick_1() {
  router.push({ name: 'photograph' });
}

function onClick_2() {
  router.push({ name: 'my' });
}

function toVoice() {
    router.push({ name: 'voice' })
  }

onMounted(async () => {
  await fetchUserMessage();
  fetchAndDisplayImage(avatar_url.value);
});

</script>

<template>
  <div class="animation" v-if="flag">
    <div class="circle"></div>
    <div class="sector" @animationend="handleAnimationEnd"></div>
    <div class="sector2"></div>
    <img src="../../images/xiyang098/logo.png" alt="" class="logo">
  </div>
  <div class="flex-col justify-start page" v-else>
    <div class="flex-col group">
      <div class="flex-row items-center header">
        <img class="image" src="../../images/92170897a875bf4e6e60e123fe08ea17.png" />
        <input class="ml-12 text" type="text" v-model="search" placeholder="在这里搜索你想要的..." />
      </div>
      <div class="flex-row justify-between items-center group_2">
        <div class="flex-row items-center">
          <img class="image_2" :src="avatar" />
          <div class="flex-col items-start ml-19">
            <span class="font text_2">{{ name }}</span>
            <span class="mt-4 font text_3">早上好！</span>
          </div>
        </div>
        <div class="flex-col group_3">
          <img class="self-center image_3" src="../../images/6ac87c46c356f5d69f34d8bdd1b04c6e.png" />
          <span class="mt-8 self-start text_4">消息中心</span>
        </div>
      </div>
      <div class="flex-col mt-34">
        <div class="flex-row equal-division">
          <img class="checkbox image_1" src="../../images/a02a325d89c0f2d00b5f701664f6382b.png" @click="onClick" />
          <img class="ml-14 checkbox image_6" src="../../images/7cd2245d3c9c648c4c9242211d42d741.png" @click="toVoice" />
        </div>
        <div class="mt-20 flex-col self-stretch group_1">
          <img class="image_8" src="../../images/9164f859c8aac716b404ad7d27ebbd53.png" />
          <div class="mt-32 flex-col group_13">
            <div class="flex-col list">
              <div class="flex-row relative section_2">
                <span class="font_4 pos_2">垃圾分类新规</span>
                <span class="font_5 text_8 pos_6">本文介绍了垃圾分类的最新国标</span>
                <div class="flex-row group_16 pos_3">
                  <div class="flex-col justify-start text-wrapper_2"><span class="font_6 text_9">Trending</span></div>
                  <div class="ml-6 flex-col justify-start text-wrapper_2">
                    <span class="font_6 text_1">Policy</span>
                  </div>
                </div>
                <img class="image_9 pos_1" src="../../images/e0d7f39e39b796b15d6b739b7a3429fd.png" />
              </div>
              <div class="flex-col items-start relative section_3 mt-29">
                <span class="font_4 text_18">厨余垃圾，你分对了吗？</span>
                <span class="font_5 text_10">本文介绍了判断厨余垃圾的一般方法</span>
                <div class="flex-row group_14">
                  <div class="flex-col justify-start shrink-0 text-wrapper_2">
                    <span class="font_6 text_19">Trending</span>
                  </div>
                  <div class="ml-6 flex-col justify-start flex-1 text-wrapper_2">
                    <span class="font_6 text_17">Technology</span>
                  </div>
                </div>
                <img class="image_9 pos" src="../../images/859d3a2c0a7b2e3dc1cf0db4b5c24827.png" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 底部导航栏 -->
    <tabBar :select="0" />
  </div>
</template>

<style scoped lang="css">
/* 扇形样式 */
.sector {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translateY(-100%);
  width: 12vw;
  height: 12vw;
  border-radius: 0 100px 0 0;
  background-color: #e0e0e0;

  animation: spin 3s;
  /* 应用动画 */
}

.sector2 {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translateY(-100%);
  width: 12vw;
  height: 12vw;
  border-radius: 0 100px 0 0;
  background-color: #e0e0e0;

  animation: spin 2s infinite;
  /* 应用动画 */
}


/* 定义旋转动画 */
@keyframes spin {
  0% {
    transform-origin: bottom left;
    /* 旋转的基点在底部左侧，即扇形的顶点 */
    transform: translateY(-100%) rotate(0deg);
  }

  50% {
    transform-origin: bottom left;
    /* 旋转的基点在底部左侧，即扇形的顶点 */
    transform: translateY(-100%) rotate(360deg);
  }

  100% {
    transform-origin: bottom left;
    transform: translateY(-100%) rotate(720deg);
    /* 旋转720度，即两圈 */
  }
}

.circle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 24vw;
  height: 24vw;
  border-radius: 50%;
  background-color: #f3f3f3;
  /* border: 0.2vw solid #bdbdbd; */
}

.logo {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 20vw;
  height: 20vw;
  background-color: #fff;
  border-radius: 50%;
  border: 0.2vw solid #bdbdbd;
  animation: none;
}



input {
  border: none;
  background: none;
  padding: 0;
  width: 60vw;
}

input:focus {
  outline: none;
}

input::placeholder {
  color: #888
}

input:focus::placeholder {
  color: transparent;
}

.ml-19 {
  margin-left: 4.835vw;
}

.mt-29 {
  margin-top: 7.379vw;
}

.mt-37 {
  margin-top: 9.415vw;
}

.page {
  padding-bottom: 5.412vw;
  background-color: #fff;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;
}

.group {
  padding-bottom: 12.468vw;
  overflow-y: auto;
}

.header {
  margin-left: 24.173vw;
  margin-right: 6.87vw;
  margin-top: 5.598vw;
  align-self: auto;
  background-color: hsla(0, 0%, 85.1%, 0);
  border-radius: 2.036vw;
  border: .254vw solid #b7afaf;
  padding-top: 1.908vw;
  padding-bottom: 1.908vw;
  padding-left: 3.562vw;
}

.image {
  width: 3.817vw;
  height: 4.071vw;
}

.text {
  color: #888;
  font-size: 3.308vw;
  font-family: Inter;
  line-height: 3.084vw;
}

.group_2 {
  margin-top: 3.817vw;
  padding: 0 6.616vw;
}

.image_2 {
  border-radius: 50%;
  width: 13.995vw;
  height: 13.995vw;
}

.font {
  font-size: 4.58vw;
  font-family: Inter;
  line-height: 4.321vw;
  color: #000;
}

.text_2 {
  font-weight: 100;
}

.text_3 {
  margin-left: .298vw;
  line-height: 4.219vw;
}

.group_3 {
  margin-right: 2.545vw;
  width: 15.394vw;
}

.image_3 {
  width: 6.107vw;
  height: 6.616vw;
}

.text_4 {
  margin-left: 1.781vw;
  color: #000;
  font-size: 3.053vw;
  font-family: Poppins;
  line-height: 2.799vw;
}

.equal-division {
  align-self: center;
}

.checkbox {
  width: 39.695vw;
  height: 19.847vw;
}

.image_1 {
  margin-left: 3.562vw;
  margin-right: 2.799vw;
}

.image_6 {
  margin-right: 2.799vw;
}

.group_1 {
  padding-top: 2.417vw;
}

.image_8 {
  margin-top: 3.817vw;
  border-radius: 4.835vw;
  width: 100vw;
  height: 36.6412vw;
}

.group_13 {
  padding-bottom: 3.069vw;
}

.list {
  padding-left: 8.651vw;
  padding-right: 7.888vw;
}

.section_2 {
  padding-left: 2.036vw;
  background-color: #f2fbf5;
  border-radius: 1.272vw;
  height: 24.936vw;
}

.font_4 {
  font-size: 5.089vw;
  font-family: Ubuntu;
  line-height: 4.702vw;
  color: #000;
}

.pos_2 {
  position: absolute;
  left: 2.204vw;
  top: 3.364vw;
}

.font_5 {
  font-size: 3.053vw;
  font-family: Ubuntu;
  line-height: 2.835vw;
  color: #000;
}

.text_8 {
  font-size: 3.308vw;
  line-height: 3.074vw;
}

.pos_6 {
  position: absolute;
  left: 2.135vw;
  top: 50%;
  transform: translateY(-50%);
}

.group_16 {
  width: 46.664vw;
}

.pos_3 {
  position: absolute;
  left: 2.036vw;
  top: 19.847vw;
}

.font_6 {
  font-size: 2.545vw;
  font-family: Ubuntu;
  line-height: 2.453vw;
  color: #000;
}

.text_9 {
  margin-left: 1.059vw;
  margin-right: .468vw;
}

.text-wrapper_2 {
  padding: .316vw 0 .285vw;
  background-color: rgba(0, 0, 0, .0784313725490196);
  border-radius: 1.272vw;
  height: 3.053vw;
}

.text_1 {
  margin-left: 1.237vw;
  margin-right: .29vw;
}

.image_9 {
  border-radius: 1.272vw;
  width: 26.718vw;
  height: 24.936vw;
}

.pos_1 {
  position: absolute;
  right: 0;
  bottom: 0;
}

.section_3 {
  padding: 2.85vw 2.036vw 2.036vw;
  background-color: #f2fbf5;
  border-radius: 1.272vw;
}

.text_18 {
  line-height: 4.819vw;
}

.text_10 {
  margin-top: 3.28vw;
  font-size: 3.308vw;
  line-height: 3.087vw;
}

.group_14 {
  margin-top: 5.812vw;
  width: 29.262vw;
}

.text_19 {
  margin-left: 1.059vw;
  margin-right: .468vw;
}

.text_17 {
  margin-left: 1.059vw;
  margin-right: .468vw;
}

.pos {
  position: absolute;
  right: 0;
  bottom: 0;
}

.group_15 {
  padding: 0 4.186vw;
}

.group_6 {
  flex: 1 1 18.272vw;
}

.group_7 {
  padding: 1.02vw 0 1.511vw;
}

.image_10 {
  width: 6.399vw;
  height: 6.399vw;
}

.font_7 {
  font-size: 3.053vw;
  font-family: Roboto;
  line-height: 2.835vw;
  color: #b9bcbe;
}

.text_12 {
  color: #00b140;
  line-height: 2.807vw;
}

.group_8 {
  padding: 1.02vw 0 1.501vw;
}

.text_14 {
  line-height: 2.83vw;
}

.group_9 {
  padding: 1.018vw 0 1.506vw;
}

.text_15 {
  line-height: 2.822vw;
}

.group_10 {
  padding: 1.02vw 0 1.517vw;
}

.text_16 {
  line-height: 2.812vw;
}

.group_11 {
  padding: 1.018vw 0 1.509vw;
}
</style>