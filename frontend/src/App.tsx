import { useRoutes } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import SignInSide from "./pages/SignInSide";
import PrivateRoute from "./utils/PrivateRoute";

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
          element: <h2>roomchat</h2>,
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
