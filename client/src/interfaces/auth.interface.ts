export interface signUpUserData {
  id: string;
  email: string;
  is_active: boolean;
  is_superuser: boolean;
  is_verified: boolean;
  username: string;
}

export interface shortUserInfoDTO {
  id: string;
  username: string;
  // TODO: image: string
}
