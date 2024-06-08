// src/api/api.js
import axiosInstance from './index'
const host = 'https://garbage.sa1ge.ink';

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

export function infer(email) {
    return axiosInstance.post(`${host}/main/infer/`, {
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

export function createModel(userId) {
    const formData = new FormData();
    formData.append('user_id', userId);
    return axiosInstance.post(`${host}/main/create_model/`, formData);
}


  export function uploads(formData) {
    return axiosInstance.post(`${host}/main/upload_images/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
  }
  export function getImageByPath(folderUrl, imageName) {
    return axiosInstance.get(`${host}/main/get_image_by_path/`, {
        params: { folder_url: folderUrl, image_name: imageName },
        responseType: 'blob'  // 以二进制流的形式获取图片数据
    });
}

export function updateModel(formData) {
    return axiosInstance.post(`${host}/main/update_model/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
  }

  export function getModels(userId) {
    return axiosInstance.get(`${host}/main/get_models/?user_id=${userId}`);
  }

  export function getRandomImageByFolder(folderUrl) {
    return axiosInstance.get(`${host}/main/get_random_image_by_folder/`, {
      params: { folder_url: folderUrl },
      responseType: 'blob' // Important to handle binary data
    });
  }

  export function getModelDetails(modelId) {
    return axiosInstance.get(`${host}/main/get_model_details/`, {
      params: { model_id: modelId }
    });
  }
  

  export function deleteModelById(data) {
      return axiosInstance.post(`${host}/main/delete_model/`, data, {
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
          }
      });
  }
  

  export function getImagesByFolder(folderUrl) {
    return axiosInstance.get(`${host}/main/get_images_by_folder/`, {
        params: {
            folder_url: folderUrl
        }
    });
    }
    export function fetchInferMessage(email) {
        return axiosInstance.get(`${host}/main/infer/`, {
            params: { email: email }
        })
    }

    export function uploadPhoto(formData) {
        return axiosInstance.post(`${host}/main/upload_photo/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            },
        })
    }