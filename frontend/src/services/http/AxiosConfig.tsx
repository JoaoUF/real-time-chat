import axios from "axios";
// import AuthContext from "../contexts/AuthContext";
// import { AuthenticationService } from "./Authentication/Authentication.service";

const AxiosConfig = axios.create({
  baseURL: process.env.REACT_APP_API_PATH,
  timeout: 10000,
  withCredentials: true,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

// AxiosConfig.interceptors.response.use(null, async (error: any) => {
//   if (error) {
//     console.log("error interceptor");
//     console.log(error);
//   }
//   let { logoutUser }: any = useContext(AuthContext);
//   error.config.retries = error.config.retries || {
//     count: 0,
//   };

//   if (isUnAuthorizedError(error) && shouldRetry(error.config)) {
//     let authenticationService = new AuthenticationService();
//     error.config.retries.count += 1;

//     const originalRequestConfig = error.config;
//     delete originalRequestConfig.headers["Authorization"];
//     return authenticationService
//       .refresh_token()
//       .then(() => axios.request(originalRequestConfig));
//   }
//   // logoutUser();
//   return Promise.reject(error);
// });

function isUnAuthorizedError(error: any) {
  return error.config && error.response && error.response.status === 401;
}

function shouldRetry(config: any) {
  return config.retries.count < 2;
}

export default AxiosConfig;
