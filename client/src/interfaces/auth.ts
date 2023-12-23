export interface SignUpResponse {
  id: string;
  password: string;
  email: string;
  is_active: boolean;
  is_superuser: boolean;
  is_verified: boolean;
  username: string;
}
