import React from "react";
import { getLoginMemberId } from "../../utils/cookie";

type Props = {
  children: JSX.Element;
};
const GlobalLoader = ({ children }: Props) => {
  const memberId = getLoginMemberId(true);
  return <div>{children}</div>;
};

export default GlobalLoader;
