from fastapi import APIRouter
from .auth import router as auth_router
from .user import router as users_router
from .article import router as articles_router

api_router = router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(articles_router)
