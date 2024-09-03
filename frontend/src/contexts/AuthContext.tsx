import { createContext, useState } from "react";
import { Outlet, useNavigate } from "react-router-dom";
import { Login } from "../services/http/Authentication/Authentication.interface";
import { AuthenticationService } from "../services/http/Authentication/Authentication.service";

interface ContextProps {
  user: number | null;
  loginGoogle: (access_token: any) => Promise<void>;
  loginUser: (data: Login) => Promise<void>;
  logoutUser: () => void;
}

const AuthContext = createContext<ContextProps | null>(null);

export default AuthContext;

export const AuthProvider = () => {
  let [user, setUser] = useState<number | null>(null);
  let navigate = useNavigate();

  let loginGoogle = async (access_token: any) => {
    try {
      let authenticationService = new AuthenticationService();
      let authenticationResponse = await authenticationService.login_google(
        access_token
      );
      setUser(authenticationResponse.user.pk);
      navigate("/chatroom");
    } catch (error) {
      console.log(error);
    }
  };

  let loginUser = async (data: Login) => {
    try {
      let authenticationService = new AuthenticationService();
      let authenticationResponse = await authenticationService.login(data);
      setUser(authenticationResponse.user.pk);
      navigate("/chatroom");
    } catch (error) {
      console.log(error);
    }
  };

  let logoutUser = async () => {
    setUser(null);
    navigate("/");
  };

  let contextProps: ContextProps = {
    user: user,
    loginGoogle: loginGoogle,
    loginUser: loginUser,
    logoutUser: logoutUser,
  };

  return (
    <AuthContext.Provider value={contextProps}>
      {<Outlet />}
    </AuthContext.Provider>
  );
};
