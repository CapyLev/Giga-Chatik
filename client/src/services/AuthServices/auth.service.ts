import { signUpUserData } from "../../interfaces/auth.interface";
import axiosInst from "../../utils/axiosUtils";

interface authData {
  [key: string]: string;
}

interface signInData {
  access_token: string;
  token_type: string;
}

export const signIn = async (
  email: string,
  password: string,
): Promise<void> => {
  const authData: authData = {
    username: email,
    password: password,
  };

  const formData = Object.keys(authData)
    .map(
      (key) =>
        encodeURIComponent(key) + "=" + encodeURIComponent(authData[key]),
    )
    .join("&");

  const { data } = await axiosInst.post<signInData>(
    "/api/auth/login",
    formData,
    {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    },
  );

  const { access_token } = data;
  const token = `Bearer ${access_token}`;

  localStorage.setItem("token", token);
};

export const signUp = async (
  email: string,
  username: string,
  password: string,
): Promise<signUpUserData> => {
  const authData: authData = {
    email: email,
    username: username,
    password: password,
  };

  try {
    const { data } = await axiosInst.post("/api/auth/register", authData, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return data;
  } catch (err) {
    console.log("Cannot register user: " + err);
    throw new Error("Cannot register user: " + err);
  }
};

export async function logout(): Promise<void> {
  await axiosInst.post("/api/auth/logout");

  localStorage.removeItem("token");
  localStorage.removeItem("token_type");
}
