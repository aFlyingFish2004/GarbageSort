<script setup>
import { useRouter } from 'vue-router';
// import { ref, reactive, onMounted } from 'vue';

const tabList = [{
  text: "主页",
  iconPath: "/src/images/xiyang098/home.png",
  selectedIconPath: "/src/images/xiyang098/home_active.png"
}, {
  text: "搜索",
  iconPath: "/src/images/xiyang098/search.png",
  selectedIconPath: "/src/images/xiyang098/search_active.png"
}, {
  text: "拍照",
  iconPath: "/src/images/xiyang098/photograph.png",
  selectedIconPath: "/src/images/xiyang098/photograph_active.png"
}, {
  text: "社区",
  iconPath: "/src/images/xiyang098/community.png",
  selectedIconPath: "/src/images/xiyang098/community_active.png"
}, {
  text: "我的",
  iconPath: "/src/images/xiyang098/my.png",
  selectedIconPath: "/src/images/xiyang098/my_active.png"
},]

const props = defineProps({
  select: {
    type: Number,
    required: true, // 如果 prop 是必需的，可以添加 required 属性  
    // default: 0, // 如果不是必需的，可以提供一个默认值  
  },
});
const router = useRouter();

function toSelect(index) {
  if (props.select !== index) {
    switch (index) {
      case 0:
        router.push({ name: 'home' });
        break;
      case 1:
        router.push({ name: 'search' });
        break;
      case 2:
        router.push({ name: 'photograph' });
        break;
      case 3:
        router.push({ name: 'community' });
        break;
      case 4:
        router.push({ name: 'my' });
        break;
    }

  }
}


</script>


<template>
  <div class="tabbar">
    <div class="tabbar-item" @click="toSelect(index)" v-for="(item, index) in tabList" :key="index">
      <img class="img-icon" :src="props.select === index ? item.selectedIconPath : item.iconPath">
      <text :style="{ color: props.select === index ? '#00b140' : '' }">{{ item.text }}</text>
    </div>
  </div>
</template>



<style scoped lang="css">
.tabbar {
  width: 100%;
  display: flex;
  background-color: #fff;
  position: fixed;
  bottom: 0;
  /* height: 17vw; */

  /* 避开不可见区域 */
  /* padding-bottom: env(safe-area-inset-bottom); */
  padding-bottom: 2vw;
  padding-top: 2vw;

  border-top: 2px solid #f3f3f3;
}

.tabbar-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #8a8a8a;

  font-size: 3vw;
}

.tabbar-item .img-icon {
  width: 6.3vw;
  height: 6.3vw;
}
</style>