import Link from "next/link";
import styles from "./EntryPoint.module.scss";

export default function EntryPoint() {
  
  return (
    <div>
      <div className={styles.title}>
        <h1>Hello!</h1>
      </div>
      <div className={styles.actions}>
        <Link href="/signin">
          <div className={styles.action}>SIGN IN</div>
        </Link>
        <Link href="/signup">
          <div className={styles.action}>SIGN UP</div>
        </Link>
      </div>
    </div>
  );
}
