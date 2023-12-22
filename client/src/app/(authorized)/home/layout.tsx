import NavigateBar from "@/components/NavigateBar/NavigateBar";

const HomeLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <>
      <NavigateBar />
      {children}
    </>
  );
};

export default HomeLayout;
