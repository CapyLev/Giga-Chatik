import React, { FC, useState } from "react";
import { useRouter } from "next/navigation";
import styles from "@/components/modals/Modals.module.scss";
import * as authService from "@/services/auth.service";
import { isSignUpCredentialsValid } from "@/utils/auth";
import { AuthValidationState, ModalProps } from "@/interfaces/common";

const SignUp: FC<ModalProps> = ({ closeModal }) => {
  const router = useRouter();

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
      localStorage.setItem('userId', user.id);
      router.push("/home");
    }
  };

  const handleContainerClick = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
  };

  return (
    <>
      <div className={styles.overlay} onClick={closeModal}>
        <div className={styles.modal} onClick={handleContainerClick}>
          <span className={styles.close} onClick={closeModal}>
            &times;
          </span>
          <div className={styles.modalContent}>
            {validationError && (
              <div className={styles.validationError}>{validationError[0]}</div>
            )}
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={handleEmailChange}
              className={styles.input}
            />
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={handleUsernameChange}
              className={styles.input}
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={handlePasswordChange}
              className={styles.input}
            />
            <input
              type="password"
              placeholder="Repeat password"
              value={repeatPassword}
              onChange={handleRepeatPasswordChange}
              className={styles.input}
            />
            <button onClick={handleSubmit} className={styles.submitButton}>
              Submit
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default SignUp;
