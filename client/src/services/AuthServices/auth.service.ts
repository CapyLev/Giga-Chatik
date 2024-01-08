export const signIn = async (
  email: string,
  password: string,
): Promise<void> => {
  const authData = {
    username: email,
    password: password,
  };
};

export const signUp = async (
  email: string,
  username: string,
  password: string,
): Promise<void> => {};

export async function logout(): Promise<void> {}

const setupCookies = async (token: string): Promise<void> => {};

const removeAuthCookie = async (): Promise<void> => {};
