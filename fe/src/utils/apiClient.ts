import axios from "axios";
import config from "../config";
import { getLoginCookie } from "./cookie";

export const serverApiClient = axios.create({
  baseURL: config.API_URL,
  headers: {
    Authorization: `Bearer ${getLoginCookie()}`,
  },
});
