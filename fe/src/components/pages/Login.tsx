import React, { useEffect, useState } from "react";
import { Helmet } from "react-helmet-async";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { useMutation } from "react-query";
import * as authApi from "../../apis/auth";
import { getLoginMemberId, setLoginCookie } from "../../utils/cookie";
import Toast from "../molecules/Toast";
import { Container } from "@mui/material";

const defaultTheme = createTheme();
const TIMEOUT_LOGIN = 1000;

const LoginPage = () => {
  const [isOpenToast, setIsOpenToast] = useState(false);
  const [isErrToast, setIsErrToast] = useState(false);

  useEffect(() => {
    const memberId = getLoginMemberId();
    if (memberId) {
      window.location.href = "/users";
    }
  }, []);

  const loginMutation = useMutation<authApi.LoginResponse, Error, authApi.LoginParams>({
    mutationFn: async (params: authApi.LoginParams) => await authApi.login(params),
    onSuccess(data: authApi.LoginResponse) {
      if (data) {
        setLoginCookie(data.access_token);
        setIsOpenToast(true);
        setTimeout(() => {
          window.location.href = "/users";
          setIsOpenToast(false);
        }, TIMEOUT_LOGIN);
      }
    },
    onError() {
      setIsErrToast(true);
      setTimeout(() => {
        setIsErrToast(false);
      }, TIMEOUT_LOGIN);
    },
  });

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const username = data.get("username");
    const password = data.get("password");

    if (username && password) {
      loginMutation.mutate({ username: username.toString(), password: password.toString() });
    } else {
      alert("Please enter a username and password");
    }
  };

  return (
    <>
      <Helmet>
        <title>Login - OPSWAT System</title>
      </Helmet>
      <ThemeProvider theme={defaultTheme}>
        <Container component="main" maxWidth="xs">
          <CssBaseline />
          <Box
            sx={{
              marginTop: 24,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign in
            </Typography>
            <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
              <TextField margin="normal" required fullWidth id="username" label="Username" name="username" autoComplete="username" autoFocus />
              <TextField margin="normal" required fullWidth name="password" label="Password" type="password" id="password" autoComplete="current-password" />
              <FormControlLabel control={<Checkbox value="remember" color="primary" />} label="Remember me" />
              <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
                Sign In
              </Button>
              <Grid container>
                <Grid item xs>
                  <Link href="#" variant="body2">
                    Forgot password?
                  </Link>
                </Grid>
                <Grid item>
                  <Link href="/sign-up" variant="body2">
                    {"Don't have an account? Sign Up"}
                  </Link>
                </Grid>
              </Grid>
            </Box>
          </Box>
        </Container>
      </ThemeProvider>
      <Toast isOpen={isOpenToast} severity="success" message="Login success" />
      <Toast isOpen={isErrToast} severity="error" message="Login failed" />
    </>
  );
};

export default LoginPage;
