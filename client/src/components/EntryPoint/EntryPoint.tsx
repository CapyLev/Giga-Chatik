import Link from "next/link";
import styles from "./EntryPoint.module.scss";
import { FC } from "react";

const EntryPoint: FC = () => {

    return (
        <div>
            <div className={styles.title}>
                <h1>Hello!</h1>
            </div>
            <div className={styles.actions}>
                {/*change to 2 different modals*/}
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

export default EntryPoint;