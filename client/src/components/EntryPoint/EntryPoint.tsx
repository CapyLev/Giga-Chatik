"use client";

import React, { FC, useState } from "react";
import styles from "./EntryPoint.module.scss";
import SignIn from "@/components/modals/SignIn/SignIn";
import SignUp from "@/components/modals/SignUp/SignUp";

const EntryPoint: FC = () => {
  const [isSignInModalOpened, setSignInModalOpened] = useState<boolean>(false);
  const [isSignUpModalOpened, setSignUpModalOpened] = useState<boolean>(false);

  const closeModal = () => {
    setSignInModalOpened(false);
    setSignUpModalOpened(false);
  };

  return (
    <div>
      <div className={styles.title}>
        <h1>Hello!</h1>
      </div>
      <div className={styles.actions}>
        <button
          className={styles.action}
          onClick={() => setSignInModalOpened(true)}
        >
          SIGN IN
        </button>

        <button
          className={styles.action}
          onClick={() => setSignUpModalOpened(true)}
        >
          SIGN UP
        </button>
      </div>

      {isSignInModalOpened && <SignIn closeModal={closeModal} />}
      {isSignUpModalOpened && <SignUp closeModal={closeModal} />}
    </div>
  );
};

export default EntryPoint;
