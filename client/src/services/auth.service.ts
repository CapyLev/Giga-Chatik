"use server";

import { cookies } from "next/headers";

export async function signIn(
  email: string,
  password: string
): Promise<void | boolean> {
  cookies().set("4atik", `${email}-${password}`);
  console.log(email, password);
  return true;
}

export async function signUp(
  email: string,
  username: string,
  password: string
): Promise<void | boolean> {
  cookies().set(
    "4atik",
    `Email: ${email}. Username: ${username}. Password: ${password}`
  );
  console.log(email, password);
  return true;
}
