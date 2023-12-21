import { FC } from "react";
import styles from "@/components/EntryPoint/EntryPoint.module.scss";

interface SignUpProps {
  closeModal: () => void;
}

const SignUp: FC<SignUpProps> = ({ closeModal }) => {
  return (
    <>
      <div className={styles.overlay} onClick={closeModal}>
        <div className={styles.modal}>
          <span className={styles.close} onClick={closeModal}>
            &times;
          </span>
          Sign Up Modal Content
        </div>
      </div>
    </>
  );
};

export default SignUp;
