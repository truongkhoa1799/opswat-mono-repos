from enum import Enum


class UserErrMsg(Enum):
    DO_NOT_AUTHORIZED = 'do_not_authorized'
    FAIL_CREATE_USER = 'fail_create_user'
    FAIL_LOGIN_USER = 'fail_login_user'
    FAIL_GET_USERS = 'fail_get_users'
    FAIL_DELETE_USER = 'fail_delete_users'


class ArticleErrMsg(Enum):
    FAIL_CREATE_ARTICLE = 'fail_create_article'
    FAIL_UPDATE_ARTICLE = 'fail_update_article'
    FAIL_GET_ARTICLES = 'fail_get_articles'
    FAIL_DELETE_ARTICLE = 'fail_delete_article'

    FAIL_REACT_ARTICLE = 'fail_react_article'
    ARTICLE_NOT_EXIST = 'article_not_exist'

