<script setup>
  import { RouterView } from 'vue-router';
  import globalState from '@/globalState';

  // 从LocalStorage同步email到全局状态
  const savedEmail = localStorage.getItem('userEmail');
  if (savedEmail) {
    globalState.email = savedEmail;
  }
</script>

<template>
  <RouterView />
</template>

<style>
  html {
    font-size: 16px;
  }

  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, Microsoft Yahei, sans-serif;
  }

  body * {
    box-sizing: border-box;
    flex-shrink: 0;
  }

  #app {
    width: 100vw;
    height: 100vh;
  }

  .flex-row {
    display: flex;
    flex-direction: row;
  }

  .flex-col {
    display: flex;
    flex-direction: column;
  }

  .justify-start {
    justify-content: flex-start;
  }

  .justify-end {
    justify-content: flex-end;
  }

  .justify-center {
    justify-content: center;
  }

  .justify-between {
    justify-content: space-between;
  }

  .justify-around {
    justify-content: space-around;
  }

  .justify-evenly {
    justify-content: space-evenly;
  }

  .items-start {
    align-items: flex-start;
  }

  .items-end {
    align-items: flex-end;
  }

  .items-center {
    align-items: center;
  }

  .items-baseline {
    align-items: baseline;
  }

  .items-stretch {
    align-items: stretch;
  }

  .self-start {
    align-self: flex-start;
  }

  .self-end {
    align-self: flex-end;
  }

  .self-center {
    align-self: center;
  }

  .self-baseline {
    align-self: baseline;
  }

  .self-stretch {
    align-self: stretch;
  }

  .flex-1 {
    flex: 1 1 0%;
  }

  .flex-auto {
    flex: 1 1 auto;
  }

  .grow {
    flex-grow: 1;
  }

  .grow-0 {
    flex-grow: 0;
  }

  .shrink {
    flex-shrink: 1;
  }

  .shrink-0 {
    flex-shrink: 0;
  }

  .relative {
    position: relative;
  }

  .ml-2 {
    margin-left: .509vw;
  }

  .mt-2 {
    margin-top: .509vw;
  }

  .ml-4 {
    margin-left: 1.018vw;
  }

  .mt-4 {
    margin-top: 1.018vw;
  }

  .ml-6 {
    margin-left: 1.527vw;
  }

  .mt-6 {
    margin-top: 1.527vw;
  }

  .ml-8 {
    margin-left: 2.036vw;
  }

  .mt-8 {
    margin-top: 2.036vw;
  }

  .ml-10 {
    margin-left: 2.545vw;
  }

  .mt-10 {
    margin-top: 2.545vw;
  }

  .ml-12 {
    margin-left: 3.053vw;
  }

  .mt-12 {
    margin-top: 3.053vw;
  }

  .ml-14 {
    margin-left: 3.562vw;
  }

  .mt-14 {
    margin-top: 3.562vw;
  }

  .ml-16 {
    margin-left: 4.071vw;
  }

  .mt-16 {
    margin-top: 4.071vw;
  }

  .ml-18 {
    margin-left: 4.58vw
  }

  .mt-18 {
    margin-top: 4.58vw
  }

  .ml-20 {
    margin-left: 5.089vw
  }

  .mt-20 {
    margin-top: 5.089vw
  }

  .ml-22 {
    margin-left: 5.598vw
  }

  .mt-22 {
    margin-top: 5.598vw
  }

  .ml-24 {
    margin-left: 6.107vw
  }

  .mt-24 {
    margin-top: 6.107vw
  }

.ml-26 {
    margin-left: 6.616vw
}

.mt-26 {
    margin-top: 6.616vw
}

.ml-28 {
    margin-left: 7.125vw
}

.mt-28 {
    margin-top: 7.125vw
}

.ml-30 {
    margin-left: 7.634vw
}

.mt-30 {
    margin-top: 7.634vw
}

.ml-32 {
    margin-left: 8.142vw
}

.mt-32 {
    margin-top: 8.142vw
}

.ml-34 {
    margin-left: 8.651vw
}

.mt-34 {
    margin-top: 8.651vw
}

.ml-36 {
    margin-left: 9.16vw
}

.mt-36 {
    margin-top: 9.16vw
}

.ml-38 {
    margin-left: 9.669vw
}

.mt-38 {
    margin-top: 9.669vw
}

.ml-40 {
    margin-left: 10.178vw
}

.mt-40 {
    margin-top: 10.178vw
}

.ml-42 {
    margin-left: 10.687vw
}

.mt-42 {
    margin-top: 10.687vw
}

.ml-44 {
    margin-left: 11.196vw
}

.mt-44 {
    margin-top: 11.196vw
}

.ml-46 {
    margin-left: 11.705vw
}

.mt-46 {
    margin-top: 11.705vw
}

.ml-48 {
    margin-left: 12.214vw
}

.mt-48 {
    margin-top: 12.214vw
}

.ml-50 {
    margin-left: 12.723vw
}

.mt-50 {
    margin-top: 12.723vw
}

.ml-52 {
    margin-left: 13.232vw
}

.mt-52 {
    margin-top: 13.232vw
}

.ml-54 {
    margin-left: 13.74vw
}

.mt-54 {
    margin-top: 13.74vw
}

.ml-56 {
    margin-left: 14.249vw
}

.mt-56 {
    margin-top: 14.249vw
}

.ml-58 {
    margin-left: 14.758vw
}

.mt-58 {
    margin-top: 14.758vw
}

.ml-60 {
    margin-left: 15.267vw
}

.mt-60 {
    margin-top: 15.267vw
}

.ml-62 {
    margin-left: 15.776vw
}

.mt-62 {
    margin-top: 15.776vw
}

.ml-64 {
    margin-left: 16.285vw
}

.mt-64 {
    margin-top: 16.285vw
}

.ml-66 {
    margin-left: 16.794vw
}

.mt-66 {
    margin-top: 16.794vw
}

.ml-68 {
    margin-left: 17.303vw
}

.mt-68 {
    margin-top: 17.303vw
}

.ml-70 {
    margin-left: 17.812vw
}

.mt-70 {
    margin-top: 17.812vw
}

.ml-72 {
    margin-left: 18.321vw
}

.mt-72 {
    margin-top: 18.321vw
}

.ml-74 {
    margin-left: 18.83vw
}

.mt-74 {
    margin-top: 18.83vw
}

.ml-76 {
    margin-left: 19.338vw
}

.mt-76 {
    margin-top: 19.338vw
}

.ml-78 {
    margin-left: 19.847vw
}

.mt-78 {
    margin-top: 19.847vw
}

.ml-80 {
    margin-left: 20.356vw
}

.mt-80 {
    margin-top: 20.356vw
}

.ml-82 {
    margin-left: 20.865vw
}

.mt-82 {
    margin-top: 20.865vw
}

.ml-84 {
    margin-left: 21.374vw
}

.mt-84 {
    margin-top: 21.374vw
}

.ml-86 {
    margin-left: 21.883vw
}

.mt-86 {
    margin-top: 21.883vw
}

.ml-88 {
    margin-left: 22.392vw
}

.mt-88 {
    margin-top: 22.392vw
}

.ml-90 {
    margin-left: 22.901vw
}

.mt-90 {
    margin-top: 22.901vw
}

.ml-92 {
    margin-left: 23.41vw
}

.mt-92 {
    margin-top: 23.41vw
}

.ml-94 {
    margin-left: 23.919vw
}

.mt-94 {
    margin-top: 23.919vw
}

.ml-96 {
    margin-left: 24.427vw
}

.mt-96 {
    margin-top: 24.427vw
}

  .ml-98 {
    margin-left: 24.936vw
  }

  .mt-98 {
    margin-top: 24.936vw
  }

  .ml-100 {
    margin-left: 25.445vw
  }
  .mt-100 {
    margin-top: 25.445vw
  }
  .el-form .el-form-item {
    margin-bottom: unset;
  }

  .el-form .el-form-item__label,
  .el-form .el-form-item__content {
    line-height: 32px;
  }

  .el-form.el-form--label-left .el-form-item__label {
    position: relative;
  }

  .el-form.el-form--label-left .el-form-item__label::before {
    position: absolute;
    left: -10px;
  }

  .el-form .el-checkbox,
  .el-form .el-radio {
    margin-right: unset;
  }

  .el-tabs__content {
    padding: unset !important;
  }

  .el-card__header {
    padding: unset !important;
    border-bottom: unset !important;
  }

  .el-dialog {
    max-width: 90vw;
    max-height: 90vh;
    overflow: auto;
  }

  .el-dialog .el-dialog__body {
    padding: unset;
  }

  .el-drawer {
    max-width: 90vw;
  }
</style>