<script setup>
import { useRouter } from 'vue-router';
import { reactive, onMounted } from 'vue';

const props = defineProps({});

const data = reactive({});

const router = useRouter();
</script>

<template>
<div class="flex-col page">
  <div class="flex-row justify-center items-center self-stretch relative group">
    <img
      class="image pos"
      src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=824283acfe845390be4089574f86a353.png"
    />
    <span class="text">我的模型</span>
  </div>
  <div class="flex-col self-stretch group_2">
    <div class="flex-row justify-between section">
      <img
        class="image_2"
        src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=59c968c80bfef6d02569c62640546e02.png"
      />
      <div class="flex-row items-end self-start group_3">
        <div class="flex-col items-center">
          <span class="text_2">模型名</span>
          <span class="font text_3">模型制作者</span>
          <span class="font">自己的描述</span>
        </div>
        <div class="ml-46 flex-row items-center group_4">
          <div class="flex-col justify-start items-center button"><span class="font text_4">已完成</span></div>
          <img
            class="image_3 ml-19"
            src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=6de690b563d52abcde97853679620f76.png"
          />
        </div>
      </div>
    </div>
    <div class="flex-row justify-between section mt-7">
      <img
        class="image_2"
        src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=59c968c80bfef6d02569c62640546e02.png"
      />
      <div class="flex-row items-center self-start group_5">
        <div class="button_2"></div>
        <img
          class="image_3 ml-19"
          src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=6de690b563d52abcde97853679620f76.png"
        />
      </div>
    </div>
    <div class="flex-row justify-between section mt-7">
      <img
        class="image_2"
        src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=59c968c80bfef6d02569c62640546e02.png"
      />
      <div class="flex-row items-center self-start group_6">
        <div class="button_2"></div>
        <img
          class="image_3 ml-19"
          src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=6de690b563d52abcde97853679620f76.png"
        />
      </div>
    </div>
    <div class="flex-row justify-between section mt-7">
      <img
        class="image_2"
        src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=59c968c80bfef6d02569c62640546e02.png"
      />
      <div class="flex-row items-center self-start group_7">
        <div class="section_2"></div>
        <img
          class="image_3 ml-19"
          src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=6de690b563d52abcde97853679620f76.png"
        />
      </div>
    </div>
    <div class="flex-row justify-between section mt-7">
      <img
        class="image_2"
        src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=59c968c80bfef6d02569c62640546e02.png"
      />
      <div class="flex-row items-center self-start group_8">
        <div class="button_2"></div>
        <img
          class="image_3 ml-19"
          src="https://ide.code.fun/api/image?token=66431e0aa2432f00114e8100&name=6de690b563d52abcde97853679620f76.png"
        />
      </div>
    </div>
  </div>
  <div class="flex-col justify-start items-center self-center text-wrapper"><span class="text_5">新的模型</span></div>
</div>
</template>

<style scoped lang="css">
.ml-19 {
  margin-left: 1.19rem;
}
.mt-7 {
  margin-top: 0.44rem;
}
.page {
  padding: 1.19rem 0 3.31rem;
  background-color: #ffffff;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;
}
.group {
  padding: 1.44rem 2.12rem 1.17rem;
  border-bottom: solid 0.13rem #d9d9d9;
}
.image {
  width: 0.88rem;
  height: 0.81rem;
}
.pos {
  position: absolute;
  left: 2.12rem;
  top: 1.17rem;
}
.text {
  color: #181d27;
  font-size: 0.88rem;
  font-family: DM Sans;
  font-weight: 700;
  line-height: 0.83rem;
}
.group_2 {
  padding-top: 0.94rem;
}
.section {
  background-color: #ffffff;
  box-shadow: 0rem 0.25rem 0.25rem #00000040;
}
.image_2 {
  width: 6.88rem;
  height: 6.5rem;
}
.group_3 {
  margin-right: 1.13rem;
  margin-top: 0.71rem;
}
.text_2 {
  color: #000000;
  font-size: 1rem;
  font-family: DM Sans;
  font-weight: 700;
  line-height: 0.95rem;
}
.font {
  font-size: 0.88rem;
  font-family: DM Sans;
  line-height: 1.19rem;
  color: #000000;
}
.text_3 {
  margin-top: 0.14rem;
}
.group_4 {
  margin-bottom: 0.23rem;
}
.button {
  padding: 0.7rem 0 0.55rem;
  background-color: #00b140;
  width: 4.06rem;
  height: 2.06rem;
}
.text_4 {
  color: #ffffff;
  line-height: 0.81rem;
}
.image_3 {
  width: 0.44rem;
  height: 0.75rem;
}
.group_5 {
  margin-right: 1.13rem;
  margin-top: 1.88rem;
}
.button_2 {
  background-color: #00b140;
  width: 4.06rem;
  height: 2.06rem;
}
.group_6 {
  margin-right: 1.13rem;
  margin-top: 1.88rem;
}
.group_7 {
  margin-right: 1.13rem;
  margin-top: 1.88rem;
}
.section_2 {
  background-color: #ee2222;
  width: 4.06rem;
  height: 2.06rem;
}
.group_8 {
  margin-right: 1.13rem;
  margin-top: 1.81rem;
}
.text-wrapper {
  margin-top: 5.69rem;
  padding: 1.54rem 0 1.41rem;
  background-color: #00b140;
  border-radius: 1.88rem;
  width: 9.5rem;
}
.text_5 {
  color: #ffffff;
  font-size: 1.25rem;
  font-family: Inter;
  font-weight: 700;
  line-height: 1.18rem;
}
</style>