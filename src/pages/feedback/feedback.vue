<script>
import { useRouter } from 'vue-router';
import { reactive, onMounted } from 'vue';


export default {
  data() {
    return {
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
      selectedBig: '',    // 除初始化，其他为数字，index
      selectedSmall: '',  // 字符串，小类名
      isFormValid: false,
      name: '',
    };
  },
  watch: {
    selectedBig(newVal) {
      this.selectedSmall = ''; // 重置小类选择  
    },
    selectedSmall(newVal) {
      this.isFormValid = this.selectedBig !== '' && newVal !== '' && this.name !== ''; // 当小类也选择后，检查表单是否有效  
    },
    name() {
      this.isFormValid = this.selectedBig !== '' && this.selectedSmall !== '' && this.name !== '';
    }
  },
  methods: {
    submitForm() {
      // 提交表单的逻辑  数字和字符串
      console.log('Form submitted:', this.selectedBig, this.selectedSmall);
      this.selectedBig = ''    // 除初始化，其他为数字，index
      this.selectedSmall = ''  // 字符串，小类名
      this.name = ''
      this.$router.push({ name: 'recognize_result' });
    },
  },
  mounted() {
    // 组件加载时，检查是否至少选择了一个大类（在这个示例中，默认为false）  
    this.isFormValid = false;
  },
};
</script>

<template>
  <div class="feedback">
    <!-- 名称 -->
    <div class="name">
      <div class="name-hint">该物品是什么？</div>
      <div class="block">
        <span class="must-red">*</span>
        <input class="name-input" type="text" v-model="name" placeholder="请填入物品名称">
      </div>
    </div>
    <!-- 类别 -->
    <div class="category">
      <div class="category-hint">该物品属于什么分类？</div>
      <!-- 大类选择器 -->
      <div class="block">
        <span class="must-red">*</span>
        <select v-model="selectedBig" @change="updateSmallOptions">
          <option value="" disabled>请选择大类</option>
          <option v-for="(big, index) in bigSort" :key="index" :value="index">{{ big }}</option>
        </select>
      </div>

      <!-- 小类选择器 -->
      <div class="block">
        <span class="must-red">*</span>
        <select v-model="selectedSmall" :disabled="selectedBig === null">
          <option value="" disabled>请选择小类</option>
          <option v-for="(small, index) in smallSort[selectedBig]" :key="index" :value="small">{{ small }}</option>
        </select>
      </div>

    </div>

    <!-- 提交按钮和提示 -->
    <button @click="submitForm" :disabled="!isFormValid">提交</button>


  </div>

</template>

<style scoped lang="css">
.feedback {
  padding: 5vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff;
}

.feedback>div {
  margin-bottom: 5vw;
  width: 100%;
}

.name-hint,
.category-hint {
  padding: 3vw;
  margin-top: 5vw;
  text-align: center;
  font-size: 4.2vw;
  background-color: #00b140;
  color: white;
  border: none;
  /* height: 10vw; */
  /* line-height: 10vw; */
  width: auto;
  max-width: 100%;
  border-radius: 4vw;
  box-sizing: border-box;

  box-shadow: 0 1vw 1vw rgba(0, 0, 0, .25);
}

.block {
  display: flex;

}

.name-input,
select {
  width: 97%;
  /* height: 8vw; */
  font-size: 4vw;
  border: 1px solid #b8b8b8;
  border-radius: 1vw;
  box-sizing: border-box;
  padding: 2vw;
  margin-top: 5vw;
  /* 适当的垂直间距 */
}

select {
  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;
  background: url('../../images/xiyang098/open.png') no-repeat right 3vw center / 3.5vw 3.5vw;
}

.must-red {
  color: red;
  font-size: 4vw;
  /* 红色星号 */
}

button {
  padding: 3vw;
  margin-top: 5vw;
  /* height: 10vw; */
  width: 40%;
  border-radius: 6vw;
  font-size: 4.5vw;
  background-color: #00b140;
  color: white;
  border: none;
  box-shadow: 0 1vw 1vw rgba(0, 0, 0, .25);
  cursor: pointer;
}

button:disabled {
  opacity: 0.5;
  /* 禁用时降低透明度 */
  cursor: not-allowed;
  /* 禁用时鼠标悬停时显示禁止图标 */
}
</style>