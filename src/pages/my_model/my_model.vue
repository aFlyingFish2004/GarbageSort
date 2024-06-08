<script setup>
import { useRouter } from 'vue-router';
import { reactive, onMounted, ref } from 'vue';
import { fetchMessage, createModel, getModels, getRandomImageByFolder } from '@/api/api';

const props = defineProps({});

const data = reactive({});
const email = ref(localStorage.getItem('userEmail') || '');
const user_id = ref('');
const folder_url = ref('');
const model_id = ref('');  // 新增的变量
const models = ref([]); // 存储模型列表

const router = useRouter();

function onClick1() {
  router.push({ name: 'my' });
}

async function onClick() {
  await fetchUserMessage();
  await handleCreateModel();
}

async function fetchUserMessage() {
  try {
    const response = await fetchMessage(email.value);
    user_id.value = response.data.user_id;
    await loadModels();  // 加载模型列表
  } catch (error) {
    console.error('Failed to fetch user info:', error);
  }
}

async function handleCreateModel() {
  try {
    const response = await createModel(user_id.value);
    folder_url.value = response.data.folder_url;
    model_id.value = response.data.model_id;  // 获取 model_id
    // 在创建模型成功后导航到新的模型页面
    router.push({ name: 'new_model', query: { folder_url: folder_url.value, user_id: user_id.value, model_id: model_id.value } });
  } catch (error) {
    console.error('Error creating model:', error);
  }
}

async function loadModels() {
  try {
    const response = await getModels(user_id.value);
    models.value = response.data.models;
    await loadModelImages();  // 加载模型图片
  } catch (error) {
    console.error('Failed to load models:', error);
  }
}

async function loadModelImages() {
  for (const model of models.value) {
    if (model.images) {
      try {
        const response = await getRandomImageByFolder(model.images);
        const blob = await response.data;
        const url = URL.createObjectURL(blob);
        model.image_url = url;  // 将图片 URL 保存到模型对象中
      } catch (error) {
        console.error('Failed to load image:', error);
      }
    }
  }
}

function viewDetails(modelId) {
  router.push({ name: 'model_detail', query: { model_id: modelId } });
}

onMounted(() => {
  fetchUserMessage();
});
</script>

<template>
<div class="flex-col page">
  <div class="flex-row items-center header">
    <img
      class="back-arrow"
      src="https://ide.code.fun/api/image?token=6653eca5602bd200126394b7&name=643e11766a93d71f4d786dabda17d139.png"
      @click="onClick1"
    />
    <span class="text ml-122">我的模型</span>
  </div>
  <div class="flex-col self-stretch group_2">
    <div v-for="model in models" :key="model.model_id" class="flex-row justify-between section" @click="viewDetails(model.model_id)">
      <img
        class="image_2"
        :src="model.image_url"
        alt="model image"
      />
      <div class="flex-col justify-center items-center flex-1">
        <span class="text_2">{{ model.model_name }}</span>
        <span class="font text_3">{{ model.model_description }}</span>
      </div>
      <div class="flex-col justify-center items-center">
        <span :class="{
            'text_pending': model.status === 'pending', 
            'text_training': model.status === 'training', 
            'text_completed': model.status === 'completed'
          }" class="status-text">
          {{ model.status === 'pending' ? '审核中' : model.status === 'training' ? '训练中' : '已完成' }}
        </span>
        <div :class="{
            'status_pending': model.status === 'pending', 
            'status_training': model.status === 'training', 
            'status_completed': model.status === 'completed'
          }" class="status-block"></div>
      </div>
    </div>
  </div>
  <button class="flex-col justify-start items-center self-center text-wrapper" @click="onClick">
    <span class="text_5">新的模型</span>
  </button>
</div>
</template>

<style scoped>
.page {
  padding: 1.19rem 0 3.31rem;
  background-color: #ffffff;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;
}

.header {
  padding: 1.5rem 2.12rem;
  height: 4rem;
  background-color: #f8f8f8;
  box-shadow: 0 0.1rem 0.1rem rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
}

.back-arrow {
  width: 1.5rem;
  height: 1.5rem;
  cursor: pointer;
}

.text {
  color: #181d27;
  font-size: 1.5rem;
  font-family: DM Sans;
  font-weight: 700;
  line-height: 1.5rem;
  margin-left: 1rem;
}

.group_2 {
  padding-top: 1rem;
}

.section {
  background-color: #ffffff;
  box-shadow: 0 0.25rem 0.25rem rgba(0, 0, 0, 0.1);
  margin-bottom: 1rem;
  border-radius: 1rem;
  padding: 1rem;
  display: flex;
  align-items: center;
}

.image_2 {
  width: 6.88rem;
  height: 6.88rem;
  object-fit: cover;
  border-radius: 0.5rem;
  border: 1px solid #ddd;
  box-shadow: 0 0.25rem 0.25rem rgba(0, 0, 0, 0.1);
}

.text_2 {
  color: #000000;
  font-size: 1rem;
  font-family: DM Sans;
  font-weight: 700;
  line-height: 1rem;
  text-align: center;
}

.font {
  font-size: 0.88rem;
  font-family: DM Sans;
  line-height: 1.19rem;
  color: #000000;
  text-align: center;
  margin-top: 0.5rem;
}

.status-text {
  margin-bottom: 0.5rem;
  font-size: 0.88rem;
  font-family: DM Sans;
}

.status_pending {
  color: #ff0000; /* 红色 */
}

.status_training {
  color: #0000ff; /* 蓝色 */
}

.status_completed {
  color: #00b140; /* 绿色 */
}

.status-block {
  width: 1rem;
  height: 1rem;
  border-radius: 0.5rem;
}

.status_pending.status-block {
  background-color: #ff0000; /* 红色 */
}

.status_training.status-block {
  background-color: #0000ff; /* 蓝色 */
}

.status_completed.status-block {
  background-color: #00b140; /* 绿色 */
}

.text_5 {
  color: #ffffff;
  font-size: 1.25rem;
  font-family: Inter;
  font-weight: 700;
  line-height: 1.18rem;
}

.text-wrapper {
  padding: 1rem 2rem;
  background-color: #00b140;
  border-radius: 2rem;
  color: #fff;
  font-size: 1.25rem;
  font-weight: 700;
  cursor: pointer;
  margin-top: 1rem;
  text-align: center;
}
</style>
