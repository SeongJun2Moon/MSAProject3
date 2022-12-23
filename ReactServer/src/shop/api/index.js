import axios from "axios";
const server = `http://localhost:8000`;
// export const irisApi = req => axios.get(`${server}/shop/iris/iris`, req)
export const irisApi = (req) => axios.post(`${server}/shop/iris/iris`, req);
export const ApiPost = (req) =>
  axios.post(`${server}/shop/fashion/fashion`, req);
export const ApiGet = (req) =>
  axios.get(`${server}/shop/fashion/fashion?id=${req}`);
export const getnumber = (req) =>
  axios.get(`${server}/shop/number/number?req=${req}`);
export const postnumber = (req) =>
  axios.post(`${server}/shop/number/number`, req);
