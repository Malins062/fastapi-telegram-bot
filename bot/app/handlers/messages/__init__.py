from aiogram import Router

from .crud_handlers import router as crud_handlers_router

router = Router(name="card")

router.include_routers(
    crud_handlers_router,
)
