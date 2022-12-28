import {server, irispath, fashionpath, numberpath } from 'context'
import axios from "axios";
// export const irisApi = req => axios.get(`${server}/shop/iris/iris`, req)
export const irisApi = (req) => axios.post(`${server}${irispath}`, req);
export const ApiPost = (req) =>
  axios.post(`${server}${fashionpath}`, req);
export const ApiGet = (req) =>
  axios.get(`${server}${fashionpath}?id=${req}`);
export const getnumber = (req) =>
  axios.get(`${server}${numberpath}?req=${req}`);
export const postnumber = (req) =>
  axios.post(`${server}${numberpath}`, req);
  