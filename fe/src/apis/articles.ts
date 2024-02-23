import { ARTICLE_URL } from "../constants/urls";
import { serverApiClient } from "../utils/apiClient";
import { Article } from "../utils/types";

export type GetArticlesResponse = {
  articles: Article[];
  total: number;
};

export type CreateArticleParams = {
  title: string;
  body: string;
};

export type UpdateArticleParams = {
  id: string;
} & CreateArticleParams;

export const getArticles = async (offset: number, limit: number): Promise<GetArticlesResponse> => {
  const res = await serverApiClient.get(ARTICLE_URL.GetArticles, {
    params: { offset, limit },
  });

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }
  const response: GetArticlesResponse = res.data.data;
  return response;
};

export const getArticle = async (articleId: string): Promise<Article> => {
  const url = `${ARTICLE_URL.GetArticles}/${articleId}`;
  const res = await serverApiClient.get(url, {});

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }
  const response: Article = res.data.data;
  return response;
};

export const remoteArticle = async (articleId: string): Promise<boolean> => {
  const url = `${ARTICLE_URL.DeleteArticles}/${articleId}`;
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

export const updateArticle = async (params: UpdateArticleParams): Promise<Article> => {
  const data = new FormData();
  data.append("title", params.title);
  data.append("body", params.body);
  const url = `${ARTICLE_URL.UpdateArticles}/${params.id}`;
  const res = await serverApiClient.put(url, data, {
    headers: {
      "content-type": "multipart/form-data",
    },
  });

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }

  const response: Article = res.data.data;
  return response;
};

export const createArticle = async (params: CreateArticleParams): Promise<Article> => {
  const data = new FormData();
  data.append("title", params.title);
  data.append("body", params.body);
  const url = `${ARTICLE_URL.CreateArticles}`;
  const res = await serverApiClient.post(url, data, {
    headers: {
      "content-type": "multipart/form-data",
    },
  });

  if (res.data.status !== 200) {
    throw new Error(res.data.error);
  }

  const response: Article = res.data.data;
  return response;
};
