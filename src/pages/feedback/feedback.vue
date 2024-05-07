<script setup>
  import { useRouter } from 'vue-router';
  import { reactive, onMounted } from 'vue';

  const props = defineProps({});

  const data = reactive({});

  const router = useRouter();

  function onClick() {
    router.push({ name: 'recognize_result' });
  }
</script>

<template>
  <div class="flex-col page">
    <div class="flex-col justify-start items-center text-wrapper"><span class="font text">该物品是什么？</span></div>
    <div class="flex-col group mt-11">
      <div class="shrink-0 self-stretch section"></div>
      <div class="flex-col justify-start self-stretch group_2">
        <div class="flex-col justify-start items-center text-wrapper">
          <span class="font text_2">该物品属于什么分类？</span>
        </div>
      </div>
      <div class="flex-col justify-start items-end self-stretch relative image-wrapper">
        <img class="image" src="../../images/834e944ca75ae1febc56085de85ab92a.png" />
      </div>
      <div class="flex-col self-stretch section_2">
        <span class="self-center font_2">可回收垃圾</span>
        <div class="mt-8 self-stretch divider"></div>
        <span class="mt-8 self-center font_2">有害垃圾</span>
        <div class="mt-8 self-stretch divider"></div>
        <span class="mt-8 self-center font_2">厨余垃圾</span>
        <div class="mt-8 self-stretch divider"></div>
        <span class="mt-8 self-center font_2">其他垃圾</span>
      </div>
      <div class="flex-col justify-start items-center self-center submit_button" @click="onClick">
        <span class="font text_5">提交</span>
      </div>
    </div>
  </div>
</template>

<style scoped lang="css">
  .mt-11 {
    margin-top: 2.828vw;
  }
  .page {
    padding: 6.427vw 4.884vw 6.17vw 5.398vw;
    background-color: hsla(0, 0%, 100%, .4);
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .text-wrapper {
    padding: 3.892vw 0 3.905vw;
    background-color: #00b140;
    border-radius: 5.141vw;
  }
  .font {
    font-size: 5.141vw;
    font-family: Inter;
    line-height: 4.746vw;
    color: #fff;
  }
  .text {
    line-height: 4.776vw;
  }
  .group {
    padding: .771vw 0 .771vw;
  }
  .section {
    background-color: #fff;
    box-shadow: 0 1.028vw 1.028vw rgba(0, 0, 0, .25098039215686274);
    height: 11.568vw;
    border-left: .257vw solid #a1a0a0;
    border-right: .257vw solid #a1a0a0;
    border-top: .257vw solid #a1a0a0;
    border-bottom: .257vw solid #a1a0a0;
  }
  .group_2 {
    margin-top: 4.113vw;
    padding-bottom: 2.602vw;
    filter: drop-shadow(0 1.028vw .514vw #00000040);
  }
  .text_2 {
    line-height: 4.781vw;
  }
  .image-wrapper {
    margin-top: 2.057vw;
    padding: 3.846vw 0 2.581vw;
    background-color: #fff;
    box-shadow: 0 1.028vw 1.028vw rgba(0, 0, 0, .25098039215686274);
    border-left: .257vw solid #959595;
    border-right: .257vw solid #959595;
    border-top: .257vw solid #959595;
    border-bottom: .514vw solid #b8b8b8;
  }
  .image {
    margin-right: 3.866vw;
    width: 2.314vw;
    height: 1.285vw;
  }
  .section_2 {
    padding: 1.584vw 0 2.154vw;
    background-color: #fff;
    border-radius: 0 0 4.37vw 4.37vw;
    box-shadow: 0 1.028vw 1.028vw rgba(0, 0, 0, .25098039215686274);
    border-left: .257vw solid #a4a4a4;
    border-right: .257vw solid #a4a4a4;
    border-top: .257vw solid #a4a4a4;
    border-bottom: .257vw solid #a4a4a4;
  }
  .font_2 {
    font-size: 5.141vw;
    font-family: Inter;
    line-height: 4.746vw;
    color: #000;
  }
  .divider {
    background-color: #b1b1b1;
    height: .514vw;
  }
  .text_5 {
    font-weight: 700;
    line-height: 4.853vw;
  }
  .submit_button {
    margin-top: 6.17vw;
    padding: 6.17vw 0 6.684vw;
    background-color: #00b140;
    border-radius: 10.283vw;
    width: 52.442vw;
  }
</style>