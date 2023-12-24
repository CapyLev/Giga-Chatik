import React, { FC, useState } from "react";
import styles from "@/components/modals/Modals.module.scss";
import * as authService from "@/services/auth.service";
import { isSignInCredentialsValid } from "@/utils/auth";
import {
  ModalProps,
  AuthValidationState,
} from "@/interfaces/common.interfaces";
import { useRouter } from "next/navigation";
import { Routers } from "@/utils/common";

const SignIn: FC<ModalProps> = ({ closeModal }) => {
  const router = useRouter();

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
      router.push(Routers.HOME);
    }
  };

  const handleContainerClick = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
  };

  return (
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
            type="password"
            placeholder="Password"
            value={password}
            onChange={handlePasswordChange}
            className={styles.input}
          />
          <button onClick={handleSubmit} className={styles.submitButton}>
            Submit
          </button>
        </div>
      </div>
    </div>
  );
};

export default SignIn;
