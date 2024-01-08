import { signUpUserData } from "../../interfaces/auth.interface";
import axiosInst from "../../utils/axiosUtils";

interface authData {
  [key: string]: string;
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

  await axiosInst.post("/api/auth/login", formData, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
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
}
