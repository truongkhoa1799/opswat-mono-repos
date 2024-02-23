import axios from "axios";
import config from "../config";
import { USER_URL } from "../constants/urls";
import { serverApiClient } from "../utils/apiClient";
import { getLoginCookie } from "../utils/cookie";
import { User } from "../utils/types";

export type GetUsersResponse = {
  users: User[];
  total: number;
};

export const getUsers = async (offset: number, limit: number): Promise<GetUsersResponse> => {
  const res = await serverApiClient.get(USER_URL.GetUsers, {
    params: { offset, limit },
  });

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }
  const response: GetUsersResponse = res.data.data;
  return response;
};

export const remoteUser = async (email: string): Promise<boolean> => {
  const url = `${USER_URL.DeleteUsers}/${email}`;
  const res = await serverApiClient.delete(url, {
    headers: {
      "content-type": "multipart/form-data",
    },
  });

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }

  const response: boolean = res.data.data;
  return response;
};
