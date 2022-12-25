import axios from "axios";
const host = `http://localhost:8000`;
const userLoginApi = (req) => axios.post(`${host}/blog/auth/login`, req);

const random = `/users/users`;
const server = "http://127.0.0.1:8000/";

const randomUserMaker = {
  randomUsers,
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

async function randomUsers() {
  const res = await fetch(`${server}${random}`)
    .then(handleResponse)
    .then((data) => JSON.stringify(data)) //JSON.stringify() : 딕셔너리를 JSON으로 변환
    .catch((error) => {
      alert("error :::: " + error);
    });
  return Promise.resolve(res);
}
export { randomUserMaker, userLoginApi };
