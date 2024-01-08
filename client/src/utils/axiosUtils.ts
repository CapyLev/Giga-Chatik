import axios from "axios";

const axiosInst = axios.create({
  baseURL: "http://localhost:6969",
  timeout: 5000,
});

export default axiosInst;
