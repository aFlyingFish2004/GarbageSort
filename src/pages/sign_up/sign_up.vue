<script setup>
  import { useRouter } from 'vue-router';
  import { ref, reactive, onMounted } from 'vue';

  const props = defineProps({});

  const data = reactive({});

  const router = useRouter();

  const name = ref('')
  const email = ref('')
  const password = ref('')
  const confirmPpassword = ref('')
  const isChecked = ref(false)

  function onClick() {
    router.back();
  }

  function onClick_1() {
    router.push({ name: 'log_in' });
  }

  function onClick_2() {
    router.push({ name: 'log_in' });
  }
</script>

<template>
  <div class="flex-col page">
    <div class="flex-col">
      <div class="flex-row justify-between self-stretch">
        <img class="self-start return" src="../../images/655f6c4b053c90cca35c24d96cb02958.png" @click="onClick" />
        <img class="logo" src="../../images/1a914daca29a478bd3f03af277cfab3a.png" />
      </div>
      <span class="self-center signup_text mt-17">注册账号</span>
    </div>
    <div class="flex-col group">
      <span class="self-start font text_2">姓名</span>
      <div class="flex-col justify-start items-start self-stretch text-wrapper_1">
        <input class="font_2 text_3 text_4" type="text" v-model="name" placeholder="ex: jon smith" />
      </div>
      <span class="self-start font text_5">邮箱</span>
      <div class="flex-col justify-start items-start self-stretch text-wrapper_1">
        <input class="font_2 text_3 text_4" type="text" v-model="email" placeholder="ex: jon.smith@email.com" />
      </div>
      <span class="self-start font text_5">密码</span>
      <div class="flex-col justify-start items-start self-stretch text-wrapper_1">
        <input class="font_2 text_3 text_4" type="password" v-model="password" placeholder="Password" />
      </div>
      <span class="self-start font text_5">确认密码</span>
      <div class="flex-col justify-start items-start self-stretch text-wrapper_1">
        <input class="font_2 text_3 text_4" type="password" v-model="confirmPpassword" placeholder="Password" />
      </div>
      <div class="flex-row self-stretch group_2">
          <input type="checkbox" class="group_3" id="checkbox" v-model="isChecked" />
        <div class="group_4 ml-9">
          <label for="checkbox" class="font_4 text_9">我同意</label>
          <span class="font_4 text_10">用户协议</span>
          <label for="checkbox" class="text_11">.</label>
        </div>
      </div>
      <button class="flex-col justify-start items-center self-stretch text-wrapper_2" @click="onClick_1">
        <span class="text_12">注册</span>
      </button>
    </div>
    <div class="flex-col group_5">
      <span class="self-center font_2">或通过以下方式</span>
      <div class="flex-row button_1 mt-21">
        <img class="image_3" src="../../images/cf783c67a0a27763f617854a37e2395a.png" />
        <img class="image_3" src="../../images/ac1330c9ffa321a66ada30c407776177.png" />
        <img class="image_3" src="../../images/cbf3d74dd6a8afd77105d936b7d1c77d.png" />
      </div>
    </div>
    <div class="flex-row group_6">
      <span class="font_2">已经有了账号？</span>
      <span class="ml-6 font_2 text_13" @click="onClick_2">登录</span>
    </div>
  </div>
</template>

<style scoped lang="css">
 input {
  border: none;
  background: none;
  padding: 0;
  width: 60vw;
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
  .mt-17 {
    margin-top: 4.326vw;
  }
  .ml-9 {
    margin-left: 2.29vw;
  }
  .mt-21 {
    margin-top: 5.344vw;
  }
  .page {
    padding: 9.415vw 9.16vw 26.112vw 12.977vw;
    background-color: #fff;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .return {
    margin-top: 5.598vw;
    width: 4.835vw;
    height: 2.545vw;
  }
  .logo {
    width: 16.285vw;
    height: 16.285vw;
  }
  .signup_text {
    color: #000;
    font-size: 8.651vw;
    font-family: Poppins;
    font-weight: 600;
    line-height: 8.27vw;
  }
  .group {
    margin-top: 11.74vw;
  }
  .font {
    font-size: 4.071vw;
    font-family: Poppins;
    line-height: 3.771vw;
    color: #6e6e6e;
  }
  .text_2 {
    margin-left: .417vw;
    line-height: 3.766vw;
  }
  .text_5 {
    margin-left: .595vw;
    margin-top: 3.687vw;
    line-height: 3.766vw;
  }
  .text-wrapper_1 {
    margin-right: 4.326vw;
    margin-top: 2.975vw;
    padding: 3.71vw 0 3.079vw;
    background-color: #f9f9f9;
    border-radius: 2.545vw;
    overflow: hidden;
  }
  .text-wrapper {
    margin-right: 4.326vw;
    margin-top: 2.98vw;
  }
  .font_3 {
    font-size: 4.071vw;
    font-family: Poppins;
    line-height: 1.427vw;
    color: #888;
  }
  .group_2 {
    padding: 4.58vw .763vw;
  }
  .group_3 {
    border-radius: .254vw;
    width: 3.308vw;
    height: 3.308vw;
    border-left: .254vw solid #00b140;
    border-right: .254vw solid #00b140;
    border-top: .254vw solid #00b140;
    border-bottom: .254vw solid #00b140;
  }
  .group_4 {
    line-height: 2.845vw;
    height: 2.845vw;
    margin-top: .6vw;
  }
  .font_4 {
    font-size: 3.053vw;
    font-family: Poppins;
    line-height: 2.845vw;
  }
  .text_9 {
    color: #000;
    line-height: 2.822vw;
  }
  .text_10 {
    color: #00b140;
  }
  .text_11 {
    color: #000;
    font-size: 3.053vw;
    font-family: Poppins;
    line-height: .379vw;
  }
  .text-wrapper_2 {
    margin-right: 4.326vw;
    padding: 3.226vw 0 3.109vw;
    background-color: #00b140;
    border-radius: 2.545vw;
    overflow: hidden;
  }
  .text_12 {
    color: #fff;
    font-size: 4.58vw;
    font-family: Poppins;
    font-weight: 600;
    line-height: 4.351vw;
  }
  .group_5 {
    margin-top: 5.987vw;
  }
  .button_1 {
    align-self: stretch;
    margin-right: 4.326vw;
  }
  .image_3 {
    margin-right: 3.817vw;
    width: 21.883vw;
    height: 10.687vw;
  }
  .group_6 {
    margin-top: 6.758vw;
    padding: 0 16.41vw;
  }
  .font_2 {
    font-size: 4.071vw;
    font-family: Poppins;
    line-height: 3.771vw;
    color: #888;
  }
  .text_3 {
    opacity: 0.5;
  }
  .text_1 {
    margin-left: 4.051vw;
    font-size: 3.817vw;
  }
  .text_4 {
    margin-left: 3.982vw;
    font-size: 3.817vw;
    line-height: 3.898vw;
  }
  .text_15 {
    margin-left: 3.982vw;
    font-size: 3.817vw;
    line-height: 3.898vw;
  }
  .text_13 {
    color: #00b140;
    line-height: 3.74vw;
  }
</style>