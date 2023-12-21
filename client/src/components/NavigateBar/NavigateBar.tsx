import Link from 'next/link';
import { FC } from "react";
import styles from "./NavigateBar.module.scss";

const NavigateBar: FC = () => {
  return (
    <div className={styles.navigationContainer}>
      <Link href="/home">
        <a className={styles.homeIcon}>
          <img src="/home.svg" alt="Home" width={55} height={55} />
        </a>
      </Link>
    </div>
  );
};

export default NavigateBar;
