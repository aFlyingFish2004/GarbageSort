<script setup>
import { useRouter, useRoute } from 'vue-router';
import { reactive, onMounted, ref } from 'vue';

// import { eventBus } from '../../main';


const props = defineProps({});

const data = reactive({
  search: '',
  index: 0,
  bigSort: ['可回收垃圾', '有害垃圾', '厨余垃圾', '其他垃圾'],
  smallSort: [
    [ // 可回收垃圾
      '乒乓球拍', '书', '保温杯', '保鲜盒', '信封', '充电头', '充电宝', '充电线', '八宝粥罐', '刀', '剃须刀片', '剪刀', '勺子',
      '单肩包手提包', '卡', '叉子', '变形玩具', '台历', '台灯', '吹风机', '呼啦圈', '地球仪', '地铁票', '垫子', '塑料瓶',
      '塑料盆', '奶盒', '奶粉罐', '奶粉罐铝盖', '尺子', '帽子', '废弃扩声器', '手提包', '手机', '手电筒', '手链', '打印机墨盒',
      '打气筒', '护肤品空瓶', '报纸', '拖鞋', '插线板', '搓衣板', '收音机', '放大镜', '易拉罐', '暖宝宝', '望远镜', '木制切菜板',
      '木制玩具', '木质梳子', '木质锅铲', '枕头', '档案袋', '水杯', '泡沫盒子', '灯罩', '烟灰缸', '烧水壶', '热水瓶', '玩偶',
      '玻璃器皿', '玻璃壶', '玻璃球', '电动剃须刀', '电动卷发棒', '电动牙刷', '电熨斗', '电视遥控器', '电路板', '登机牌', '盘子',
      '碗', '空气加湿器', '空调遥控器', '纸牌', '纸箱', '罐头瓶', '网卡', '耳套', '耳机', '耳钉耳环', '芭比娃娃', '茶叶罐',
      '蛋糕盒', '螺丝刀', '衣架', '袜子', '裤子', '计算器', '订书机', '话筒', '购物纸袋', '路由器', '车钥匙', '量杯', '钉子',
      '钟表', '钢丝球', '锅', '锅盖', '键盘', '镊子', '鞋', '餐垫', '鼠标'
    ],
    [ // 有害垃圾
      'LED灯泡', '保健品瓶', '口服液瓶', '指甲油', '杀虫剂', '温度计', '滴眼液瓶', '玻璃灯管', '电池', '电池板', '碘伏空瓶',
      '红花油', '纽扣电池', '胶水', '药品包装', '药片', '药膏', '蓄电池', '血压计'
    ],
    [ // 厨余垃圾
      '八宝粥', '冰糖葫芦', '咖啡渣', '哈密瓜', '圣女果', '巴旦木', '开心果', '普通面包', '板栗', '果冻', '核桃', '梨', '橙子',
      '残渣剩饭', '汉堡', '火龙果', '炸鸡', '烤鸡烤鸭', '牛肉干', '瓜子', '甘蔗', '生肉', '番茄', '白菜', '白萝卜', '粉条',
      '糕点', '红豆', '肠(火腿)', '胡萝卜', '花生皮', '苹果', '茶叶', '草莓', '荷包蛋', '菠萝', '菠萝包', '菠萝蜜', '蒜', '薯条',
      '蘑菇', '蚕豆', '蛋', '蛋挞', '西瓜皮', '贝果', '辣椒', '陈皮', '青菜', '饼干', '香蕉皮', '骨肉相连', '鸡翅'
    ],
    [ // 其他垃圾
      'PE塑料袋', 'U型回形针', '一次性杯子', '一次性棉签', '串串竹签', '便利贴', '创可贴', '厨房手套', '口罩', '唱片', '图钉',
      '大龙虾头', '奶茶杯', '干果壳', '干燥剂', '打泡网', '打火机', '放大镜', '毛巾', '涂改带', '湿纸巾', '烟蒂', '牙刷', '百洁布',
      '眼镜', '票据', '空调滤芯', '笔及笔芯', '纸巾', '胶带', '胶水废包装', '苍蝇拍', '茶壶碎片', '餐盒', '验孕棒', '鸡毛掸'
    ]
  ],
  searchResults: [],
  isSearch: false,    // 判断现在右侧显示的是否是搜索结果

});


// eventBus.on('voice-recognized', (text_result) => {
//   data.search = text_result;
//   this.toSearch();
// });


// beforeUnmount() {
//   // 在组件卸载前移除事件监听器，避免内存泄漏  
//   eventBus.off('voice-recognized');
// }


function getSort(index) {
  data.index = index
  data.isSearch = false   // 当点击左侧大类切换大类渲染
}

const router = useRouter();
const goBack = () => {
  router.back();
};


function toSearch() {
  // console.log('我是toSearch1');
  // console.log(data.search);
  let { smallSort, bigSort, searchResults } = data;
  data.isSearch = true;   // 当点击搜索图标，切换搜索结果渲染
  searchResults = [];     // 首先置空搜索结果，防止数据累积
  for (let i = 0; i < smallSort.length; i++) {
    // 遍历当前分类下的所有项  
    for (let j = 0; j < smallSort[i].length; j++) {
      // 如果当前项包含搜索关键词  
      if (smallSort[i][j].includes(data.search)) {
        // 将当前项及其所属的大类一起放入结果数组中  
        // 注意：这里假设你想同时存储项和它的分类信息  
        searchResults.push({
          bigIndex: i,
          category: bigSort[i], // 注意这里的索引 i 应该对应 bigSort 的索引，但这里假设 smallSort 的索引直接对应 bigSort  
          name: smallSort[i][j]
        });
      }
    }
  }
  // console.log('我是toSearch2');
  data.searchResults = searchResults;
  // console.log(data.searchResults[1].name);

}

const search = ref('');
console.log('我是search');

onMounted(() => {
  const route = useRoute();
  const textResult = route.query.textResult;
  console.log(textResult);
  if (textResult) {
    search.value = textResult;
    data.search = textResult;

    toSearch(); // 立即执行搜索  
  }
});

</script>

<template>
  <div class="container">
    <!-- <img class="image" src="../../images/xiyang098/5f75d39751dd7fc3326ebb162726d3fa.png" /> -->
    <!-- 顶部 -->
    <div class="top">
      <!-- 返回 -->
      <img class="back" @click="goBack" src="../../images/xiyang098/a0826ba5fc994a76749cd5cb2d23b553.png" alt="">
      <!-- 搜索框 -->
      <div class="search">
        <img class="search-icon" @click="toSearch" src="../../images/xiyang098/34d0ae1d39711ae4276b0c018b950e7f.png"
          alt="">
        <input type="text" @keyup.enter="toSearch" v-model.trim="data.search" placeholder="搜索垃圾类别">
      </div>
    </div>

    <!-- 分类 -->
    <div class="classification">
      <!-- 左侧大类 -->
      <div class="left">
        <div class="left-item" :class="{ 'active': (data.index === index && !data.isSearch) }"
          v-for="(item, index) in data.bigSort" :key="index" @click="getSort(index)">
          <p>{{ item }} ></p>
        </div>
        <img class="logo" src="../../images/xiyang098/d5e7f13786175f196321b6781789453e.png" alt="">
      </div>

      <!-- 右侧小类 -->
      <!-- 渲染搜索结果 -->
      <div class="right" v-if="data.isSearch">
        <div class="right-item" v-for="(item, index) in data.searchResults" :key="index">
          <span>{{ item.name }}</span>
          <span class="right-class" :class="{
            'blue': item.bigIndex === 0,
            'red': item.bigIndex === 1,
            'green': item.bigIndex === 2,
            'grey': item.bigIndex === 3
          }">
            {{ item.category }}
          </span>
        </div>
      </div>
      <!-- 渲染大类结果 -->
      <div class="right" v-else>
        <div class="right-item" v-for="(item, index) in data.smallSort[data.index]" :key="index">
          <span>{{ item }}</span>
          <span class="right-class" :class="{
            'blue': data.index === 0,
            'red': data.index === 1,
            'green': data.index === 2,
            'grey': data.index === 3
          }">
            {{ data.bigSort[data.index] }}
          </span>
        </div>
      </div>
    </div>

    <!-- 底部导航栏 -->
    <tabBar :select="1" />
  </div>

</template>



<style scoped lang="css">
.container {
  background-color: #f3f3f3;
  min-height: 100vh;
  width: 100%;
  padding-bottom: 20vw;
}

.top {
  display: flex;
  align-items: center;
  padding: 4vw 8vw 3vw 5vw;
  padding-right: 10vw;
}

.top .back {
  margin-right: 5vw;
  width: 3.562vw;
  height: 2.799vw;
}

.top .search {
  display: flex;
  align-items: center;
  padding: 0 3vw;
  flex: 1;
  height: 9vw;
  background-color: #fff;
  border-radius: 4.5vw;
}

.top .search .search-icon {
  /* margin-left: 3vw; */
  margin-right: 2vw;
  width: 4vw;
  height: 4vw;
}

.top .search input {
  border: none;
  outline: none;
  width: 0;
  flex: 1;
  font-size: 3.8vw;
}

.top .search input::placeholder {
  color: #b9bcbe;
}


/* 分类 */
.classification {
  display: flex;
}

.classification .left {
  position: relative;
  width: 30vw;
  height: 100vw;
}

.classification .left .left-item {
  height: 11.5vw;
  font-size: 4vw;
  line-height: 11.5vw;
  padding-right: 3vw;
  text-align: end;
}

.classification .left-item p {
  margin: 0;
}

.active {
  background-color: #fff;
  color: #00b140;
}

.logo {
  position: absolute;
  bottom: 10vw;
  left: 50%;
  transform: translateX(-50%);
  width: 20vw;
  height: 20vw;
}

/* 右边细分 */
.classification .right {
  padding: 2vw;
  padding-top: 0;
  flex: 1;
}

.classification .right .right-item {
  padding: 1vw 2vw;
  margin-bottom: 2vw;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 11vw;
  font-size: 3.817vw;
  line-height: 11vw;
  color: #888888;
  background-color: #fff;
  border-radius: 2vw;

  filter: drop-shadow(0vw 1.018vw 0.509vw #00000040);

}

.right-item .right-class {
  text-align: center;
  line-height: 6.6vw;
  font-size: 3.2vw;
  color: #fff;
  width: 20vw;
  height: 6.6vw;
  border-radius: 3.3vw;
}

.blue {
  background-color: #005dad;
}

.red {
  background-color: #e50015;
}

.green {
  background-color: #009a44;
}

.grey {
  background-color: #707070;
}
</style>