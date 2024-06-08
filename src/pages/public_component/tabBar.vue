<script setup>
import { useRouter } from 'vue-router'

// 引入图标文件
import homeIcon from '@/images/xiyang098/home.png'
import homeActiveIcon from '@/images/xiyang098/home_active.png'
import searchIcon from '@/images/xiyang098/search.png'
import searchActiveIcon from '@/images/xiyang098/search_active.png'
import photographIcon from '@/images/xiyang098/photograph.png'
import photographActiveIcon from '@/images/xiyang098/photograph_active.png'
import communityIcon from '@/images/xiyang098/community.png'
import communityActiveIcon from '@/images/xiyang098/community_active.png'
import myIcon from '@/images/xiyang098/my.png'
import myActiveIcon from '@/images/xiyang098/my_active.png'

const tabList = [{
  text: "主页",
  iconPath: homeIcon,
  selectedIconPath: homeActiveIcon
}, {
  text: "搜索",
  iconPath: searchIcon,
  selectedIconPath: searchActiveIcon
}, {
  text: "拍照",
  iconPath: photographIcon,
  selectedIconPath: photographActiveIcon
}, {
  text: "社区",
  iconPath: communityIcon,
  selectedIconPath: communityActiveIcon
}, {
  text: "我的",
  iconPath: myIcon,
  selectedIconPath: myActiveIcon
}]

const props = defineProps({
  select: {
    type: Number,
    required: true
  }
})

const router = useRouter()

function toSelect(index) {
  if (props.select !== index) {
    switch (index) {
      case 0:
        router.push({ name: 'home' })
        break
      case 1:
        router.push({ name: 'search' })
        break
      case 2:
        router.push({ name: 'photograph' })
        break
      case 3:
        router.push({ name: 'community' })
        break
      case 4:
        router.push({ name: 'my' })
        break
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
