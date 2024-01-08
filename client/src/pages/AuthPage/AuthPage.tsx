import { useState } from "react";
import useAuth from "../../hooks/useAuth";
import { useLocation, useNavigate } from "react-router-dom";
import { SignUpModal, SignInModal } from "../../components";
import "./AuthPage.scss"

const AuthPage = () => {
  const [isSignInModalOpened, setSignInModalOpened] = useState<boolean>(false);
  const [isSignUpModalOpened, setSignUpModalOpened] = useState<boolean>(false);

  const { setAuth } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from?.pathname || "/";

  const closeModal = () => {
    setSignInModalOpened(false);
    setSignUpModalOpened(false);
  };

  return (
    <>
      <div className="title">
        <h1>Hello!</h1>
      </div>

      <div className="actions">
        <button className="action" onClick={() => setSignInModalOpened(true)}>
          SIGN IN
        </button>

        <button className="action" onClick={() => setSignUpModalOpened(true)}>
          SIGN UP
        </button>
      </div>

      {isSignInModalOpened && <SignInModal closeModal={closeModal} />}
      {isSignUpModalOpened && <SignUpModal closeModal={closeModal} />}

      {/* <button
        type={"button"}
        onClick={() => {
          setAuth(true);
          navigate(from, { replace: true });
        }}
      >
        Login
      </button> */}
    </>
  );
};

export default AuthPage;
