import NavigateBar from "@/components/NavigateBar/NavigateBar";

const HomeLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <html lang="en">
      <body>
        <NavigateBar />
        {children}
      </body>
    </html>
  );
};

export default HomeLayout;
