import Typography from "@mui/material/Typography/Typography";
import React, { useEffect, useState } from "react";
import { Helmet } from "react-helmet-async";
import MainLayout from "../templates/MainLayout";

import { Button, Pagination } from "@mui/material";
import { QUERY_KEY_GET_ARTICLES } from "../../constants/queryKeys";
import * as articleApi from "../../apis/articles";
import { useMutation, useQuery } from "react-query";
import { Article, User } from "../../utils/types";
import { Box, Stack } from "@mui/system";
import ConfirmModal from "../molecules/ConfirmModal";
import useModal from "../../hooks/useModal";
import ArticleListComponent from "../molecules/ArticleLists";
import { useNavigate } from "react-router-dom";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";

const ARTICLE_PER_PAGE = 5;

const ArticlesPage = () => {
  const [articles, setArticles] = useState<Article[]>([]);
  const [page, setPage] = React.useState(1);
  const [totalPages, setTotalPages] = React.useState(0);
  const [modal, showModal] = useModal();
  const navigate = useNavigate();

  const offset = (page - 1) * ARTICLE_PER_PAGE;
  const articlesQuery = useQuery([QUERY_KEY_GET_ARTICLES, offset], () => articleApi.getArticles(offset, ARTICLE_PER_PAGE));

  const handleChange = (event: React.ChangeEvent<unknown>, value: number) => {
    setPage(value);
  };

  const removeUserMutation = useMutation<boolean, Error, string>({
    mutationFn: async (articleId: string) => await articleApi.remoteArticle(articleId),
    onSuccess(data: boolean) {
      if (data) {
        articlesQuery.refetch();
      }
    },
  });

  useEffect(() => {
    if (articlesQuery.data?.articles) {
      const pages = Math.ceil(articlesQuery.data.total / ARTICLE_PER_PAGE);
      setTotalPages(pages);
      setArticles(articlesQuery.data.articles);
    }
  }, [articlesQuery.data]);

  const deleteArticle = (articleId: string) => {
    showModal((onClose) => (
      <ConfirmModal
        title="Delete Article"
        message="Are you sure you want to delete this article?"
        onAccept={() => {
          removeUserMutation.mutate(articleId);
          onClose();
        }}
        onDeny={onClose}
      />
    ));
  };

  const updateArticle = (articleId: string) => {
    showModal((onClose) => (
      <ConfirmModal
        title="Update Article"
        message="Are you sure you want to update this article?"
        onAccept={() => {
          navigate(`/article/edit/${articleId}`);
          onClose();
        }}
        onDeny={onClose}
      />
    ));
  };

  return (
    <>
      <Helmet>
        <title>Articles - OPSWAT System</title>
      </Helmet>
      <MainLayout>
        <Stack flexDirection="row" justifyContent="space-between" alignItems="center">
          <h1>Articles Management</h1>
          <Button sx={{ height: "50px", width: "100px" }} variant="outlined" endIcon={<AddCircleOutlineIcon />} onClick={() => navigate(`/article/edit`)}>
            New
          </Button>
        </Stack>
        <Stack spacing={2}>
          <ArticleListComponent articles={articles} updateArticle={updateArticle} removeArticle={deleteArticle} />
          <Stack direction="row" justifyContent="center" alignItems="baseline" spacing={2}>
            <Pagination count={totalPages} page={page} onChange={handleChange} color="secondary" size="large" />
          </Stack>
          {modal}
        </Stack>
      </MainLayout>
    </>
  );
};

export default ArticlesPage;
