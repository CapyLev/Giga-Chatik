import { ServerImageResponse } from "../../interfaces/server.interface";
import axiosInst from "../../utils/axiosUtils";

export const getAllUserServers = async (): Promise<ServerImageResponse> => {
  const { data } = await axiosInst.get("/api/server/user-servers/", {
    withCredentials: true,
  });

  return data;
};
