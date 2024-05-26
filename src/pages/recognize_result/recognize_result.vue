<script setup>
  import { useRouter, useRoute } from 'vue-router';
  import { ref, reactive, onMounted, computed } from 'vue';
  import { fetchImage, fetchInferMessage, fetchMessage, infer } from '@/api/api';

  const props = defineProps({});

  const data = reactive({});

  const router = useRouter();
    
  const route = useRoute();
  const decodedImgSrc = ref('')
  const email = ref(localStorage.getItem('userEmail') || '');
  const user_id = ref('')
  const photo_url = ref('')
  const top1_pro = ref('')
  const top2_pro = ref('')
  const top3_pro = ref('')
  const top1_res = ref('')
  const top2_res = ref('')
  const top3_res = ref('')

  function onClick() {
    router.push({ name: 'home' });
  }

  function onClick_1() {
    router.push({ name: 'feedback' });
  }

  function onClick_2() {
    router.push({ name: 'photograph' });
  }

  async function fetchUserMessage() {
  try {
    const response = await fetchMessage(email.value);
    user_id.value = response.data.user_id;
  } catch (error) {
    console.error('Failed to fetch user name:', error);
  }
}

async function InferMessage() {
    try{
      const response = await fetchInferMessage(email.value);
      top1_pro.value = response.data.top1_pro
      top2_pro.value = response.data.top2_pro
      top3_pro.value = response.data.top3_pro
      top1_res.value = response.data.top1_res
      top2_res.value = response.data.top2_res
      top3_res.value = response.data.top3_res
    } catch (error) {
       console.error('Failed to fetch infer:', error);
  }
}
  
const fetchAndDisplayImage = async (imageName) => {
  try {
    const response = await fetchImage(imageName);
    const blob = await response.data;
    decodedImgSrc.value = URL.createObjectURL(blob);
  } catch (error) {
    console.error('Error fetching image:', error);
  }
};

onMounted(async () => {
  await fetchUserMessage();
  photo_url.value = user_id.value + '_ph.jpg';
  fetchAndDisplayImage(photo_url.value)
  await InferMessage()
  console.log(top1_res.value)
});

</script>

<template>
  <div class="flex-col page">
    <div class="flex-col justify-start items-start image-wrapper" :style="{ backgroundImage: 'url(' + decodedImgSrc + ')' }">
      <img class="return" src="../../images/4c095678482b518c22b5db9dedc98c6d.png" @click="onClick" />
    </div>
    <div class="flex-col relative section">
      <span class="self-center font">识别结果</span>
      <div class="flex-row justify-between items-center self-stretch section_1">
        <span class="font_1 text">{{ top1_res }}</span>
        <div class="flex-row items-center group">
          <span class="font_1">准确率</span>
          <div class="flex-col justify-start items-start shrink-0 self-stretch button ml-3">
            <div class="flex-col justify-start items-center text-wrapper"><span class="font_3 text_3">{{ top1_pro }}</span></div>
          </div>
        </div>
      </div>
      <div class="flex-row justify-between items-center self-stretch section_1">
        <span class="font_2 text">{{ top2_res }}</span>
        <div class="flex-row items-center group">
          <span class="font_1">准确率</span>
          <div class="flex-col justify-start items-start shrink-0 self-stretch button ml-3">
            <div class="flex-col justify-start items-end text-wrapper_2"><span class="font_3 text_3">{{ top2_pro }}</span></div>
          </div>
        </div>
      </div>
      <div class="flex-row justify-between items-center self-stretch section_1">
        <span class="font_2 text">{{ top3_res }}</span>
        <div class="flex-row items-center group">
          <span class="font_1">准确率</span>
          <div class="flex-col justify-start items-start shrink-0 self-stretch button ml-3">
            <div class="flex-col justify-start items-end text-wrapper_3"><span class="font_3 text_3">{{ top3_pro }}</span></div>
          </div>
        </div>
      </div>
      <div class="self-stretch divider"></div>
      <span class="self-center font text_5">塑料相关知识</span>
      <div class="flex-col justify-start self-stretch group_2">
        <div class="flex-col justify-start text-wrapper_6">
          <span class="text_6">
            了解你所在地区接受的可回收塑料类型。常见的可回收塑料包括PET（聚对苯二甲酸乙二醇酯）、HDPE（高密度聚乙烯）、LDPE（低密度聚乙烯）、PP（聚丙烯）和PS（聚苯乙烯）。
          </span>
        </div>
      </div>
    </div>
    <div class="flex-row relative section_7">
      <div class="flex-col justify-start items-center text-wrapper_1" @click="onClick_1">
        <span class="font_4 text_7">反馈错误</span>
      </div>
      <div class="flex-col justify-start items-center text-wrapper_4 ml-45 text-wrapper_1" @click="onClick_2">
        <span class="font_4 text_8">再拍一张</span>
      </div>
    </div>
  </div>
</template>

<style scoped lang="css">
  .ml-3 {
    margin-left: .763vw;
  }
  .ml-45 {
    margin-left: 11.45vw;
  }
  .page {
    padding-bottom: 11.705vw;
    background-color: #fff;
    height: 100%;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
  }
  .image-wrapper {
    padding: 9.092vw 0 76.659vw;
    background-size: 100% 100%;
    background-repeat: no-repeat;
  }
  .return {
    margin-left: 7.634vw;
    width: 3.562vw;
    height: 2.799vw;
  }
  .section {
    margin-top: -11.45vw;
    padding-top: 5.74vw;
    background-color: #fff;
    border-radius: 8.142vw 8.142vw 0 .509vw;
  }
  .font {
    font-size: 4.071vw;
    font-family: Roboto;
    line-height: 3.761vw;
    color: #000;
  }
  .section_1 {
    margin: 5.852vw 5.598vw 0 5.852vw;
    padding: 1.781vw 7.288vw 1.496vw;
    background-color: #00b140;
    border-radius: 1.272vw;
    box-shadow: 0 1.018vw 1.018vw rgba(0, 0, 0, .25098039215686274);
  }
  .font_1 {
    font-size: 3.562vw;
    font-family: Roboto;
    line-height: 3.293vw;
    color: #fff;
  }
  .group {
    margin-right: 2.127vw;
  }
  .button {
    padding-bottom: .267vw;
    background-color: #fff;
    border-radius: 5.089vw;
    width: 24.682vw;
    height: 3.817vw;
    border-left: .254vw solid #b9bcbe;
    border-right: .254vw solid #b9bcbe;
    border-top: .254vw solid #b9bcbe;
    border-bottom: .254vw solid #b9bcbe;
  }
  .text-wrapper {
    margin-left: .509vw;
    margin-top: .254vw;
    padding-top: .509vw;
    padding-bottom: .382vw;
    background-color: rgba(31, 171, 137, .9411764705882353);
    border-radius: 5.089vw;
    width: 20.865vw;
  }
  .font_3 {
    font-size: 2.799vw;
    font-family: Roboto;
    line-height: 2.048vw;
    color: #000;
  }
  .text_3 {
    margin-right: 1.232vw;
  }
  .font_2 {
    font-size: 3.562vw;
    font-family: Roboto;
    color: #fff;
  }
  .text {
    line-height: 3.28vw;
  }
  .text-wrapper_2 {
    margin-left: .254vw;
    margin-top: .382vw;
    padding-top: .509vw;
    padding-bottom: .127vw;
    background-color: rgba(31, 171, 137, .9411764705882353);
    border-radius: 5.089vw;
    width: 17.303vw;
  }
  .text-wrapper_3 {
    margin-left: .254vw;
    margin-top: .382vw;
    padding-top: .509vw;
    padding-bottom: .127vw;
    background-color: rgba(31, 171, 137, .9411764705882353);
    border-radius: 5.089vw;
    width: 13.995vw;
    
  }
  .divider {
    margin-top: 4.835vw;
    background-color: #d9d9d9;
    height: .509vw;
  }
  .text_5 {
    margin-top: 2.433vw;
  }
  .group_2 {
    margin-top: 1.949vw;
    padding: .763vw 0 7.634vw;
    border-radius: 3.562vw;
  }
  .text-wrapper_6 {
    margin-left: 3.053vw;
    margin-right: 2.036vw;
    padding: 4.835vw 0 10.178vw;
    background-color: #fff;
    border-radius: 5.598vw;
    box-shadow: 0 1.018vw 1.018vw rgba(0, 0, 0, .25098039215686274);
    border-left: .254vw solid #9e9e9e;
    border-right: .254vw solid #9e9e9e;
    border-top: .254vw solid #9e9e9e;
    border-bottom: .254vw solid #9e9e9e;
  }
  .text_6 {
    margin-left: 4.972vw;
    margin-right: 2.662vw;
    color: #000;
    font-size: 4.071vw;
    font-family: Inter;
    line-height: 4.835vw;
    text-indent: 8.265vw;
  }
  .section_7 {
    margin-top: -3.562vw;
    padding: 2.277vw 3.55vw 2.048vw;
    background-color: #fff;
    border-radius: 2.799vw 0 0 .763vw;
    border-left: .254vw solid rgba(0, 0, 0, .07058823529411765);
    border-right: .254vw solid rgba(0, 0, 0, .07058823529411765);
    border-top: .254vw solid rgba(0, 0, 0, .07058823529411765);
    border-bottom: .254vw solid rgba(0, 0, 0, .07058823529411765);
  }
  .font_4 {
    font-size: 4.071vw;
    font-family: DM Sans;
    line-height: 3.761vw;
    font-weight: 700;
    color: #fff;
  }
  .text_7 {
    line-height: 3.847vw;
  }
  .text-wrapper_4 {
    flex: 1 1 40.458vw;
  }
  .text-wrapper_1 {
    padding: 6.723vw 0 5.969vw;
    flex: 1 1 40.458vw;
    background-color: #00b140;
    border-radius: 7.634vw;
    height: 16.539vw;
  }
  .text_8 {
    line-height: 3.835vw;
  }
</style>