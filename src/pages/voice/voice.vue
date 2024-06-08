<script setup>
import { useRouter } from 'vue-router';
import { reactive, onMounted } from 'vue';

// 我
import axios from 'axios';
// // 在 voice.vue 中  
// import { eventBus } from '../../main';  
// eventBus.emit('voice-recognized', text_result);  
// //

const props = defineProps({});


const data = reactive({
  flag: false,
  text_result: '',
});

const router = useRouter();
const goBack = () => {
  router.back();
};
const navigateToSearch = (text_result) => {
  // 使用查询参数传递数据  
  router.push({ name: 'search', query: { textResult: text_result.trim() } });
};

function startAnimation() {
  data.flag = !data.flag

  axios.post('https://10.122.210.57:8000/api/run-script/', { flag: true })
    .then(response => {
      // console.log(response);
      // console.log(response.data);
      console.log(response.data.output);
      data.text_result = response.data.output
      // console.log(111);
      // 假设这是你从后端获得的识别结果  
      const text_result = data.text_result;
      navigateToSearch(text_result);

      // console.log(text_result);
    })
    .catch(error => {
      console.error('Error: ', error);
    });
}

</script>

<template>

  <div class="container">
    <!-- 返回 -->
    <img class="back" @click="goBack" src="../../images/xiyang098/a0826ba5fc994a76749cd5cb2d23b553.png" alt="">

    <!-- 中心话筒 -->
    <div>
      <!-- 圆波 -->
      <div class="ripple1 center" :style="{ animation: data.flag ? '' : 'none' }"></div>
      <div class="ripple2 center" :style="{ animation: data.flag ? '' : 'none' }"></div>
      <div class="ripple3 center" :style="{ animation: data.flag ? '' : 'none' }"></div>
      <!-- 话筒 -->
      <div class="microphone-bg center" @click="startAnimation">
        <img class="microphone" src="../../images/xiyang098/ef4f0a509f33cafaca4f470d1f5992d9.png" alt="">
      </div>

    </div>


    <!-- 底部波纹 -->
    <div>
      <img class="crinkle1 bottom" :style="{ animation: data.flag ? '' : 'none' }"
        src="../../images/xiyang098/crinkle1.png" alt="">
      <img class="crinkle2 bottom" :style="{ animation: data.flag ? '' : 'none' }"
        src="../../images/xiyang098/crinkle2.png" alt="">
      <img class="crinkle3 bottom" :style="{ animation: data.flag ? '' : 'none' }"
        src="../../images/xiyang098/crinkle3.png" alt="">
    </div>
  </div>


</template>

<style scoped lang="css">
.container {
  position: relative;
  min-height: 100vh;
  background-image: linear-gradient(180deg, #d7fdf3 59.4%, #c6f8d8d4 99.6%);
  overflow: hidden;
}

.back {
  margin-top: 8vw;
  margin-left: 5vw;
  width: 3.562vw;
  height: 2.799vw;
}


/* 中心话筒 */
.center {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, calc(-50% - 20vw));
}

.ripple1 {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 25vw;
  /* 初始波纹大小的两倍，因为我们会缩小到一半 */
  height: 25vw;
  background: radial-gradient(circle at 50% 50%, transparent 50%, rgba(65, 204, 112, 0.6) 60%, transparent 70%) center no-repeat;
  border-radius: 50%;
  transform: translate(-50%, calc(-50% - 20vw)) scale(0.5);
  /* 初始大小设为容器的一半 */
  opacity: 1;
  animation: rippleEffect 2s ease-out infinite alternate;
}

.ripple2 {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 25vw;
  /* 初始波纹大小的两倍，因为我们会缩小到一半 */
  height: 25vw;
  background: radial-gradient(circle at 50% 50%, transparent 40%, rgba(65, 204, 112, 0.6) 60%, transparent 70%) center no-repeat;
  border-radius: 50%;
  transform: translate(-50%, calc(-50% - 20vw)) scale(0.5);
  /* 初始大小设为容器的一半 */
  opacity: 1;
  animation: rippleEffect 2s ease-out infinite alternate 2s;
}



@keyframes rippleEffect {
  0% {
    transform: translate(-50%, calc(-50% - 20vw)) scale(0.5);

    background-size: 0% 0%;
  }

  100% {
    transform: translate(-50%, calc(-50% - 20vw)) scale(2);
    /* 扩大到两倍 */

    background-size: 100% 100%;
    /* 波纹扩散到整个元素 */
  }
}

.ripple3 {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20vw;
  /* 初始波纹大小的两倍，因为我们会缩小到一半 */
  height: 20vw;
  background: radial-gradient(circle at 50% 50%, rgba(65, 204, 112, 0.8) 60%, transparent 70%) center no-repeat;
  border-radius: 50%;
  transform: translate(-50%, calc(-50% - 20vw)) scale(0.5);
  /* 初始大小设为容器的一半 */
  opacity: 1;
  animation: rippleSpread 2s ease-out infinite 0.5s;
}

@keyframes rippleSpread {
  0% {
    transform: translate(-50%, calc(-50% - 20vw)) scale(0.5);
    opacity: 1;
    background-size: 0% 0%;
  }

  100% {
    transform: translate(-50%, calc(-50% - 20vw)) scale(5);
    /* 扩大到两倍 */
    opacity: 0;
    background-size: 100% 100%;
    /* 波纹扩散到整个元素 */
  }
}

.microphone-bg {
  background-color: #f0e5e5;
  box-shadow: 0vw 1.018vw 0.763vw #00000040, 0vw -1.018vw 0.763vw #ffffff40, 1.018vw 0vw 1.018vw #ffffff80, -1.018vw 0vw 1.018vw #ffffff80;
  filter: blur(0.127vw);
  border-radius: 50%;
  width: 25vw;
  height: 25vw;
}


.microphone {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 8.142vw;
  height: 12.723vw;

}


/* 底部波纹 */
.bottom {
  position: absolute;
  bottom: 10vw;

}

/* 红线 */
.crinkle1 {
  height: 20vw;
  animation: zoom1 6s linear infinite 0.5s forwards;
}

@keyframes zoom1 {
  0% {
    transform: translateX(-200vw) scaleY(0.5);
    transform-origin: bottom;
  }

  25% {
    transform: translateX(-150vw) scaleY(1.2);
    transform-origin: bottom;
  }

  50% {
    transform: translateX(-100vw) scaleY(0.5);
    transform-origin: bottom;
  }

  75% {
    transform: translateX(-50vw) scaleY(1.2);
    transform-origin: bottom;
  }

  100% {
    transform: translateX(0) scaleY(0.5);
    transform-origin: bottom;
  }
}

/* 蓝线 */
.crinkle2 {
  height: 30vw;
  animation: zoom2 4s linear infinite 0.5s forwards;
}

@keyframes zoom2 {
  0% {
    transform: translateX(0) scaleY(0.8);
    transform-origin: bottom;
  }

  25% {
    transform: translateX(-50vw) scaleY(1.8);
    transform-origin: bottom;
  }

  50% {
    transform: translateX(-100vw) scaleY(0.8);
    transform-origin: bottom;
  }

  75% {
    transform: translateX(-150vw) scaleY(1.8);
    transform-origin: bottom;
  }

  100% {
    transform: translateX(-200vw) scaleY(0.8);
    transform-origin: bottom;
  }
}


/* 灰线 */
.crinkle3 {
  height: 10vw;
  animation: zoom3 3s linear infinite 1s forwards;
}


@keyframes zoom3 {
  0% {
    transform: translateX(0);
    transform-origin: bottom;
  }

  25% {
    transform: translateX(-50vw);
    transform-origin: bottom;
  }

  50% {
    transform: translateX(-100vw);
    transform-origin: bottom;
  }

  75% {
    transform: translateX(-150vw);
    transform-origin: bottom;
  }

  100% {
    transform: translateX(-200vw);
    transform-origin: bottom;
  }
}
</style>