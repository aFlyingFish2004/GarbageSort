<script setup>
  import { useRouter } from 'vue-router';
  import { ref, reactive, onMounted } from 'vue';
  import { account } from '@/api/api';
  import { fetchMessage, fetchImage, uploadAvatar } from '@/api/api';

  const props = defineProps({});

  const data = reactive({});

  const router = useRouter();

  const name = ref('')
  const input_name = ref('')
  const f_name = ref('')
  const phone = ref('')
  const sex = ref('')
  const birthday = ref('')
  const email = ref(localStorage.getItem('userEmail') || '');
  const avatar_url = ref('')
  const avatar = ref('')

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


  function onClick() {
    router.push({ name: 'my' });
  }

  function onClick_1() {
    account(input_name.value, email.value)
      .then(response => {
        console.log('更新成功:', response.data);
        router.push({ name: 'my' });
      })
      .catch(error => {
          console.error('更新失败:', error.response.data);
      });
    // router.push({ name: 'my' });
  }

  function onClick_2() {
    router.push({ name: 'home' });
  }

  function changeAvatar() {
  document.querySelector('input[type="file"]').click();
}

async function handleFileChange(event) {
  const file = event.target.files[0];
  if (!file) return;

  try {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('email', email.value);
    const response = await uploadAvatar(formData);
    console.log('上传成功:', response.data);
    await fetchUserMessage();
    fetchAndDisplayImage(avatar_url.value);
  } catch (error) {
    console.error('上传失败:', error);
  }
}


  onMounted(async () => {
    await fetchUserMessage();
    fetchAndDisplayImage(avatar_url.value);
  });
</script>

<template>
  <div class="flex-col justify-start page">
    <div class="flex-col group">
      <div class="flex-row items-center header">
        <input type="file" @change="handleFileChange" ref="fileInput" style="display: none;" />
        <img @click="onClick" src="https://codefun-proj-user-res-1256085488.cos.ap-guangzhou.myqcloud.com/6632313d5a7e3f0310306e22/6635a788bba59d0011c215ac/17147924121604625810.png" class="image">
        <span class="font text ml-125">个人信息</span>
      </div>
      <div class="flex-col group_2">
        <img class="self-center image_2" :src="avatar" @click="changeAvatar" />
        <div class="flex-col items-center self-stretch group_3">
          <span class="text_2">{{ name }}</span>
          <span class="mt-12 font text_3">{{ email }}</span>
        </div>
        <div class="flex-col justify-start items-start self-stretch input view_1">
          <input class="font text_4" v-model="input_name" placeholder="我的昵称" />
        </div>
        <div class="flex-col self-stretch group_4">
          <div class="flex-col justify-start items-start input">
            <input class="font text_4" v-model="f_name" placeholder="我的姓名" />
          </div>
          <div class="mt-28 flex-row items-center input_2">
            <img class="image_3" src="../../images/7220972e79dff0f6349d425eb6404847.png" />
            <div class="ml-16 section"></div>
            <input class="ml-16 font text_5" v-model="phone" placeholder="手机号（中国+86）" />
          </div>
        </div>
        <div class="flex-row justify-between items-center self-stretch group_5">
          <input class="font text_6" v-model="sex" placeholder="选择性别" />
          <img class="image_4" src="../../images/03e6f3565b0b1584e44e8beddde56b23.png" />
        </div>
        <div class="flex-col justify-start items-start self-stretch input view">
          <input class="font text_4" v-model="birthday" placeholder="我的生日" />
        </div>
        <button class="flex-col justify-start items-center self-center text-wrapper_2" @click="onClick_1">
          <span class="text_7">更新</span>
        </button>
      </div>
    </div>
    <!-- 底部导航栏 -->
    <tabBar :select="4" />
  </div>
</template>

<style scoped lang="css">
 input {
  border: none;
  background: none;
  padding: 0;
  width: 60vw;
}
input::placeholder {
  color: #555
}
input:focus {
  outline: none;
}
input:focus::placeholder {
  color: transparent;
}
button {
  border: none; 
}
  .ml-125 {
    margin-left: 31.807vw;
  }
  .page {
    background-color: #ffffff;
    padding-bottom: 20vw;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .group {
    padding-bottom: 8.142vw;
    overflow-y: auto;
  }
  .header {
    padding: 8.931vw 8.626vw 4.547vw;
  }
  .image {
    width: 3.562vw;
    height: 2.799vw;
  }
  .group_2 {
    padding: 7.379vw 5.089vw 6.616vw 7.634vw;
  }
  .image_2 {
    border-radius: 50%;
    width: 18.321vw;
    height: 18.321vw;
  }
  .group_3 {
    margin-top: 6.341vw;
  }
  .text_2 {
    color: #181d27;
    font-size: 3.562vw;
    font-family: DM Sans;
    font-weight: 700;
    line-height: 3.392vw;
  }
  .input {
    padding-bottom: 5.448vw;
    border-bottom: .254vw solid #e8e8e8;
  }
  .view_1 {
    margin-top: 16.074vw;
  }
  .group_4 {
    margin-top: 10.059vw;
    border-bottom: .254vw solid #e8e8e8;
  }
  .input_2 {
    padding: 0 2.545vw 2.163vw;
  }
  .image_3 {
    border-radius: .509vw;
    width: 7.634vw;
    height: 5.598vw;
  }
  .font {
    font-size: 3.308vw;
    font-family: DM Sans;
    line-height: 3.069vw;
    color: #555;
  }
  .text_4 {
    margin-left: 4.204vw;
  }
  .text_3 {
    color: #ababab;
    line-height: 3.109vw;
  }
  .text {
    color: #181d27;
    font-size: 3.562vw;
    line-height: 3.316vw;
  }
  .section {
    background-color: rgba(199, 202, 211, .4);
    width: .254vw;
    height: 9.415vw;
  }
  .text_5 {
    line-height: 3.145vw;
  }
  .group_5 {
    margin-top: 10.071vw;
    padding: 0 4.071vw 5.448vw 4.221vw;
    border-bottom: .254vw solid #e8e8e8;
  }
  .text_6 {
    line-height: 3.056vw;
  }
  .image_4 {
    width: 2.29vw;
    height: 1.272vw;
  }
  .view {
    margin-top: 10.059vw;
  }
  .text-wrapper_2 {
    margin-top: 9.288vw;
    padding: 5.481vw 0 4.715vw;
    background-color: #00b140;
    border-radius: 3.817vw;
    width: 66.112vw;
  }
  .text_7 {
    color: #fff;
    font-size: 4.071vw;
    font-family: DM Sans;
    font-weight: 700;
    line-height: 3.799vw;
    opacity: .909;
  }
  .section_2 {
    padding: 3.415vw 0 3.069vw;
    overflow: hidden;
    background-image: url('../../images/4929bbe2a8eb6089d4bacf58dbbaada5.png');
    background-size: 100% 100%;
  }
  .equal-division {
    padding: 0 4.186vw;
  }
  .group_6 {
    flex: 1 1 18.272vw;
  }
  .group_1 {
    padding: 1.02vw 0 1.511vw;
  }
  .image_5 {
    width: 6.399vw;
    height: 6.399vw;
  }
  .font_2 {
    font-size: 3.308vw;
    font-family: Roboto;
    line-height: 3.069vw;
    color: #b9bcbe;
  }
  .text_8 {
    font-size: 3.053vw;
    line-height: 2.807vw;
  }
  .group_7 {
    padding: 1.02vw 0 1.501vw;
  }
  .text_9 {
    font-size: 3.053vw;
    line-height: 2.83vw;
  }
  .group_8 {
    padding: 1.018vw 0 1.506vw;
  }
  .text_10 {
    font-size: 3.053vw;
    line-height: 2.822vw;
  }
  .group_9 {
    padding: 1.02vw 0 1.517vw;
  }
  .text_11 {
    font-size: 3.053vw;
    line-height: 2.812vw;
  }
  .group_10 {
    padding: 1.018vw 0 1.509vw;
  }
  .text_12 {
    color: #00b140;
    font-size: 3.053vw;
    line-height: 2.835vw;
  }
</style>