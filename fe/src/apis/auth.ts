import axios from "axios";
import { AUTHN_URLS } from "../constants/urls";
import { serverApiClient } from "../utils/apiClient";
import config from "./../config";

export type LoginParams = {
  username: string;
  password: string;
};

export type SignUpParams = {
  username: string;
  password: string;
  email: string;
  fullName: string;
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

  const res = await serverApiClient.post(AUTHN_URLS.Login, data, {
    headers: {
      "content-type": "multipart/form-data",
    },
  });

  const response: LoginResponse = res.data.data;

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }

  return response;
};

export const signUp = async (params: SignUpParams): Promise<LoginResponse> => {
  const data = new FormData();
  data.append("username", params.username);
  data.append("password", params.password);
  data.append("fullname", params.fullName);
  data.append("email", params.email);

  const res = await serverApiClient.post(AUTHN_URLS.Signup, data, {
    headers: {
      "content-type": "multipart/form-data",
    },
  });

  const response: LoginResponse = res.data.data;

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }

  return response;
};
