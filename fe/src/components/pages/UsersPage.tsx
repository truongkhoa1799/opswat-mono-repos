import Typography from "@mui/material/Typography/Typography";
import React, { useEffect, useState } from "react";
import { Helmet } from "react-helmet-async";
import MainLayout from "../templates/MainLayout";

import { Button, Pagination } from "@mui/material";
import UserListComponent from "../molecules/UserLists";
import { QUERY_KEY_GET_USERS } from "../../constants/queryKeys";
import * as userApi from "../../apis/users";
import { useMutation, useQuery } from "react-query";
import { User } from "../../utils/types";
import { Box, Stack } from "@mui/system";
import ConfirmModal from "../molecules/ConfirmModal";
import useModal from "../../hooks/useModal";

const USER_PER_PAGE = 10;

const UsersPage = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [page, setPage] = React.useState(1);
  const [totalPages, setTotalPages] = React.useState(0);
  const [modal, showModal] = useModal();

  const offset = (page - 1) * USER_PER_PAGE;
  const usersQuery = useQuery([QUERY_KEY_GET_USERS, offset], () => userApi.getUsers(offset, USER_PER_PAGE));

  const handleChange = (event: React.ChangeEvent<unknown>, value: number) => {
    setPage(value);
  };

  const removeUserMutation = useMutation<boolean, Error, string>({
    mutationFn: async (email: string) => await userApi.remoteUser(email),
    onSuccess(data: boolean) {
      if (data) {
        usersQuery.refetch();
      }
    },
  });

  useEffect(() => {
    if (usersQuery.data?.users) {
      const pages = Math.ceil(usersQuery.data.total / USER_PER_PAGE);
      setTotalPages(pages);
      setUsers(usersQuery.data.users);
    }
  }, [usersQuery.data]);

  const deleteUser = (email: string) => {
    showModal((onClose) => (
      <ConfirmModal
        title="Delete User"
        message="Are you sure you want to delete this user?"
        onAccept={() => {
          removeUserMutation.mutate(email);
          onClose();
        }}
        onDeny={onClose}
      />
    ));
  };

  return (
    <>
      <Helmet>
        <title>Users - OPSWAT System</title>
      </Helmet>
      <MainLayout>
        <h1>User Management</h1>
        <Stack spacing={2}>
          <UserListComponent users={users} removeUser={deleteUser} />
          <Stack direction="row" justifyContent="center" alignItems="baseline" spacing={2}>
            <Pagination count={totalPages} page={page} onChange={handleChange} color="secondary" size="large" />
          </Stack>
          {modal}
        </Stack>
      </MainLayout>
    </>
  );
};

export default UsersPage;
