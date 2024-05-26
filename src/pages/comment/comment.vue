<script>
import axios from 'axios';

export default {
  // ... 其他选项 ...  
  data() {
    return {
      comments: [],
      newComment: {  
        content: '',  
        email: '', // 假设这是从Vuex、localStorage或其他地方获取的当前用户email  
      },  
      currentUserEmail: '2531094816@qq.com', // 这里只是一个示例，你需要根据实际情况获取当前用户email  
    };
  },
  async created() {
    try {
      const response = await axios.get('http://localhost:8000/api/comments/'); // 发送GET请求到Django后端  
      this.comments = response.data; // 将响应数据赋值给组件的comments属性  
    } catch (error) {
      console.error('Error fetching comments:', error);
    }
  },

  
  

};

</script>


<template>

  <ul>
    <li v-for="(item, index) in comments" :key="item.id">{{ index }}-{{ item.content }}-{{ item.user_name }}-{{ item.like }}-{{ item.avatar_url }}-{{ item.email }}</li>
  </ul>


</template>



<style></style>