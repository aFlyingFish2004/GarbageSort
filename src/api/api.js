// appfront/src/api/api.js
import axiosInstance from './index'

export const getBooks = () => axiosInstance.get('http://localhost:8000/api/books/')

export const postBook = (bookName, bookAuthor) => axiosInstance.post('http://localhost:8000/api/books/', { 'name': bookName, 'author': bookAuthor })

export function login(email, password) {
    return axiosInstance.post('http://localhost:8000/main/login/', {
        email: email,
        password: password
    });
}
