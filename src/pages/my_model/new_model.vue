<script setup>
import { useRouter, useRoute } from 'vue-router';
import { ref, reactive, onMounted } from 'vue';
import { uploads, fetchMessage, getImageByPath,updateModel } from '@/api/api';

const props = defineProps({});
const data = reactive({});
const router = useRouter();
const route = useRoute();  // 使用 useRoute 获取路由参数


const email = ref(localStorage.getItem('userEmail') || '');
const user_id = ref(route.query.user_id || '');  // 从路由参数获取 user_id
const model_id = ref(route.query.model_id || '');  // 从路由参数获取 model_id
const folder_url = ref(route.query.folder_url || '');  // 从路由参数获取 folder_url
const images = ref([]); // 用于存储上传的图片列表
const fileInputRef = ref(null); // 引用文件输入元素
const model_name = ref(''); // 模型名字
const model_description = ref(''); // 模型描述

function onClick(){
  router.push({name:'my_model'})
}

async function fetchUserMessage() {
  try {
    const response = await fetchMessage(email.value);
    user_id.value = response.data.user_id;
  } catch (error) {
    console.error('Failed to fetch user info:', error);
  }
}

function triggerFileInput() {
  fileInputRef.value.click(); // 触发文件输入对话框
}

function handleFileChange(event) {
  const files = event.target.files;
  const formData = new FormData();
  formData.append('user_id', user_id.value);
  formData.append('folder_url', folder_url.value);  // 添加 folder_url
  for (let i = 0; i < files.length; i++) {
    formData.append('images', files[i]);
  }
  uploadImages(formData);
}

async function uploadImages(formData) {
  try {
    const response = await uploads(formData);
    images.value = response.data.uploaded_files; // 假设后端返回上传图片的路径
    await loadImages();
  } catch (error) {
    console.error('Failed to upload images:', error);
  }
}

async function loadImages() {
  const loadedImages = [];
  for (const img of images.value) {
    try {
      const response = await getImageByPath(folder_url.value, img.split('/').pop());
      const blob = await response.data;
      const url = URL.createObjectURL(blob);
      loadedImages.push(url);
    } catch (error) {
      console.error('Failed to load image:', error);
    }
  }
  images.value = loadedImages;
}

async function handleSubmit() {
  try {
    const formData = new FormData();
    formData.append('model_id', model_id.value);
    formData.append('model_name', model_name.value);
    formData.append('model_description', model_description.value);
    const response = await updateModel(formData);
    console.log('Model updated successfully:', response.data);
    // 处理成功的更新逻辑
    router.push({ name: 'my_model' });
  } catch (error) {
    console.error('Failed to update model:', error);

  }
}

onMounted(() => {
  fetchUserMessage();
  loadImages();
});

</script>

<template>
<div class="flex-col page">
  <div class="flex-row justify-center header group">
    <img
      class="image pos"
      src="https://ide.code.fun/api/image?token=66533fdda16e9e00124ff259&name=643e11766a93d71f4d786dabda17d139.png" @click="onClick"
    />
    <span class="font text">新建模型</span>
  </div>
  <div class="flex-col flex-1 group_2">
    <div class="flex-col relative section">
      <span class="self-center font text_2">使用图片</span>
      <div class="flex-col self-stretch mt-12">
        <input type="file" multiple ref="fileInputRef" @change="handleFileChange" style="display: none;" />
        <div class="self-stretch grid">
          <div v-for="(img, index) in images" :key="index" class="grid-item">
            <img :src="img" alt="uploaded image" class="uploaded-image" />
          </div>
        </div>
        <div class="flex-col justify-start items-center self-center text-wrapper mt-13" @click="triggerFileInput">
          <span class="font_2 text_3">上传图片</span>
        </div>
      </div>
    </div>
    <div class="flex-col group_3">
      <div class="flex-col justify-start items-center relative text-wrapper_2">
        <span class="font text_4">模型名字</span>
        <input v-model="model_name" type="text" class="input-field" placeholder="请输入模型名字" />
      </div>
      <div class="flex-col group_4">
        <div class="flex-col justify-start items-center self-stretch relative text-wrapper_3">
          <span class="font text_5">模型描述</span>
          <textarea v-model="model_description" class="textarea-field" placeholder="请输入模型描述"></textarea>
        </div>
        <button class="flex-col justify-start items-center self-center text-wrapper_4 mt-27" @click="handleSubmit">
          <span class="font_2 text_6">创建模型</span>
        </button>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped lang="css">
.mt-13 {
  margin-top: 0.81rem;
}
.mt-27 {
  margin-top: 1.69rem;
}
.page {
  background-color: #ffffff;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;
}
.header {
  position: relative;
}
.group {
  padding: 2.32rem 2.12rem 0.73rem;
  height: 3.88rem;
}
.image {
  width: 0.88rem;
  height: 0.81rem;
}
.pos {
  position: absolute;
  left: 2.12rem;
  bottom: 0.71rem;
}
.font {
  font-size: 0.88rem;
  font-family: DM Sans;
  line-height: 0.82rem;
  font-weight: 700;
  color: #000000;
}
.text {
  color: #181d27;
}
.group_2 {
  padding: 0.94rem 0.69rem 0 0.88rem;
  overflow-y: auto;
}
.section {
  padding: 0.63rem 0.52rem 0.69rem 0.69rem;
  background-color: #ffffff;
  border-radius: 1.69rem;
  box-shadow: 0rem 0.25rem 0.25rem #00000040;
  border: solid 0.063rem #afa9a9;
}
.text_2 {
  line-height: 0.83rem;
}
.grid {
  margin-right: 0.13rem;
  display: grid;
  grid-template-rows: repeat(auto-fill, minmax(6.44rem, 1fr));
  grid-template-columns: repeat(auto-fill, minmax(6.44rem, 1fr));
  gap: 1.16rem;
}
.grid-item {
  width: 6.44rem;
  height: 6.44rem;
  overflow: hidden;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
}
.uploaded-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.text-wrapper {
  padding: 0.71rem 0 0.56rem;
  background-color: #00b140;
  border-radius: 2.5rem;
  width: 7rem;
  cursor: pointer;
}
.font_2 {
  font-size: 1.25rem;
  font-family: Inter;
  line-height: 1.22rem;
  font-weight: 700;
  color: #ffffff;
}
.text_3 {
  transform: rotate(0.9deg);
}
.group_3 {
  padding: 1.81rem 0 1.06rem 0.13rem;
}
.text-wrapper_2 {
  padding: 0.37rem 0 2.36rem;
  background-color: #ffffff;
  border-radius: 1.88rem;
  box-shadow: 0rem 0.25rem 0.25rem #00000040;
  border: solid 0.063rem #c6c6c6;
  width: 100%;
  margin-bottom: 1rem;
}
.input-field {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  font-size: 1rem;
  margin-top: 0.5rem;
}
.text_4 {
  line-height: 0.83rem;
}
.group_4 {
  padding: 1.44rem 0 1.44rem;
}
.text-wrapper_3 {
  padding: 0.57rem 0 11.36rem;
  background-color: #ffffff;
  border-radius: 1.88rem;
  box-shadow: 0rem 0.25rem 0.25rem #00000040;
  border: solid 0.063rem #c6c6c6;
  width: 100%;
  margin-bottom: 1rem;
}
.textarea-field {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  font-size: 1rem;
  margin-top: 0.5rem;
  height: 5rem;
  resize: none;
}
.text_5 {
  line-height: 0.82rem;
}
.text-wrapper_4 {
  padding: 1.52rem 0 1.41rem;
  background-color: #00b140;
  border-radius: 1.88rem;
  width: 9.5rem;
  cursor: pointer;
}
.text_6 {
  line-height: 1.19rem;
}
</style>
