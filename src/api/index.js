// src/api/index.js
import Axios from 'axios'

const axiosInstance = Axios.create({
    withCredentials: true
})

// 通过拦截器处理csrf问题，这里的正则和匹配下标可能需要根据实际情况小改动
axiosInstance.interceptors.request.use((config) => {
    config.headers['X-Requested-With'] = 'XMLHttpRequest'
    const regex = /.*csrftoken=([^;.]*).*$/
    config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
    return config
})

axiosInstance.interceptors.response.use(
    response => response,
    error => Promise.reject(error)
)

// 创建一个插件来挂载 axiosInstance
export const axiosPlugin = {
    install(app) {
        app.config.globalProperties.$axios = axiosInstance
    }
}

export default axiosInstance
