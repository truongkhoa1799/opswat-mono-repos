import { getMemberInfo } from "../utils/cookie";
import { MemberInfo } from "../utils/types";

type useGlobalResponse = {
  memberInfo: MemberInfo;
};

export function useGlobal(): useGlobalResponse {
  const memberInfo = getMemberInfo(true);

  if (!memberInfo) {
    throw new Error("global data is not loaded");
  }

  return { memberInfo };
}
