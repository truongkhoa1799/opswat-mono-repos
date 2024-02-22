from fastapi import APIRouter
from .user import router as user_router
from .auth import router as auth_router

api_router = router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

api_router.include_router(auth_router)
api_router.include_router(user_router)
