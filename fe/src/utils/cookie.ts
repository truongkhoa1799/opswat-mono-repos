import moment from "moment";
import Cookies, { CookieSetOptions } from "universal-cookie";
import jwt_decode from "jwt-decode";
import { MemberInfo } from "./types";

const defaultOption: CookieSetOptions = {
  path: "/",
  expires: moment().add(120, "days").toDate(),
  secure: true,
  sameSite: "strict",
};

const COOKIE_NAME_LOGIN = "login";

type LoginCookie = {
  id: string;
};

export function getLoginCookie(redirectOnNotLoggedIn: boolean = false): string {
  try {
    const cookies = new Cookies();
    const value = cookies.get(COOKIE_NAME_LOGIN);

    if (value === undefined) {
      if (redirectOnNotLoggedIn) {
        window.location.href = `/login`;
      }
      return "";
    }

    return value;
  } catch (error) {
    console.error(error);
    return "";
  }
}

export function getLoginMemberId(redirectOnNotLoggedIn: boolean = false): LoginCookie | string {
  try {
    const token = getLoginCookie(redirectOnNotLoggedIn);
    const decoded = jwt_decode<LoginCookie>(token);
    return decoded["id"];
  } catch (error) {
    console.error(error);
    return "";
  }
}

export function getMemberInfo(redirectOnNotLoggedIn: boolean = false): MemberInfo | null {
  try {
    const token = getLoginCookie(redirectOnNotLoggedIn);
    const decoded = jwt_decode<MemberInfo>(token);
    return decoded;
  } catch (error) {
    console.error(error);
    return null;
  }
}

export function removeLoginCookie() {
  const cookies = new Cookies();
  cookies.remove(COOKIE_NAME_LOGIN, defaultOption);
}

export function setLoginCookie(token: string) {
  const cookies = new Cookies();
  cookies.set(COOKIE_NAME_LOGIN, token, defaultOption);
}
