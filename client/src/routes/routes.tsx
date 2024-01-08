import { Route, Routes } from "react-router-dom";
import PrivateRoute from "../components/PrivateRoute";
import { AuthPage, HomePage } from "../pages/";

export const useRoutes = () => {
  return (
    <Routes>
      <Route index element={<AuthPage />} />
      <Route path="/" element={<AuthPage />} />

      <Route element={<PrivateRoute />}>
        <Route path="/home" element={<HomePage />} />
      </Route>
    </Routes>
  );
};

export default useRoutes;
