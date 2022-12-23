import axios from 'axios'
const server = `http://localhost:8000`
export const userLoginApi = req => axios.post(`${server}/blog/auth/login`, req)