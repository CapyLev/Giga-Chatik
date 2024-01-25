import { createContext, useEffect, useState } from "react";

type AuthContextType = {
  isAuthenticated: boolean;
  setAuth: (auth: boolean) => void;
};

const AuthContext = createContext<AuthContextType>({
  isAuthenticated: false,
  setAuth: () => {},
});

export const AuthProvider = ({ children }: { children: JSX.Element }) => {
  const [isAuthenticated, setAuth] = useState<boolean>(() => {
    const storedToken = localStorage.getItem("token");
    return !!storedToken;
  });

  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    setAuth(!!storedToken);
  }, []);

  return (
    <AuthContext.Provider value={{ isAuthenticated, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
