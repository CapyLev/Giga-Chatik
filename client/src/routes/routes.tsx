import { Route, Routes } from "react-router-dom";
import PrivateRoute from "../components/PrivateRoute";
import AuthPage from "../pages/AuthPage/AuthPage";
import Admin from "../pages/Admin";
import Logout from "../pages/Logout";

export const useRoutes = () => {
  return (
    <Routes>
      <Route index element={<AuthPage />} />

      <Route element={<PrivateRoute />}>
        <Route path="/admin" element={<Admin />} />
        <Route path="/logout" element={<Logout />} />
      </Route>
    </Routes>
  );
};

export default useRoutes;
