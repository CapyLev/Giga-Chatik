// WelcomeNavigateBar.tsx

import { FC } from "react";
import "./WelcomeNavigateBar.scss";
import useAuth from "../../hooks/useAuth";
import { Link } from "react-router-dom";

const WelcomeNavigateBar: FC = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="WelcomeNavigateBar">
      <nav>
        <Link to="/About">About</Link>
        <Link to="/updates">Updates</Link>
        <Link to="/sourceCode">Source Code</Link>
        {isAuthenticated ? (
          <Link to="/logout">Logout</Link>
        ) : (
          <>
            <Link to="/auth/signIn">Sign In</Link>
            <Link to="/auth/signUp">Sign Up</Link>
          </>
        )}
      </nav>
    </div>
  );
};

export default WelcomeNavigateBar;
