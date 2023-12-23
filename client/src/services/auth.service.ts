"use server";

import { config } from "@/utils/config";
import axiosInstance from "@/utils/axiosInst";
import { SignInResponse, SignUpResponse } from "@/interfaces/auth";

export async function signIn(email: string, password: string): Promise<string> {
  const authData = {
    username: email,
    password: password,
  };

  const { data } = await axiosInstance.post<SignInResponse>(
    `${config.baseUrl}/auth/login`,
    authData,
    {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    },
  );

  return data.access_token;
}

export async function signUp(
  email: string,
  username: string,
  password: string,
): Promise<{ token: string; user: SignUpResponse }> {
  const authData = {
    email: email,
    username: username,
    password: password,
    is_active: true,
    is_superuser: true,
    is_verified: true,
  };

  const res = await fetch(`${config.baseUrl}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(authData),
  });

  const result: SignUpResponse = await res.json();

  if (res.status === 200 || res.status === 201) {
    const token = await signIn(email, password);
    return { token: token, user: result };
  } else {
    throw new Error("Failed to sign up");
  }
}

export async function logout(): Promise<void> {
  await axiosInstance.post<SignInResponse>(`${config.baseUrl}/auth/logout`);
}
