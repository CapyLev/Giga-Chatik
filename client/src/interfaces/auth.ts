export interface SignInResponse {
  access_token: string;
  token_type: string;
}

export interface SignUpResponse {
  password: string;
  email: string;
  is_active: boolean;
  is_superuser: boolean;
  is_verified: boolean;
  username: string;
}
