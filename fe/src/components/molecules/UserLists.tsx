import React from "react";
import { Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Pagination } from "@mui/material";
import { User } from "../../utils/types";
import { useGlobal } from "../../hooks/useGlobal";

type Props = {
  users: User[];
  removeUser: (email: string) => void;
};

const UserListComponent = ({ users, removeUser }: Props) => {
  const { memberInfo } = useGlobal();
  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Full Name</TableCell>
            <TableCell>Email</TableCell>
            <TableCell>Action</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {users.map((user) => (
            <TableRow key={user.id}>
              <TableCell>{user.id}</TableCell>
              <TableCell>{user.fullname}</TableCell>
              <TableCell>{user.email}</TableCell>
              <TableCell>
                <Button disabled={memberInfo.id === user.id} variant="contained" color="secondary" onClick={() => removeUser(user.email)}>
                  Delete
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default UserListComponent;
