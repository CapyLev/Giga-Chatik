import { Link } from "react-router-dom";
import useAuth from "../hooks/useAuth";

const Navbar = () => {
  const { isAuthenticated } = useAuth();
  return (
    <>
      <h1>Welcome</h1>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/admin">Admin</Link>
        {isAuthenticated ? (
          <Link to="/logout">Logout</Link>
        ) : (
          <Link to="/login">Login</Link>
        )}
      </nav>
    </>
  );
};

export default Navbar;
