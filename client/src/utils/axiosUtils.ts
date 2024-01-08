import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "localhost:6969",
  timeout: 5000,
});

export default axiosInstance;
