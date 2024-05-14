<script setup>
  import { useRouter } from 'vue-router';
  import { reactive, onMounted } from 'vue';

  const props = defineProps({});

  const data = reactive({});

  const router = useRouter();

  //获取视频流
  // const mediaStreamTrack = ref({});
  // const videoStream = ref(''); // 视频stream
  // const imgSrc = ref(''); // 拍照图片
  // let canvas = null;
  // let context = null;
  // const video = ref(null)

  function onClick() {
    router.push({ name: 'home' });
  }

  function onClick_1() {
    router.push({ name: 'recognize_result' });
  }
</script>

<template>
  <div class="flex-col justify-start page">
    <div class="flex-col group">
      <div class="flex-col justify-start items-start header">
        <img class="image" src="../../images/1794f4ab3971c7e55da31307933ee500.png" @click="onClick" />
      </div>
      <div class="flex-row justify-between items-center section">
        <img class="album_button" src="../../images/f021282d9cadcb210411fcf1af1282c0.png" />
        <div class="flex-col justify-start items-center photo_button">
          <img class="image_2" src="../../images/006988cd50ac0e6d285e307c37673de1.png" @click="onClick_1" />
        </div>
        <div class="flex-col justify-start items-center photo_button">
          <img class="change_button" src="../../images/44a21b179d9c82a587cbd2119e166494.png" />
        </div>
      </div>
      <div class="section_3"></div>
    </div>
  </div>
</template>

<style scoped lang="css">
  .page {
    background-color: #ffffff;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .group {
    overflow-y: auto;
  }
  .header {
    padding: 10.858vw 0 11.025vw;
    background-color: #000;
  }
  .image {
    margin-left: 9.644vw;
    width: 3.562vw;
    height: 3.308vw;
  }
  .section {
    padding: 144.784vw 1.781vw 7.125vw 2.036vw;
    background-color: rgba(30, 30, 30, .5686274509803921);
  }
  .album_button {
    width: 18.321vw;
    height: 14.249vw;
  }
  .photo_button {
    width: 18.321vw;
  }
  .image_2 {
    width: 18.321vw;
    height: 18.321vw;
  }
  .section_3 {
    background-color: #000;
    height: 21.374vw;
  }
  .change_button {
    border-radius: 50%;
    width: 12.214vw;
    height: 12.214vw;
  }
</style>