import { useState } from "react";
import useAuth from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";
import { SignUpModal, SignInModal, Button } from "../../components";
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

  const handleSignUpClick = () => {
    setSignUpModalOpened(true);
  };

  const handleSignInClick = () => {
    setAuth(true);
    navigate("/home", { replace: true });
  };

  return (
    <>
      <div className="title">
        <h1>Hello!</h1>
      </div>

        <Button onClickHandler={handleSignInClick} buttonText="SIGN IN"/>
        <Button onClickHandler={handleSignUpClick} buttonText="SIGN UP"/>

      {isSignInModalOpened && <SignInModal closeModal={closeModal} />}
      {isSignUpModalOpened && <SignUpModal closeModal={closeModal} />}
    </>
  );
};

export default AuthPage;
