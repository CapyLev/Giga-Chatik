import { FC } from "react";
import styles from "@/components/EntryPoint/EntryPoint.module.scss";

interface SignInProps {
  closeModal: () => void;
}

const SignIn: FC<SignInProps> = ({ closeModal }) => {
  return (
    <>
      <div className={styles.overlay} onClick={closeModal}>
        <div className={styles.modal}>
          <span className={styles.close} onClick={closeModal}>
            &times;
          </span>
          Sign In Modal Content
        </div>
      </div>
    </>
  );
};

export default SignIn;
