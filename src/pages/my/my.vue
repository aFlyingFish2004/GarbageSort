<script setup>
  import { useRouter } from 'vue-router';
  import { ref, reactive, onMounted } from 'vue';
  import { fetchMessage, fetchImage } from '@/api/api';

  const props = defineProps({});
  const data = reactive({});
  const router = useRouter();

  //用户信息
  const name = ref('')
  const email = ref(localStorage.getItem('userEmail') || '');
  const avatar_url = ref('')
  const avatar = ref('')

  function onClick() {
    router.push({ name: 'account' });
  }

  function onClick_1() {
    router.push({ name: 'log_in' });
  }

  function onClick_2() {
    router.push({ name: 'home' });
  }

  function onClick_3()
  {
    router.push({name:'my_model'})
  }

  async function fetchUserMessage() {
    try{
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

onMounted(async () => {
    await fetchUserMessage();
    fetchAndDisplayImage(avatar_url.value);
  });

</script>

<template>
  <div class="flex-col page">
    <div class="flex-col group">
      <div class="flex-col group_2">
        <span class="self-start text">个人主页</span>
        <div class="flex-col self-stretch group_1">
          <div class="flex-row items-center relative section">
            <div class="flex-col justify-start items-center image-wrapper">
              <img class="image" :src="avatar" />
            </div>
            <div class="ml-12 flex-col items-start flex-1">
              <span class="text_2">{{ name }}</span>
              <span class="mt-6 font text_3">正式会员</span>
            </div>
          </div>
          <div class="mt-22 flex-col section_2">
            <div class="flex-row justify-between items-center" @click="onClick">
              <div class="flex-row items-center">
                <img class="image_2" src="../../images/546fd3f3447f7a5c4e01902f97bf32ca.png" />
                <div class="ml-16 flex-col items-start">
                  <span class="font_2 text_4">个人信息</span>
                  <span class="mt-10 font">修改我的账户信息</span>
                </div>
              </div>
              <div class="flex-row items-center">
                <img class="image_4" src="../../images/78aaef27dc6051753e9a783745ea6d66.png" />
                <img class="ml-40 image_3" src="../../images/cc384e6e23b61b0cf448c97004b10949.png" />
              </div>
            </div>
            <div class="flex-col mt-25">
              <div class="flex-row justify-between items-center">
                <div class="flex-row items-center">
                  <img class="image_5" src="../../images/cd7427faa87b3ad69ec71834e6296a94.png" />
                  <div class="ml-16 flex-col items-start">
                    <span class="font_2 text_6">切换账号</span>
                    <span class="mt-10 font text_7">管理我保存的账号</span>
                  </div>
                </div>
                <img class="image_3" src="../../images/cc384e6e23b61b0cf448c97004b10949.png" />
              </div>
              <div class="flex-row justify-between items-center mt-25" @click="onClick_3">
                <div class="flex-row items-center">
                  <img class="image_5" src="../../images/7c538df0d704d28c82642b8e6148f31d.png" />
                  <div class="ml-16 flex-col items-start">
                    <span class="font_2">我的模型</span>
                    <span class="mt-10 font text_8">训练我的模型或上传数据集</span>
                  </div>
                </div>
                <img class="image_3" src="../../images/f17c3760bbf9ee7611bcded5a95a263f.png" />
              </div>
              <div class="flex-row justify-between items-center mt-25">
                <div class="flex-row items-center">
                  <img class="image_2" src="../../images/15ea71abdb918a83e6e859e8f5ba0414.png" />
                  <div class="ml-16 flex-col items-start">
                    <span class="font_2 text_9">安全验证</span>
                    <span class="mt-10 font text_10">修改验证邮箱</span>
                  </div>
                </div>
                <img class="image_3" src="../../images/cc384e6e23b61b0cf448c97004b10949.png" />
              </div>
              <div class="flex-row justify-between items-center mt-25" @click="onClick_1">
                <div class="flex-row items-center">
                  <img class="image_2" src="../../images/598aa9dc30c615d8b820c4bf1ca1a817.png" />
                  <div class="ml-16 flex-col items-start">
                    <span class="font_2 text_11">注销</span>
                    <span class="mt-10 font text_12">安全退出账号</span>
                  </div>
                </div>
                <img class="image_3" src="../../images/cc384e6e23b61b0cf448c97004b10949.png" />
              </div>
            </div>
          </div>
        </div>
        <span class="self-start font_2 text_13">更多</span>
      </div>
      <div class="flex-col section_3">
        <div class="flex-row justify-between items-center">
          <div class="flex-row items-center">
            <img class="shrink-0 image_2" src="../../images/2e3d15e3dd089d696256b075764fd163.png" />
            <span class="ml-16 font_2 text_14">获取帮助</span>
          </div>
          <img class="image_3" src="../../images/f17c3760bbf9ee7611bcded5a95a263f.png" />
        </div>
        <div class="flex-row justify-between items-center mt-25">
          <div class="flex-row items-center">
            <img class="shrink-0 image_2" src="../../images/f41d8e99522a1555ab745e789af457fb.png" />
            <span class="ml-16 font_2">联系我们</span>
          </div>
          <img class="image_3" src="../../images/cc384e6e23b61b0cf448c97004b10949.png" />
        </div>
      </div>
    </div>
    <!-- 底部导航栏 -->
    <tabBar :select="4" />
  </div>
</template>

<style scoped lang="css">
  .mt-25 {
    margin-top: 6.361vw;
  }
  .page {
    padding: 4.066vw 0 10.957vw;
    padding-bottom: 20vw;
    background-color: #fff;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .group {
    padding: 0 5.852vw 3.817vw 6.87vw;
  }
  .group_2 {
    padding: 3.817vw 0 6.064vw;
  }
  .text {
    color: #181d27;
    font-size: 5.089vw;
    font-family: DM Sans;
    font-weight: 700;
    line-height: 4.799vw;
  }
  .group_1 {
    margin-top: 4.366vw;
  }
  .section {
    padding: 4.071vw 4.071vw 4.071vw 4.071vw;
    filter: drop-shadow(0 1.018vw .509vw #00000040);
    background-color: #00b140;
    border-radius: 1.272vw;
    box-shadow: 0 1.018vw 11.196vw rgba(0, 0, 0, .058823529411764705);
  }
  .image-wrapper {
    padding: .509vw 0 .509vw;
    border-radius: 50%;
    background-image: url('../../images/a4f94e80ecf97f465b26f5a73c429191.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    width: 14.504vw;
    height: 14.504vw;
  }
  .image {
    border-radius: 50%;
    width: 13.486vw;
    height: 13.486vw;
  }
  .text_2 {
    color: #fff;
    font-size: 3.562vw;
    font-family: DM Sans;
    font-weight: 700;
    line-height: 3.392vw;
  }
  .section_2 {
    padding: 6.107vw 4.071vw 6.616vw 4.071vw;
    background-color: #fff;
    border-radius: 4.835vw;
    box-shadow: 0 1.018vw 11.196vw rgba(0, 0, 0, .058823529411764705);
  }
  .image_2 {
    border-radius: 50%;
    width: 10.178vw;
    height: 10.178vw;
  }
  .font_2 {
    font-size: 3.308vw;
    font-family: DM Sans;
    line-height: 3.069vw;
    color: #181d27;
  }
  .text_4 {
    line-height: 3.079vw;
  }
  .font {
    font-size: 2.799vw;
    font-family: DM Sans;
    line-height: 2.621vw;
    color: #ababab;
  }
  .text_3 {
    color: #d7d7d7;
    line-height: 2.58vw;
  }
  .image_4 {
    width: .509vw;
    height: 2.036vw;
  }
  .image_3 {
    width: 1.781vw;
    height: 3.053vw;
  }
  .image_5 {
    width: 10.178vw;
    height: 10.178vw;
  }
  .text_6 {
    line-height: 3.066vw;
  }
  .text_7 {
    line-height: 2.603vw;
  }
  .text_8 {
    line-height: 2.601vw;
  }
  .text_9 {
    line-height: 3.074vw;
  }
  .text_10 {
    line-height: 2.606vw;
  }
  .text_11 {
    color: #555;
    line-height: 3.051vw;
  }
  .text_12 {
    line-height: 2.595vw;
  }
  .text_13 {
    margin-top: 5.656vw;
    font-size: 3.562vw;
    line-height: 3.293vw;
    opacity: .8;
  }
  .section_3 {
    padding: 4.326vw 4.071vw 4.326vw 4.071vw;
    background-color: #fff;
    border-radius: 5.089vw;
    box-shadow: 0 1.018vw 11.196vw rgba(0, 0, 0, .058823529411764705);
  }
  .text_14 {
    line-height: 12px;
  }
  .equal-division {
    padding: 0 4.186vw;
  }
  .group_3 {
    flex: 1 1 18.272vw;
  }
  .group_4 {
    padding: 1.02vw 0 1.511vw;
  }
  .image_6 {
    width: 6.399vw;
    height: 6.399vw;
  }
  .font_3 {
    font-size: 3.308vw;
    font-family: Roboto;
    line-height: 2.621vw;
    color: #b9bcbe;
  }
  .text_15 {
    font-size: 3.053vw;
    line-height: 2.807vw;
  }
  .group_5 {
    padding: 1.02vw 0 1.501vw;
  }
  .text_16 {
    font-size: 3.053vw;
    line-height: 2.83vw;
  }
  .group_6 {
    padding: 1.018vw 0 1.506vw;
  }
  .text_17 {
    font-size: 3.053vw;
    line-height: 2.822vw;
  }
  .group_7 {
    padding: 1.02vw 0 1.517vw;
  }
  .text_18 {
    font-size: 3.053vw;
    line-height: 2.812vw;
  }
  .group_8 {
    padding: 1.018vw 0 1.509vw;
  }
  .text_19 {
    color: #00b140;
    font-size: 3.053vw;
    line-height: 2.835vw;
  }
</style>