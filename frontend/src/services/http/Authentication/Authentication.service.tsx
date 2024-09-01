import AxiosConfig from "../AxiosConfig";

export class AuthenticationService {
  register_google_access_toke(access_token: any) {
    return AxiosConfig.post("dj-rest-auth/google/", {
      access_token: access_token,
    }).then((response) => response.status);
  }
}
