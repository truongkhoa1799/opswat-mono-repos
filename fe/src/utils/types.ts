export type User = {
  id: string;
  email: string;
  username: string;
  fullname: string;
  created_at: string;
  updated_at: string;
};

export type Article = {
  id: string;
  title: string;
  body: string;
  favourite_count: number;
  created_at: string;
  updated_at: string;
  user: User;
};

export type MemberInfo = {
  id: string;
  created_at: string;
  email: string;
  fullname: string;
  updated_at: string;
  username: string;
};
