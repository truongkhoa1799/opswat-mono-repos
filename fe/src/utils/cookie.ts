import moment from "moment";
import Cookies, { CookieSetOptions } from "universal-cookie";
import jwt_decode from "jwt-decode";

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

export function getLoginMemberId(redirectOnNotLoggedIn: boolean = false): LoginCookie | string {
  const cookies = new Cookies();
  const value = cookies.get(COOKIE_NAME_LOGIN);

  if (value === undefined) {
    if (redirectOnNotLoggedIn) {
      window.location.href = `/login`;
    }
    return "";
  }

  const decoded = jwt_decode<LoginCookie>(value);
  return decoded["id"];
}

export function removeLogin() {
  const cookies = new Cookies();
  cookies.remove(COOKIE_NAME_LOGIN, defaultOption);
}

export function setLogin(token: string) {
  const cookies = new Cookies();
  cookies.set(COOKIE_NAME_LOGIN, token, defaultOption);
}
