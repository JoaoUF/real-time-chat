import { useRoutes } from "react-router-dom";
import SignInSide from "./pages/SignInSide";

export default function App() {
  const routes = useRoutes([
    {
      path: "/",
      element: <SignInSide />,
    },
  ]);
  return routes;
}
