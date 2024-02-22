import axios from "axios";
import { AUTHN_URLS } from "../constants/urls";
import config from "./../config";

export type LoginParams = {
  username: string;
  password: string;
};

export type LoginResponse = {
  id: string;
  email: string;
  username: string;
  fullName: string;
  created_at: string;
  updated_at: string;
  access_token: string;
};

export const login = async (params: LoginParams): Promise<LoginResponse> => {
  const data = new FormData();
  data.append("username", params.username);
  data.append("password", params.password);

  const url = `${config.API_URL}${AUTHN_URLS.Login}`;

  const res = await axios.post(url, data, {
    headers: {
      "content-type": "multipart/form-data",
    },
    withCredentials: true,
  });

  const response: LoginResponse = res.data.data;

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }

  return response;
};
