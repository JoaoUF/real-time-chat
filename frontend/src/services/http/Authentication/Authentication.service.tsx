import { AxiosResponse } from "axios";
import AxiosConfig from "../AxiosConfig";
import {
  Login,
  LoginSuccesful,
  RefreshToken,
  Register,
} from "./Authentication.interface";

export class AuthenticationService {
  register_gmail(data: Register) {
    return AxiosConfig.post("dj-rest-auth/", data).then(
      (response) => response.status
    );
  }

  login_google(access_token: any): Promise<LoginSuccesful> {
    return AxiosConfig.post("dj-rest-auth/google/", {
      access_token: access_token,
    }).then((response: AxiosResponse<LoginSuccesful>) => response.data);
  }

  login(data: Login): Promise<LoginSuccesful> {
    return AxiosConfig.post("dj-rest-auth/login/", data).then(
      (response: AxiosResponse<LoginSuccesful>) => response.data
    );
  }

  logout() {
    return AxiosConfig.post("dj-rest-auth/logout/").then(
      (response) => response.status
    );
  }

  refresh_token(): Promise<RefreshToken> {
    return AxiosConfig.post("dj-rest-auth/token/refresh/").then(
      (response: AxiosResponse<RefreshToken>) => response.data
    );
  }
}
