import useAuth from "../hooks/useAuth";
import { useLocation, useNavigate } from "react-router-dom";

const Login = () => {
  const { setAuth } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from?.pathname || "/";

  return (
    <>
      <div>Login</div>
      <button
        type={"button"}
        onClick={() => {
          setAuth(true);
          navigate(from, { replace: true });
        }}
      >
        Login
      </button>
    </>
  );
};

export default Login;
