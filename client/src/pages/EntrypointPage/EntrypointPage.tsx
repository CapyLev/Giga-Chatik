import { FC } from "react";
import { Link } from 'react-router-dom';
import styles from "./EntrypointPage.module.scss";

const EntrypointPage: FC = () => {
    return (
        <div>
            <div className={styles.title}>
                <p>Hello</p>
            </div>
            <div className={styles.actions}>
                <Link to="/signin">SIGN IN</Link>
                <Link to="/signup">SIGN UP</Link>
            </div>
        </div>
    );
};

export default EntrypointPage;
