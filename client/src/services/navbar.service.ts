import axiosInstance from "@/utils/axiosInst";
import { ServerImageResponse } from "@/interfaces/server.interfaces";

export const fetchServerIcons = async (): Promise<ServerImageResponse> => {
  const { data } = await axiosInstance.get(
    `http://localhost:6969/api/server/getAll`,
    {
      withCredentials: true,
    },
  );

  return data;
};
