import {navercrawler, server} from 'context'

const webcrawlerService = {
  naverMovie,
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

async function naverMovie() {
  const res = await fetch(`${server}${navercrawler}`)
    .then(handleResponse)
    .then((data) => JSON.stringify(data)) //JSON.stringify() : 딕셔너리를 JSON으로 변환
    .catch((error) => {
      alert("error :::: " + error);
    });
  return Promise.resolve(res);
}
export default webcrawlerService;
