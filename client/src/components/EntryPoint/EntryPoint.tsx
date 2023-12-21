import Link from "next/link";
import styles from "./EntryPoint.module.scss";

export default function EntryPoint() {
  return (
    <div>
      <div className={styles.title}>
        <h1>Hello!</h1>
      </div>
      <div className={styles.action}>
        <Link className={styles.action} href="/signin">SIGN IN</Link>
        <Link className={styles.action} href="/signup">SIGN UP</Link>
      </div>
    </div>
  );
}
