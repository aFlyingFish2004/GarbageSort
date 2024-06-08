<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { getModelDetails, getImagesByFolder, deleteModelById } from '@/api/api';

const route = useRoute();
const router = useRouter();
const modelId = ref(route.query.model_id);
const model = ref({});
const images = ref([]);
function onClick1(){
  router.push({name:'my_model'});
}
async function fetchModelDetails() {
  try {
    const response = await getModelDetails(modelId.value);
    model.value = response.data;
    await loadModelImages(model.value.images);
  } catch (error) {
    console.error('Failed to fetch model details:', error);
  }
}

async function loadModelImages(folderUrl) {
  try {
    const response = await getImagesByFolder(folderUrl);
    images.value = response.data.images.map(img => `data:image/jpeg;base64,${img.data}`);
  } catch (error) {
    console.error('Failed to load model images:', error);
  }
}

async function deleteModel() {
  try {
    await deleteModelById({ model_id: modelId.value });
    router.push({ name: 'my_model' });
  } catch (error) {
    console.error('Failed to delete model:', error);
  }
}

const statusClass = computed(() => {
  switch (model.value.status) {
    case 'pending':
      return 'status-pending';
    case 'training':
      return 'status-training';
    case 'completed':
      return 'status-completed';
    default:
      return '';
  }
});

onMounted(() => {
  fetchModelDetails();
});
</script>

<template>
  <div class="flex-col page">
    <div class="flex-row items-center header">
      <img
        class="image"
        src="https://ide.code.fun/api/image?token=6653eca5602bd200126394b7&name=643e11766a93d71f4d786dabda17d139.png"@click="onClick1"
      />
      <span class="font text ml-122">{{ model.model_name }}</span>
    </div>
    <div class="flex-col flex-1 group">
      <div class="flex-col relative section">
        <span class="self-center font text_2">使用图片</span>
        <div class="self-stretch grid mt-14">
          <div v-for="(img, index) in images" :key="index" class="grid-item">
            <img :src="img" alt="模型图片" />
          </div>
        </div>
      </div>
      <div class="flex-col group_2 mt-14">
        <div class="flex-col justify-start items-center self-stretch relative text-wrapper">
          <span class="font text_2">模型描述</span>
          <span class="font text_3">{{ model.model_description }}</span>
        </div>
        <div class="flex-col justify-start items-center self-center text-wrapper_2 mt-23" @click="deleteModel">
          <span class="text_4">删除模型</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="css">
.ml-122 {
  margin-left: 7.63rem;
}
.mt-14 {
  margin-top: 0.88rem;
}
.mt-23 {
  margin-top: 1.44rem;
}
.page {
  background-color: #ffffff;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;
}
.header {
  padding: 2.35rem 2.12rem 0.67rem;
  height: 3.94rem;
}
.image {
  width: 0.88rem;
  height: 0.81rem;
}
.font {
  font-size: 0.88rem;
  font-family: DM Sans;
  line-height: 0.83rem;
  font-weight: 700;
  color: #000000;
}
.text {
  color: #181d27;
}
.group {
  padding: 0.88rem 0.75rem 0 0.81rem;
  overflow-y: auto;
}
.section {
  padding: 0.69rem 0.64rem 2.06rem 0.69rem;
  background-color: #ffffff;
  border-radius: 1.69rem;
  box-shadow: 0rem 0.25rem 0.25rem #00000040;
  border: solid 0.063rem #afa9a9;
}
.text_2 {
  line-height: 0.83rem;
  font-size: 1rem;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 1rem;
}
.grid-item {
  width: 100%;
  padding-top: 100%;
  position: relative;
}
.grid-item img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 0.5rem;
}
.group_2 {
  padding: 2.75rem 0 2.75rem;
}
.text-wrapper {
  padding: 0.69rem 0;
  background-color: #ffffff;
  border-radius: 1.88rem;
  box-shadow: 0rem 0.25rem 0.25rem #00000040;
  border: solid 0.063rem #c6c6c6;
}
.text_3 {
  line-height: 0.82rem;
  margin-top: 0.5rem;
}
.text-wrapper_2 {
  padding: 1.54rem 0 1.41rem;
  background-color: #ee2222;
  border-radius: 1.88rem;
  width: 9.5rem;
  cursor: pointer;
}
.text_4 {
  color: #ffffff;
  font-size: 1.25rem;
  font-family: Inter;
  font-weight: 700;
  line-height: 1.18rem;
}
</style>
