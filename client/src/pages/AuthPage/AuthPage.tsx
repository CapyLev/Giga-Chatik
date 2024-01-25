import { useState } from "react";
import { SignUpModal, SignInModal, Button } from "../../components";
import "./AuthPage.scss";

const AuthPage = () => {
  const [isSignInModalOpened, setSignInModalOpened] = useState<boolean>(false);
  const [isSignUpModalOpened, setSignUpModalOpened] = useState<boolean>(false);

  const closeModal = () => {
    setSignInModalOpened(false);
    setSignUpModalOpened(false);
  };

  const handleSignUpClick = () => {
    setSignUpModalOpened(true);
  };

  const handleSignInClick = () => {
    setSignInModalOpened(true);
  };

  return (
    <>
      <div className="title">
        <h1>GiGa Chatik</h1>
      </div>

      <div className="authActions">
        <Button onClickHandler={handleSignInClick} buttonText="SIGN IN" />
        <Button onClickHandler={handleSignUpClick} buttonText="SIGN UP" />
      </div>

      {isSignInModalOpened && <SignInModal closeModal={closeModal} />}
      {isSignUpModalOpened && <SignUpModal closeModal={closeModal} />}
    </>
  );
};

export default AuthPage;
