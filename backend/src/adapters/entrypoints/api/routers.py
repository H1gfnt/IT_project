from fastapi import APIRouter
from backend.src.adapters.entrypoints.api.v1.index import index_router
from backend.src.adapters.entrypoints.api.v1.auth import auth_router
from backend.src.adapters.entrypoints.api.v1.users import users_router

api_router = APIRouter()

api_router.include_router(index_router.router,  tags=["Домашняя страница"])  # Убрать api/v1
api_router.include_router(auth_router.router, prefix='/auth', tags=["Аутентификация"])
api_router.include_router(users_router.router, prefix='/users', tags=["Пользователи"])
