import React from "react";
import { Route, BrowserRouter, Routes } from "react-router-dom";
import ArticlesPage from "./components/pages/ArticlesPage";
import EditArticlePage from "./components/pages/EditArticlePage";
import LandingPage from "./components/pages/LandingPage";
import LoginPage from "./components/pages/Login";
import SignUpPage from "./components/pages/SignUp";
import UsersPage from "./components/pages/UsersPage";
import GlobalLoader from "./components/templates/GlobalLoader";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/sign-up" element={<SignUpPage />} />
        <Route
          path="/users"
          element={
            <GlobalLoader>
              <UsersPage />
            </GlobalLoader>
          }
        />
        <Route
          path="/articles"
          element={
            <GlobalLoader>
              <ArticlesPage />
            </GlobalLoader>
          }
        />
        <Route
          path="/article/edit"
          element={
            <GlobalLoader>
              <EditArticlePage />
            </GlobalLoader>
          }
        />
        <Route
          path="/article/edit/:articleId"
          element={
            <GlobalLoader>
              <EditArticlePage />
            </GlobalLoader>
          }
        />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
