<script setup>
  import { useRouter } from 'vue-router';
  import { ref, reactive, onMounted } from 'vue';
  import { login } from '@/api/api';

  const props = defineProps({});

  const data = reactive({});

  const router = useRouter();

  const email = ref('');
  const password = ref('')

  function onClick() {
    login(email.value, password.value)
        .then(response => {
            console.log('Login successful:', response.data);
            router.push({ name: 'home' });
        })
        .catch(error => {
            console.error('Login failed:', error.response.data);
            // Handle login failure
        });
  }

  function onClick_1() {
    router.push({ name: 'sign_up' });
  }
  
</script>

<template>
  <div class="flex-col page">
    <div class="flex-col items-center self-stretch">
      <img class="logo" src="../../images/2e924cfa7e69e8a5e3621dd97abfa015.png" />
      <span class="mt-8 login_text">账号登录</span>
    </div>
    <div class="flex-col self-stretch group">
      <span class="self-start font">邮箱</span>
      <div class="mt-12 flex-col justify-start items-start self-stretch text-wrapper">
        <input class="font_2 text_3 text_4" type="text" v-model="email" placeholder="ex: jon.smith@email.com" />
      </div>
      <span class="mt-12 self-start font">密码</span>
      <div class="mt-12 flex-col justify-start items-start self-stretch text-wrapper">
        <input class="font_2 text_3 text_4" type="password" v-model="password" placeholder="Password" />
      </div>
    </div>
    <button class="flex-col justify-start items-center self-stretch login_button" @click="onClick">
      <span class="text_7">登录</span>
    </button>
    <span class="self-center font_2 text_8">或通过以下方式</span>
    <div class="flex-row equal-division">
      <img class="image_1" src="../../images/e2afafdca77b5918b74fa05b6e854937.png" />
      <img class="image_1" src="../../images/ac1330c9ffa321a66ada30c407776177.png" />
      <img class="image_1" src="../../images/09c9d108691749d63702ca11310fcd83.png" />
    </div>
    <div class="flex-row justify-center self-stretch group_2">
      <span class="font_2">还没有账号？</span>
      <span class="font_2 text_9 ml-9" @click="onClick_1">注册我的账号</span>
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
  .ml-9 {
    margin-left: 2.29vw;
  }
  .page {
    padding: 11.45vw 13.232vw 43.924vw 13.486vw;
    background-color: #fff;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100%;
  }
  .logo {
    width: 38.422vw;
    height: 38.422vw;
  }
  .login_text {
    color: #000;
    font-size: 9.16vw;
    font-family: Poppins;
    font-weight: 600;
    line-height: 8.651vw;
  }
  .group {
    margin-top: 12.71vw;
  }
  .font {
    font-size: 4.071vw;
    font-family: Poppins;
    line-height: 3.771vw;
    color: #6e6e6e;
  }
  .text-wrapper {
    padding: 3.71vw 0 3.079vw;
    background-color: #f9f9f9;
    border-radius: 2.545vw;
    overflow: hidden;
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
  .text_4 {
    margin-left: 3.98vw;
    font-size: 3.817vw;
    line-height: 3.898vw;
  }
  .text-wrapper_2 {
    padding: 4.323vw 0 4.936vw;
    background-color: #f9f9f9;
    border-radius: 2.545vw;
    overflow: hidden;
  }
  .text_6 {
    margin-left: 4.051vw;
    font-size: 3.817vw;
    line-height: 1.427vw;
  }
  .text_7 {
    color: #fff;
    font-size: 4.58vw;
    font-family: Poppins;
    font-weight: 600;
    line-height: 4.305vw;
  }
  .text_8 {
    margin-top: 5.987vw;
  }
  .equal-division {
    align-self: stretch;
    margin-top: 7.29vw;
  }
  .image_1 {
    margin-right: 3.817vw;
    width: 21.883vw;
    height: 10.687vw;
  }
  .group_2 {
    margin-top: 10.305vw;
    padding-left: 2.542vw;
  }
  .text_9 {
    color: #00b140;
    line-height: 3.786vw;
  }
  .login_button {
    margin-top: 9.415vw;
    padding: 3.308vw 0 3.053vw;
    background-color: #00b140;
    border-radius: 2.545vw;
    overflow: hidden;
  }
</style>