import { server, irispath, fashionpath, numberpath, traderpath } from "context";
import axios from "axios";
// export const irisApi = req => axios.get(`${server}/shop/iris/iris`, req)
export const irisApi = (req) => axios.post(`${server}${irispath}`, req);
export const ApiPost = (req) => axios.post(`${server}${fashionpath}`, req);
export const ApiGet = (req) => axios.get(`${server}${fashionpath}?id=${req}`);
export const getnumber = (req) =>
  axios.get(`${server}${numberpath}?req=${req}`);
export const postnumber = (req) => axios.post(`${server}${numberpath}`, req);

export const webcrawlerService = {
  samsungtraders,
};

const handleResponse = (response) => {
  return response.text().then((text) => {
    const data = text && JSON.parse(text);
    if (!response.ok) {
      if (response.status === 401) {
        window.location.reload();
      }
      const error = (data && data.message) || response.statusText;
      return Promise.reject(error);
    }
    return data;
  });
};

async function samsungtraders() {
  const res = await fetch(`${server}${traderpath}`)
    .then(handleResponse)
    .then((data) => JSON.stringify(data)) //JSON.stringify() : 딕셔너리를 JSON으로 변환
    .catch((error) => {
      alert("error :::: " + error);
    });
  return Promise.resolve(res);
}
