import React from "react";
import { Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Pagination } from "@mui/material";
import { Article, User } from "../../utils/types";
import { useGlobal } from "../../hooks/useGlobal";
import DeleteIcon from "@mui/icons-material/Delete";
import ModeEditIcon from "@mui/icons-material/ModeEdit";
import { Stack } from "@mui/system";

type Props = {
  articles: Article[];
  removeArticle: (articleId: string) => void;
  updateArticle: (articleId: string) => void;
};

const ArticleListComponent = ({ articles, removeArticle, updateArticle }: Props) => {
  const { memberInfo } = useGlobal();
  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Title</TableCell>
            <TableCell>Favourite Count</TableCell>
            <TableCell>Created By</TableCell>
            <TableCell>Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {articles.map((article) => (
            <TableRow key={article.id}>
              <TableCell>{article.id}</TableCell>
              <TableCell>{article.title}</TableCell>
              <TableCell>{article.favourite_count}</TableCell>
              <TableCell>{article.user.email}</TableCell>
              <TableCell>
                <Stack spacing={1} direction="row">
                  <Button disabled={article.user.id !== memberInfo.id} variant="contained" endIcon={<ModeEditIcon />} onClick={() => updateArticle(article.id)}>
                    Edit
                  </Button>
                  <Button disabled={article.user.id !== memberInfo.id} variant="outlined" endIcon={<DeleteIcon />} onClick={() => removeArticle(article.id)}>
                    Delete
                  </Button>
                </Stack>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default ArticleListComponent;
