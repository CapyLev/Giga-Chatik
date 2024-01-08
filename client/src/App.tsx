import Navbar from "./components/Navbar";
import useRoutes from "./routes/routes";

const App = () => {
  const routes = useRoutes();

  return (
    <>
      <Navbar />
      {routes}
    </>
  );
};

export default App;
