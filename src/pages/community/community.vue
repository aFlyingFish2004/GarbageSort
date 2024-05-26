<script setup>
import { useRouter } from 'vue-router';
import { ref, reactive, onMounted } from 'vue';
import { fetchMessage, fetchImage } from '@/api/api';

const props = defineProps({});

const data = reactive({
  items: [null, null, null],
});

const router = useRouter();

const email = ref(localStorage.getItem('userEmail') || '')
const name = ref('')
const avatar_url = ref('')
const avatar = ref('')

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

function toRank() {
  router.push({ name: 'rank' });
}

function toAchivement() {
  router.push({ name: 'achivement' });
}

function toComment() {
  router.push({ name: 'comment' });
}

onMounted(async () => {
  await fetchUserMessage();
  fetchAndDisplayImage(avatar_url.value);
});

</script>

<template>
  <div class="flex-col page">

    <div class="flex-col">
      <div class="flex-col flex-1 group">
        <div class="flex-row justify-between items-center group_2">
          <div class="flex-row items-center">
            <img class="image" :src="avatar" />
            <div class="flex-col items-start ml-19">
              <span class="font text">{{ name }}</span>
              <span class="mt-4 font text_2">早上好！</span>
            </div>
          </div>
          <div class="flex-col group_3" @click="toComment">
            <img class="self-center image_2" src="../../images/xiyang098/comment.png" />
            <span class="text_3">论坛</span>
          </div>
        </div>
        <div class="flex-col mt-25">
          <div class="flex-row">
            <div class="flex-col shrink-0 relative section" @click="toRank">
              <div class="flex-col justify-start items-center relative group_4">
                <span class="font_2 text_4">rank</span>
                <img class="image_4 pos_2" src="../../images/xiyang098/c4a82e7741cff9968951711613c80af7.png" />
              </div>
              <div class="flex-col mt-5">
                <div class="flex-row group_6">
                  <img class="image_5" src="../../images/xiyang098/8d5e91c4305a1449b74d60ba378706e3.png" />
                  <img class="image_6 ml-13" src="../../images/xiyang098/a3f43526e03d14366fdae5faf01908c9.png" />
                </div>
                <div class="flex-row items-start group_6 view">
                  <img class="image_7" src="../../images/xiyang098/ec2420b26c4e12f55bdf4c4ce5e83d41.png" />
                  <img class="ml-12 image_6 image_8"
                    src="../../images/xiyang098/2a0bbe7bbb668ca0c6d21f52930b04e1.png" />
                </div>
                <div class="flex-row items-end group_6 view_2">
                  <img class="image_9" src="../../images/xiyang098/f6a332e7aa88223f407fe7c906001fd4.png" />
                  <img class="image_6 ml-13" src="../../images/xiyang098/c8b211476cf0b5fc2ec0009289363a22.png" />
                </div>
              </div>
            </div>
            <div class="ml-20 flex-col flex-1 section_2" @click="toAchivement">
              <div class="flex-col justify-start items-center relative group_5">
                <span class="font_2 text_4 text_5">achievement</span>
                <img class="image_3 pos" src="../../images/xiyang098/bf80d11a15fd0d4799f78f167866b6be.png" />
              </div>
              <div class="grid mt-17">
                <img class="grid-item" src="../../images/xiyang098/96b01197c75773f6887c459149ea6e4b.png" />
                <img class="grid-item" src="../../images/xiyang098/cc6a0475f9369ed4cf8407b75672d1f9.png" />
                <img class="grid-item" src="../../images/xiyang098/f07bec031843797f8179d410895d74b3.png" />
                <img class="grid-item" src="../../images/xiyang098/d2aae0de609478ffef63d38b76eaeee6.png" />
              </div>
            </div>
          </div>



          <div class="mt-20 flex-col list">
            <div class="flex-row items-center mt-20 list-item" v-for="(item, index) in data.items" :key="index">
              <img class="shrink-0 image_10" src="../../images/xiyang098/e681f7d42adbf16897251c2c7c24a5c2.png" />
              <div class="flex-col flex-1 ml-11">
                <span class="font">可回收垃圾处理注意事项</span>
                <div class="flex-row items-baseline group_7 mt-11">
                  <span class="font_3 text_6">chenwen</span>
                  <span class="font_4 text_7 ml-11">2024/4/17</span>
                </div>
                <span class="font_5 mt-11">可回收垃圾里一定要注意这些类别</span>
              </div>
            </div>
          </div>



        </div>
      </div>
      <!-- 底部导航栏 -->
      <tabBar :select="3" />
    </div>
  </div>
</template>

<style scoped lang="css">
.ml-19 {
  margin-left: 4.835vw;
}

.mt-25 {
  margin-top: 6.361vw;
}

.mt-5 {
  margin-top: 1.272vw;
}

.ml-13 {
  margin-left: 3.308vw;
}

.mt-17 {
  margin-top: 4.326vw;
}

.mt-11 {
  margin-top: 2.799vw;
}

.ml-11 {
  margin-left: 2.799vw;
}

.page {
  background-color: #ffffff;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;
  padding-bottom: 20vw;
}

.header {
  background-image: url('../../images/xiyang098/5f75d39751dd7fc3326ebb162726d3fa.png');
  background-position: 0% 0%;
  background-size: 100%, 100%;
  background-repeat: no-repeat;
  height: 11.705vw;
}

.group {
  padding: 8.142vw 5.089vw 0;
  overflow-y: auto;
}

.group_2 {
  padding: 0 2.036vw;
}

.image {
  border-radius: 50%;
  width: 13.995vw;
  height: 13.995vw;
}

.font {
  font-size: 4.58vw;
  font-family: Inter;
  line-height: 4.333vw;
  font-weight: 700;
  color: #000000;
}

.text {
  font-weight: 100;
  line-height: 4.321vw;
}

.text_2 {
  line-height: 4.219vw;
  font-weight: unset;
}

.group_3 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 14.896vw;
  text-align: center;
}

.image_2 {
  width: 6.107vw;
  height: 6.616vw;
}

.text_3 {
  margin-top: 1vw;
  color: #000000;
  font-size: 3.053vw;
  font-family: Poppins;
  line-height: 2.84vw;
}

.section {
  padding: 5.598vw 2.036vw 4.326vw;
  background-color: #8decb499;
  border-radius: 5.089vw;
  box-shadow: 0vw 1.018vw 1.018vw #00000040;
  width: 28.244vw;
  height: 63.104vw;
}

.group_4 {
  padding-bottom: 3.562vw;
}

.font_2 {
  font-size: 7.634vw;
  font-family: Ribeye;
  line-height: 5.573vw;
  color: #000000;
}

.text_4 {
  text-shadow: 0vw 1.018vw 1.018vw #00000040;
}

.image_4 {
  mix-blend-mode: SCREEN;
  width: 13.232vw;
  height: 7.379vw;
}

.pos_2 {
  position: absolute;
  left: 4.071vw;
  bottom: 0;
}

.group_6 {
  padding: 0 0.509vw;
}

.image_5 {
  mix-blend-mode: DARKEN;
  width: 7.379vw;
  height: 11.196vw;
}

.view {
  margin-top: 3.817vw;
}

.image_7 {
  mix-blend-mode: DARKEN;
  width: 7.125vw;
  height: 10.941vw;
}

.image_6 {
  border-radius: 50%;
  width: 10.941vw;
  height: 10.941vw;
}

.image_8 {
  margin-top: 1.527vw;
}

.view_2 {
  margin-top: 2.545vw;
}

.image_9 {
  margin-bottom: 1.018vw;
  mix-blend-mode: DARKEN;
  width: 6.616vw;
  height: 11.705vw;
}

.section_2 {
  padding: 5.598vw 3.562vw 2.545vw;
  background-color: #8decb499;
  border-radius: 5.089vw;
  box-shadow: 0vw 1.018vw 1.018vw #00000040;
  height: 63.104vw;
}

.group_5 {
  height: 5.743vw;
}

.text_5 {
  line-height: 5.743vw;
}

.image_3 {
  mix-blend-mode: SCREEN;
  width: 18.321vw;
  height: 2.29vw;
}

.pos {
  position: absolute;
  right: 0.606vw;
  top: 0.402vw;
}

.grid {
  margin: 0 2.545vw;
  height: 44.784vw;
  display: grid;
  grid-template-rows: repeat(2, minmax(0, 1fr));
  grid-template-columns: repeat(2, minmax(0, 1fr));
  row-gap: 3.83vw;
  column-gap: 3.83vw;
}

.grid-item {
  width: 20.611vw;
  height: 20.611vw;
}

.list {
  padding: 0 1.018vw;
}

.list-item {
  background-color: #f4f4f4;
  border-radius: 5.344vw;
}

.list-item:first-child {
  margin-top: 0;
}

.image_10 {
  border-radius: 5.344vw 0vw 0vw 5.344vw;
  width: 31.807vw;
  height: 26.209vw;
}

.font_3 {
  font-size: 3.053vw;
  font-family: Inter;
  line-height: 2.443vw;
  font-weight: 100;
  color: #000000;
}

.text_6 {
  font-size: 3.308vw;
}

.font_5 {
  font-size: 3.562vw;
  font-family: Inter;
  line-height: 3.313vw;
  font-weight: 200;
  color: #000000;
}

.group_7 {
  padding: 0 1.527vw;
}

.font_4 {
  font-size: 3.053vw;
  font-family: Inter;
  line-height: 2.807vw;
  font-weight: 100;
  color: #000000;
}

.text_7 {
  line-height: 2.659vw;
}

.tab-bar {
  padding: 4.071vw 0 4.58vw;
  overflow: hidden;
  background-image: url('../../images/xiyang098/4929bbe2a8eb6089d4bacf58dbbaada5.png');
  background-size: 100% 100%;
}

.image_12 {
  width: 6.399vw;
  height: 6.399vw;
}

.font_6 {
  font-size: 3.053vw;
  font-family: Roboto;
  line-height: 2.807vw;
  color: #b9bcbe;
}

.equal-division-item {
  width: 7.201vw;
  height: 11.733vw;
}

.text_11 {
  color: #00b140;
}
</style>