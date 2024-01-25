import React, { FC, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  AuthValidationState,
  ModalProps,
} from "../../../../interfaces/common.interface";
import { isSignUpCredentialsValid } from "../../../../services/AuthServices/credentialsChecker.service";
import * as authService from "../../../../services/AuthServices/auth.service";
import "../../ModalsGlobal.scss";

const SignUp: FC<ModalProps> = ({ closeModal }) => {
  const navigate = useNavigate();

  const [validationError, setValidationError] =
    useState<AuthValidationState["validationError"]>(null);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [username, setUsername] = useState("");

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };

  const handleUsernameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(e.target.value);
  };

  const handleRepeatPasswordChange = (
    e: React.ChangeEvent<HTMLInputElement>,
  ) => {
    setRepeatPassword(e.target.value);
  };

  const handleSubmit = async () => {
    const validationErrors = await isSignUpCredentialsValid(
      email,
      username,
      password,
    );

    if (validationErrors && validationErrors.length > 0) {
      setValidationError(validationErrors);
    } else {
      const user = await authService.signUp(email, username, password);
      await authService.signIn(email, password);
      localStorage.setItem("userId", user.id);
      navigate("/home");
    }
  };

  const handleContainerClick = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
  };

  return (
    <>
      <div className="overlay" onClick={closeModal}>
        <div className="modal" onClick={handleContainerClick}>
          <span className="close" onClick={closeModal}>
            &times;
          </span>
          <div className="modalContent">
            {validationError && (
              <div className="validationError">{validationError[0]}</div>
            )}
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={handleEmailChange}
              className="input"
            />
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={handleUsernameChange}
              className="input"
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={handlePasswordChange}
              className="input"
            />
            <input
              type="password"
              placeholder="Repeat password"
              value={repeatPassword}
              onChange={handleRepeatPasswordChange}
              className="input"
            />
            <button onClick={handleSubmit} className="submitButton">
              Submit
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default SignUp;
