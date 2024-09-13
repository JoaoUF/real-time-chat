import { useRoutes } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import SignInSide from "./pages/SignInSide";
import PrivateRoute from "./utils/PrivateRoute";
import ChatRoom from "./pages/ChatRoom";

export default function App() {
  const routes = useRoutes([
    {
      path: "/",
      element: <AuthProvider />,
      children: [
        {
          path: "/",
          element: <SignInSide />,
        },
        {
          path: "/roomchat",
          element: <ChatRoom />,
        },
        {
          path: "/",
          element: <PrivateRoute />,
          children: [
            {
              path: "/private",
              element: <h1>Private</h1>,
            },
          ],
        },
      ],
    },
  ]);
  return routes;
}
