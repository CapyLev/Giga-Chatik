import { Route, Routes } from "react-router-dom";
import PrivateRoute from "../components/PrivateRoute";
import { AuthPage, HomePage } from "../pages/";
import useAuth from "../hooks/useAuth";

export const useRoutes = () => {
  const { isAuthenticated } = useAuth();

  return (
    <Routes>
      <Route
        path="/"
        element={isAuthenticated ? <PrivateRoute /> : <AuthPage />}
      />
      <Route path="/home" element={<PrivateRoute />}>
        <Route index element={<HomePage />} />
      </Route>
    </Routes>
  );
};

export default useRoutes;
