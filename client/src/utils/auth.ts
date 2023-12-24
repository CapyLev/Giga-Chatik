import { isOptionalString } from "@/interfaces/common.interfaces";

const isEmailValid = (email: string): boolean => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
};

const isUsernameValid = (username: string): boolean => {
  return username.length > 3;
};

const isPasswordValid = (password: string): boolean => {
  return password.length > 8 && /[!@#$%^&*(),.?":{}|<>]/.test(password);
};

const validateCredentials = (
  email: isOptionalString,
  username: isOptionalString,
  password: isOptionalString,
  validateUsername: boolean = true,
  validatePassword: boolean = true,
): string[] => {
  const errors = [];

  if (!email) {
    errors.push("Where is ur emeil idiot?!");
  }
  if (email && !isEmailValid(email)) {
    errors.push("Invalid email address");
  }

  if (validateUsername) {
    if (!username) {
      errors.push("Where is ur username idiot?!");
    }

    if (username && !isUsernameValid(username)) {
      errors.push("Username should be longer than 3 characters");
    }
  }

  if (validatePassword) {
    if (!password) {
      errors.push("Where is ur password idiot?!");
    }

    if (password && !isPasswordValid(password)) {
      errors.push(
        "Password should be longer than 8 characters and contain at least 1 special character",
      );
    }
  }

  return errors;
};

export const isSignUpCredentialsValid = async (
  email: isOptionalString,
  username: isOptionalString,
  password: isOptionalString,
): Promise<string[]> => {
  return validateCredentials(email, username, password);
};

export const isSignInCredentialsValid = async (
  email: string,
  password: string,
): Promise<string[]> => {
  return validateCredentials(email, undefined, password, false);
};
