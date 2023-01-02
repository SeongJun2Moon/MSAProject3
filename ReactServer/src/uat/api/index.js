import axios from "axios";
const host = `http://localhost:8000`;
const userLoginApi = (req) => axios.post(`${host}/security/users/login`, req);

export { userLoginApi };
