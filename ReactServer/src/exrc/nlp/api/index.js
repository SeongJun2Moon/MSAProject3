import { server, imdbpath, samsungpath, koreanpath } from "context";

const webcrawlerService = {
  samsungWords,
  navergrade,
  koreanClassify,
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

async function samsungWords() {
  const res = await fetch(`${server}${samsungpath}`)
    .then(handleResponse)
    .then((data) => JSON.stringify(data)) //JSON.stringify() : 딕셔너리를 JSON으로 변환
    .catch((error) => {
      alert("error :::: " + error);
    });
  return Promise.resolve(res);
}

async function navergrade(req) {
  const requestOption = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(req),
  };
  const res = await fetch(`${server}${imdbpath}`, requestOption)
    .then(handleResponse)
    .then((data) => JSON.stringify(data)) //JSON.stringify() : 딕셔너리를 JSON으로 변환
    .catch((error) => {
      alert("error :::: " + error);
    });
  return Promise.resolve(res);
}

async function koreanClassify(req) {
  const requestOption = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(req),
  };
  const res = await fetch(`${server}${koreanpath}`, requestOption)
    .then(handleResponse)
    .then((data) => JSON.stringify(data)) //JSON.stringify() : 딕셔너리를 JSON으로 변환
    .catch((error) => {
      alert("error :::: " + error);
    });
  return Promise.resolve(res);
}
export default webcrawlerService;
