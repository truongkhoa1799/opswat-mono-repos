import Typography from "@mui/material/Typography/Typography";
import React, { useEffect, useState } from "react";
import { Helmet } from "react-helmet-async";
import MainLayout from "../templates/MainLayout";
import * as articleApi from "../../apis/articles";

import { Button, InputBase, Paper, Stack, TextField } from "@mui/material";
import SaveAsIcon from "@mui/icons-material/SaveAs";
import { useParams, useNavigate } from "react-router-dom";
import { useMutation, useQuery } from "react-query";
import { QUERY_KEY_GET_ARTICLE } from "../../constants/queryKeys";
import { useImmer } from "use-immer";
import { Article } from "../../utils/types";
import Toast from "../molecules/Toast";

type Params = {
  articleId: string;
};

const EditArticlePage = () => {
  const navigate = useNavigate();
  const { articleId } = useParams<Params>();
  console.log("articleId: ", articleId);
  const [article, setArticle] = useImmer({
    title: "",
    body: "",
  });

  const articleQuery = useQuery([QUERY_KEY_GET_ARTICLE, articleId], () => {
    if (!articleId) {
      return null;
    }

    return articleApi.getArticle(articleId);
  });

  const updateMutation = useMutation<Article, Error, articleApi.UpdateArticleParams>({
    mutationFn: async (params: articleApi.UpdateArticleParams) => await articleApi.updateArticle(params),
    onSuccess(data: Article) {
      if (data) {
        navigate("/articles");
      }
    },
    onError() {
      alert("Fail to update article");
    },
  });

  const createMutation = useMutation<Article, Error, articleApi.CreateArticleParams>({
    mutationFn: async (params: articleApi.CreateArticleParams) => await articleApi.createArticle(params),
    onSuccess(data: Article) {
      if (data) {
        navigate("/articles");
      }
    },
    onError() {
      alert("Fail to create article");
    },
  });

  const handleChangeTitle = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const title = event.target.value;
    setArticle({ ...article, title: title });
  };

  const handleChangeBody = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const body = event.target.value;
    setArticle({ ...article, body: body });
  };

  const handleSummit = () => {
    if (article.title.length > 250 || article.body.length > 10000) {
      alert("Please fill maximum 250 characters for title and 10000 characters for body");
      return;
    } else if (article.title.length === 0 || article.body.length === 0) {
      alert("Please fill in all fields");
      return;
    }

    if (articleId) {
      updateMutation.mutate({
        id: articleId,
        title: article.title,
        body: article.body,
      });
    } else {
      createMutation.mutate({
        title: article.title,
        body: article.body,
      });
    }
  };

  useEffect(() => {
    if (articleQuery.data) {
      setArticle({
        title: articleQuery.data.title,
        body: articleQuery.data.body,
      });
    }
  }, [articleQuery.data]);

  return (
    <>
      <Helmet>
        <title>Edit Article - OPSWAT System</title>
      </Helmet>
      <MainLayout>
        <Stack flexDirection="row" justifyContent="space-between" alignItems="center">
          <h1>{articleId ? "Edit Article" : "Create Article"}</h1>
          <Button sx={{ height: "50px", width: "100px" }} variant="contained" endIcon={<SaveAsIcon />} onClick={handleSummit}>
            Save
          </Button>
        </Stack>
        <Stack spacing={2} height="100%" width="100%">
          <Paper component="form" sx={{ p: "2px 4px", display: "flex", alignItems: "center", width: "100%", height: 50 }}>
            <InputBase sx={{ ml: 1, width: "100%", flex: 1 }} placeholder="Title" inputProps={{ "aria-label": "search google maps" }} value={article.title} onChange={handleChangeTitle} />
          </Paper>
          <Paper component="form" sx={{ display: "flex", alignItems: "center", width: "100%" }}>
            <TextField required id="standard-multiline-static" label="Body" multiline rows={25} defaultValue="Default Value" variant="outlined" fullWidth value={article.body} onChange={handleChangeBody} helperText="Maximum 10000 characters" />
          </Paper>
        </Stack>
      </MainLayout>
    </>
  );
};

export default EditArticlePage;
