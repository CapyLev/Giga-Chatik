import {
  PublicServerResponseDTO,
  ServerImageDTOResponseDTO,
  UserServerDTO,
} from "../../interfaces/server.interface";
import axiosInst from "../../utils/axiosUtils";

export const getAllUserServers =
  async (): Promise<ServerImageDTOResponseDTO> => {
    const { data } = await axiosInst.get("/api/server/user-servers/", {
      withCredentials: true,
    });

    return data;
  };

export const joinToServer = async (
  server_id: string,
  password: string,
): Promise<UserServerDTO> => {
  const response = await axiosInst.post<UserServerDTO>(
    `/api/server/join/${server_id}`,
  );

  if (response.status === 401) {
  }

  return response.data;
};

export const getAllPublicServers =
  async (): Promise<PublicServerResponseDTO> => {
    const { data } = await axiosInst.get<PublicServerResponseDTO>(
      "/api/server/public-servers/",
    );
    return data;
  };
