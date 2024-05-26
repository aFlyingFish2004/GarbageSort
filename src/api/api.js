// src/api/api.js
import axiosInstance from './index'

const host = 'https://10.122.210.57:8000';

export function login(email, password) {
    return axiosInstance.post(`${host}/main/login/`, {
        email: email,
        password: password
    });
}

export function register(name, email, password) {
    return axiosInstance.post(`${host}/main/register/`, {
        name: name,
        email: email,
        password: password
    })
}

export function account(name, email) {
    return axiosInstance.post(`${host}/main/account/`, {
        name: name,
        email: email,
    })      
}

export function upload(formData) {
    return axiosInstance.post(`${host}/main/upload/`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        },
    })
}

export function uploadAvatar(formData) {
    return axiosInstance.post(`${host}/main/upload_avatar/`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        },
    })
}

export function fetchImage(imageName) {
    return axiosInstance.get(`${host}/main/get_image/`, {
        params: {
            image_name: imageName
        },
        responseType: 'blob' // Important to handle binary data
    });
}

export function fetchMessage(email) {
    return axiosInstance.get(`${host}/main/get_message/`, {
        params: { email: email }
    })
}