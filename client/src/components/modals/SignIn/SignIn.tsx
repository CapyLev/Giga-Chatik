import React, {FC, useState} from "react";
import styles from "@/components/modals/Modals.module.scss";

interface SignInProps {
    closeModal: () => void;
}

const SignIn: FC<SignInProps> = ({closeModal}) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setEmail(e.target.value);
    };

    const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setPassword(e.target.value);
    };

    const handleSubmit = () => {
        console.log("Email:", email);
        console.log("Password:", password);
        // TODO: send request to server yoy
    };

    const handleContainerClick = (e: React.MouseEvent<HTMLDivElement>) => {
        e.stopPropagation();
    };

  return (
    <>
      <div className={styles.overlay} onClick={closeModal}>
        <div className={styles.modal} onClick={handleContainerClick}    >
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
    </>
  );
};

export default SignIn;