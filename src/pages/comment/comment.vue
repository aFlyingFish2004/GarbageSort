<template>
  <div class="container">
    <!-- 顶部 -->
    <div class="top">
      <!-- 返回 -->
      <img class="back" @click="goBack" :src="backIcon" alt="">
      <!-- 搜索框 -->
      <div class="search">
        <img class="search-icon" @click="toSearch" :src="searchIcon" alt="">
        <input type="text" @keyup.enter="toSearch" v-model.trim="data.search" placeholder="输入评论关键字" class="search-input">
      </div>
    </div>

    <!-- 评论区，搜索结果 -->
    <div v-if="data.search && isSearch">
      <div class="comment" v-for="comment in data.searchResults" :key="comment.id">
        <!-- 左边头像 -->
        <div class="avatar">
          <img class="avatar-img" :src="comment.avatar" alt="">
        </div>
        <!-- 右边其他 -->
        <div class="right">
          <div class="user">
            <p class="nickName">{{ comment.user_name }}</p>
            <p class="pub_time">{{ comment.publish_time }}</p>
          </div>
          <pre class="content">{{ comment.content }}</pre>
          <img :src="comment.isExpanded ? upIcon : downIcon" alt="" @click="toggleContent(comment)" class="updown">

          <div class="icons">
            <img class="love icon"
              :src="comment.liked ? loveActiveIcon : loveIcon" alt=""
              @click="toggleLike(comment.id)">
            <span class="love-count">{{ comment.like_count }}</span>
            <img class="hate icon" :src="hateIcon" alt="">
            <span class="hate-count"></span>
            <img class="forward icon" :src="forwardIcon" alt="">
            <img class="remark icon" :src="remarkIcon" alt="">
          </div>
        </div>
      </div>
    </div>

    <!-- 评论区 -->
    <div v-else>
      <div class="comment" v-for="comment in comments" :key="comment.id">
        <!-- 左边头像 -->
        <div class="avatar">
          <img class="avatar-img" :src="comment.avatar" alt="">
        </div>
        <!-- 右边其他 -->
        <div class="right">
          <div class="user">
            <p class="nickName">{{ comment.user_name }}</p>
            <p class="pub_time">{{ comment.publish_time }}</p>
          </div>
          <pre class="content" :class="{ expanded: comment.isExpanded }">{{ comment.content }}</pre>
          <img :src="comment.isExpanded ? upIcon : downIcon" alt="" @click="toggleContent(comment)" class="updown">

          <div class="icons">
            <img class="love icon"
              :src="comment.liked ? loveActiveIcon : loveIcon" alt=""
              @click="toggleLike(comment.id)">
            <span class="love-count">{{ comment.like_count }}</span>
            <img class="hate icon" :src="hateIcon" alt="">
            <span class="hate-count"></span>
            <img class="forward icon" :src="forwardIcon" alt="">
            <img class="remark icon" :src="remarkIcon" alt="">
          </div>
        </div>
      </div>
    </div>

    <!-- 添加评论的表单 -->
    <form class="submit" @submit.prevent="createComment">
      <span class="total" v-show="true" :style="['transition: all 2s', { opacity: isTotalVisible ? 1 : 0 }]">{{
        `${newComment.length}/200字` }}</span>
      <div class="wrapper" :style="{ height: isTotalVisible ? '22vw' : '17vw' }">
        <i class="avatar-bottom"></i>
        <textarea v-model="newComment" placeholder="请输入评论..." rows="2" @focus="showTotal" @blur="hideTotal"
          maxlength="200"></textarea>
        <button class="submit-btn" type="submit">发布</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';
import { reactive, ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { fetchImage, fetchMessage } from '@/api/api';

// 导入图片资源
import backIcon from '@/images/xiyang098/a0826ba5fc994a76749cd5cb2d23b553.png';
import searchIcon from '@/images/xiyang098/34d0ae1d39711ae4276b0c018b950e7f.png';
import upIcon from '@/images/xiyang098/up.png';
import downIcon from '@/images/xiyang098/down.png';
import loveIcon from '@/images/xiyang098/love.png';
import loveActiveIcon from '@/images/xiyang098/love_active.png';
import hateIcon from '@/images/xiyang098/hate.png';
import forwardIcon from '@/images/xiyang098/forward.png';
import remarkIcon from '@/images/xiyang098/remark.png';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = 'csrftoken';

const comments = ref([]);
const newComment = ref('');

const email = ref(localStorage.getItem('userEmail') || '');

const fetchAndDisplayImage = async (imageName) => {
  try {
    const response = await fetchImage(imageName);
    const blob = await response.data;
    return URL.createObjectURL(blob);
  } catch (error) {
    console.error('Error fetching image:', error);
  }
};

onMounted(async () => {
  await fetchComments();
});

async function fetchComments() {
  try {
    const response = await axios.get('https://garbage.sa1ge.ink/main/comments', { params: { email: email.value } });
    comments.value = response.data.comments;
    comments.value.forEach(async (comment) => {
      try {
        const avatarData = await fetchAndDisplayImage(comment.avatar_url);
        comment.avatar = avatarData;
      } catch (error) {
        console.error(`Error fetching avatar for ${comment.user_name}:`, error);
      }
    });
  } catch (error) {
    console.error('Error fetching comments:', error);
  }
}

async function toggleLike(commentId) {
  try {
    const response = await axios.post('https://garbage.sa1ge.ink/main/toggle_like/', { email: email.value, comment_id: commentId });
    await fetchComments();
    console.log(response.data.message);
  } catch (error) {
    console.error('Error toggling like:', error);
  }
}

const createComment = async () => {
  if (!newComment.value) {
    alert('请输入评论内容！');
    return;
  }
  try {
    await axios.post('https://garbage.sa1ge.ink/main/comments/create/', { email: email.value, content: newComment.value });
    newComment.value = '';
    fetchComments();
  } catch (error) {
    console.error('Error creating comment:', error);
  }
};

const isTotalVisible = ref(false);

function showTotal() {
  isTotalVisible.value = true;
}

function hideTotal() {
  isTotalVisible.value = false;
}

const router = useRouter();
const goBack = () => {
  router.back();
};

const data = reactive({
  search: '',
  searchResults: [],
});

const isSearch = ref(false);

watch(
  () => data.search,
  (newVal, oldVal) => {
    if (newVal === '' && oldVal !== '') {
      isSearch.value = false;
    }
  }
);

function toSearch() {
  if (!data.search) return;
  let { searchResults } = data;
  isSearch.value = true;
  searchResults = [];
  searchResults = comments.value.filter(comment => comment.content.includes(data.search));
  data.searchResults = searchResults;
}

comments.value.forEach(comment => {
  comment.isExpanded = false;
});

function toggleContent(comment) {
  comment.isExpanded = !comment.isExpanded;
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

.container {
  padding-bottom: 20vw;
  width: 100%;
}

.top {
  display: flex;
  align-items: center;
  padding: 4vw 8vw 3vw 5vw;
  padding-right: 10vw;
  border-bottom: 0.2vw solid #f3f3f3;
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
  border: 0.5vw solid #f3f3f3;
}

.top .search .search-icon {
  margin-right: 2vw;
  width: 4vw;
  height: 4vw;
}

.top .search input {
  border: none;
  outline: none;
  width: 0;
  flex: 1;
  font-size: 3.817vw;
}

.top .search input::placeholder {
  color: #b9bcbe;
}

.comment {
  padding: 3vw;
  display: flex;
  border-bottom: 0.2vw solid #f3f3f3;
}

.avatar {
  margin-right: 3vw;
  width: 12vw;
  height: 12vw;
  border-radius: 50%;
  overflow: hidden; /* 确保图片溢出部分被隐藏 */
}

.avatar-img {
  width: 100%;
  height: 100%; /* 确保图片填满容器 */
  border-radius: 50%; /* 将图片变为圆形 */
  object-fit: cover; /* 确保图片按比例填充圆形容器 */
}


.right {
  position: relative;
  flex: 1;
}

.right .user {
  height: 12vw;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.right .nickName {
  margin: 0;
  font-size: 5vw;
  color: #00b140;
}

.right .pub_time {
  margin: 0;
  font-size: 3.5vw;
  color: #9499a0;
}

.right .content {
  margin: 3vw 0;
  max-width: 76vw;
  white-space: pre-wrap;
  font-size: 4.26vw;
}

.icons {
  display: flex;
  align-items: center;
}

.icon {
  margin-right: 2vw;
  width: 5vw;
  height: 5vw;
  vertical-align: middle;
}

.love-count {
  margin-right: 2vw;
  font-size: 4.5vw;
  color: #9499a0;
}

.submit {
  position: fixed;
  width: 100%;
  bottom: 0;
  background-color: #fff;
}

.wrapper {
  padding: 3vw;
  display: flex;
  align-items: end;
  width: 100%;
  height: 16vw;
  min-height: 16vw;
  transition: all 0.5s;
}

.avatar-bottom {
  align-self: center;
  width: 12vw;
  height: 12vw;
  border-radius: 50%;
  overflow: hidden;
  background: url(../../images/xiyang098/logo.png) no-repeat center / cover;
  margin-right: 3vw;
}

.wrapper textarea {
  padding: 2.67vw;
  width: 100%;
  flex: 1;
  outline: none;
  border-color: transparent;
  resize: none;
  background: #f5f5f5;
  border-radius: 4px;
  font-size: 4.2vw;
  height: 100%;
  transition: all 0.5s;
  overflow: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;

  &::-webkit-scrollbar {
    display: none;
  }
}

.wrapper textarea:focus {
  border-color: #e4e4e4;
  background: #fff;
  height: 100%;
}

.wrapper .submit-btn {
  background: #00aeec;
  color: #fff;
  border: none;
  border-radius: 1vw;
  margin-left: 2.67vw;
  width: 15vw;
  height: 100%;
}

.total {
  position: absolute;
  top: -5vw;
  left: 3vw;
  font-size: 3.5vw;
  color: #999;
  margin-top: 1.33vw;
  opacity: 0;
  transition: all .5s;
}

.total[v-show] {
  opacity: 1;
}

.content {
  display: -webkit-box;
  -webkit-line-clamp: 6;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  min-height: 1em;
  transition: all 5s;
}

.expanded {
  -webkit-line-clamp: unset;
}

.updown {
  position: absolute;
  right: 5vw;
  bottom: 0;
  width: 5vw;
  height: 5vw;
}
</style>
