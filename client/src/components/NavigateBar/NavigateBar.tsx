import Link from "next/link";
import Image from "next/image";
import { FC } from "react";
import styles from "./NavigateBar.module.scss";
import { Routers } from "@/utils/common";

interface NavigateBarProps {}

const NavigateBar: FC<NavigateBarProps> = ({}) => {
  // TODO: its just a test example
  const serversIds = [1, 2, 3, 4, 5, 6];

  return (
    <div className={styles.navigationContainer}>
      <div className={styles.topSection}>
        <Link href={Routers.HOME}>
          <div>
            <Image
              className={styles.Icon}
              src="/home.svg"
              alt="Home"
              width={55}
              height={55}
            />
          </div>
        </Link>
      </div>

      <div className={styles.line}></div>

      <div className={styles.centerSection}>
        {serversIds.map((id) => (
          <div key={id} className={styles.serverIcon}></div>
        ))}
      </div>

      <div className={styles.line}></div>

      <div className={styles.bottomSection}>
        <Link href={Routers.PROFILE}>
          <div>
            <Image
              className={styles.Icon}
              src="/profile.svg"
              alt="Home"
              width={55}
              height={55}
            />
          </div>
        </Link>
      </div>
    </div>
  );
};

export default NavigateBar;
