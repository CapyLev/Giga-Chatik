import { shortUserInfoDTO } from "./auth.interface";

export interface ServerDTO {
  id: string;
  name: string;
  image: string;
  is_public: boolean;
  password: string | null;
  admin_id: string;
  desc: string;
  created_at: Date;
}

export interface ServerImageDTO {
  id: string;
  image: string;
}

export interface ServerImageDTOResponseDTO {
  result: ServerImageDTO[];
}

export interface UserServerDTO {
  id: number;
  user_id: string;
  created_at: Date;
  server: ServerDTO;
}

export interface PublicServerDTO {
  id: string;
  image: string;
  name: string;
  admin: shortUserInfoDTO;
  desc: string;
  countOfMembers: number;
}

export interface PublicServerResponseDTO {
  result: PublicServerDTO[];
}
