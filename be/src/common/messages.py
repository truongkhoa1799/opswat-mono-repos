from enum import Enum


class UserErrMsg(Enum):
    DO_NOT_AUTHORIZED = 'do_not_authorized'
    FAIL_CREATE_USER = 'fail_create_user'
    FAIL_LOGIN_USER = 'fail_login_user'
    FAIL_GET_USERS = 'fail_get_users'
    FAIL_DELETE_USERS = 'fail_delete_users'
