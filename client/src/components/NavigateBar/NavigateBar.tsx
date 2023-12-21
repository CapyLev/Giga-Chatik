import Link from "next/link";
import Image from "next/image";
import { FC } from "react";
import styles from "./NavigateBar.module.scss";
import { Routers } from "@/utils/common";

const NavigateBar: FC = () => {
  return (
    <div className={styles.navigationContainer}>
      <Link href={Routers.HOME}>
        <div>
          <Image
            className={styles.homeIcon}
            src="/home.svg"
            alt="Home"
            width={55}
            height={55}
          />
        </div>
      </Link>
    </div>
  );
};

export default NavigateBar;
