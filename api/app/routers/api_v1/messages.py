from fastapi import APIRouter
from fastapi.routing import APIRoute

from ...config import settings
from ...db.crud.messages import create_message, get_messages

routes = [
    APIRoute(
        path=settings.api.v1.messages,
        endpoint=get_messages,
        methods=["GET"],
    ),
    APIRoute(
        path=settings.api.v1.message,
        endpoint=create_message,
        methods=["POST"],
    ),
]

router = APIRouter(
    routes=routes,
)
