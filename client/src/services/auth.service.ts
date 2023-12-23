"use server";

import { cookies } from "next/headers";
import { config } from "@/utils/config";
import axiosInstance from "@/utils/axiosInst";
import { SignUpResponse } from "@/interfaces/auth";
import { AxiosResponseHeaders, RawAxiosResponseHeaders } from "axios";

export const signIn = async (email: string, password: string): Promise<any> => {
  const authData = {
    username: email,
    password: password,
  };

  const response = await axiosInstance.post(
    `${config.baseUrl}/auth/login`,
    authData,
    {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    },
  );

  const token = await parseJwtToken(response.headers);
  await setupCookies(token);
};

export const signUp = async (
  email: string,
  username: string,
  password: string,
): Promise<SignUpResponse> => {
  const authData = {
    email: email,
    username: username,
    password: password,
  };

  const response = await axiosInstance.post<SignUpResponse>(
    `${config.baseUrl}/auth/register`,
    authData,
    {
      headers: { "Content-Type": "application/json" },
    },
  );

  if (response.status >= 400) {
    throw new Error("Invalid response status code: " + response.status);
  };

  await signIn(email, password);

  return response.data
}

export async function logout(): Promise<void> {
  await removeAuthCookie();
}

const parseJwtToken = async (
  headers: RawAxiosResponseHeaders | AxiosResponseHeaders,
): Promise<string> => {
  if (!headers["set-cookie"]) {
    throw new Error("Cookie not found in server response");
  }
  const cookieString = headers["set-cookie"][0];

  const cookiesArray = cookieString.split("; ");
  const targetCookie = cookiesArray.find((cookie) =>
    cookie.startsWith(`${config.auth.cookieName}=`),
  );

  if (!targetCookie) {
    throw new Error("Invalid server cookie");
  }
  const token = targetCookie.split("=")[1];

  return token;
};

const setupCookies = async (token: string): Promise<void> => {
  const cookieStore = cookies();

  await removeAuthCookie();

  cookieStore.set(config.auth.cookieName, token);
};

const removeAuthCookie = async (): Promise<void> => {
  const cookieStore = cookies();

  if (cookieStore.has(config.auth.cookieName)) {
    cookieStore.delete(config.auth.cookieName);
  }
};
