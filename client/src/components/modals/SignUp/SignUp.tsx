import React, { FC, useState } from "react";
import styles from "@/components/modals/Modals.module.scss";
import * as authService from "@/services/auth.service";
import { Routers } from "@/utils/common";
import router from "next/router";

interface SignUpProps {
  closeModal: () => void;
}

const SignUp: FC<SignUpProps> = ({ closeModal }) => {
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
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    setRepeatPassword(e.target.value);
  };

  const handleSubmit = async () => {
    const result = await authService.signUp(email, username, password);
    if (result) {
      router.push(Routers.HOME);
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
