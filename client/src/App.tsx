import useRoutes from "./routes/routes";
import "./global.scss";

const App = () => {
  const routes = useRoutes();

  return (
    <>
      {routes}
    </>
  );
};

export default App;
