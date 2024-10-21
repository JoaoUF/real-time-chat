import { useRoutes } from "react-router-dom";
// import { AuthProvider } from "./contexts/AuthContext";
import ChatRoom from "./pages/ChatRoom";
import SignInSide from "./pages/SignInSide";
import TestWS from "./TestWS";
import PrivateRoute from "./utils/PrivateRoute";

export default function App() {
  const routes = useRoutes([
    {
      path: "/",
      element: <TestWS />,
      // element: <AuthProvider />,
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
