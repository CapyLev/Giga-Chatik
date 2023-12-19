import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./global.scss";
import NavigateBar from "@/components/NavigateBar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  applicationName: "4atik",
  title: "super 4atik",
  referrer: "origin-when-cross-origin",
  description: "super mega 4atik for giga chads",
  keywords: ["chat", "talk", "4atik", "super chatik"],
  creator: "Rasul Makhmudov",
};

interface RootLayoutProps {
  children: React.ReactNode;
}

const RootLayout: React.FC<RootLayoutProps> = ({ children }) => {
  return (
    <html lang="en">
      <body className={inter.className}>
        <NavigateBar />
        {children}
      </body>
    </html>
  );
};

export default RootLayout;
