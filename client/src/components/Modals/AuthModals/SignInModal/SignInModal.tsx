import React, { FC, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  AuthValidationState,
  ModalProps,
} from "../../../../interfaces/common.interface";
import { isSignInCredentialsValid } from "../../../../services/AuthServices/credentialsChecker.service";
import useAuth from "../../../../hooks/useAuth";
import * as authService from "../../../../services/AuthServices/auth.service";
import "../../ModalsGlobal.scss";

const SignIn: FC<ModalProps> = ({ closeModal }) => {
  const { setAuth } = useAuth();
  const navigate = useNavigate();

  const [validationError, setValidationError] = useState<
    AuthValidationState["validationError"] | null
  >(null);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async () => {
    const validationErrors = await isSignInCredentialsValid(email, password);

    if (validationErrors && validationErrors.length > 0) {
      setValidationError(validationErrors);
    } else {
      setValidationError(null);
      await authService.signIn(email, password);
      setAuth(true);
      navigate("/home", { replace: true });
    }
  };

  const handleContainerClick = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
  };

  return (
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
            type="password"
            placeholder="Password"
            value={password}
            onChange={handlePasswordChange}
            className="input"
          />
          <button onClick={handleSubmit} className="submitButton">
            Submit
          </button>
        </div>
      </div>
    </div>
  );
};

export default SignIn;
