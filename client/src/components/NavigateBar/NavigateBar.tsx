import { FC } from "react";
import styles from "./NavigateBar.module.scss";

const NavigateBar: FC = () => {
    return (
        <div className={styles.navigationContainer}>
            <div className={styles.homeIcon}>
                <img src="/home.svg" alt="Home" width={55} height={55} />
            </div>
        </div>
    );
};

export default NavigateBar;
