import { useState } from "react";
import useAuth from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";
import { SignUpModal, SignInModal } from "../../components";
import "./AuthPage.scss";

const AuthPage = () => {
  const [isSignInModalOpened, setSignInModalOpened] = useState<boolean>(false);
  const [isSignUpModalOpened, setSignUpModalOpened] = useState<boolean>(false);

  const { setAuth } = useAuth();
  const navigate = useNavigate();

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
        <button
          className="action"
          type={"button"}
          onClick={() => {
            setAuth(true);
            navigate("/home", { replace: true });
          }}
        >
          SIGN IN
        </button>

        <button className="action" onClick={() => setSignUpModalOpened(true)}>
          SIGN UP
        </button>
      </div>

      {isSignInModalOpened && <SignInModal closeModal={closeModal} />}
      {isSignUpModalOpened && <SignUpModal closeModal={closeModal} />}
    </>
  );
};

export default AuthPage;
