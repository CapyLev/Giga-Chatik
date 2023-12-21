import NavigateBar from "@/components/NavigateBar/NavigateBar"

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <NavigateBar/>
      <body>{children}</body>
    </html>
  );
}
