from fastapi import APIRouter
from fastapi import WebSocket, WebSocketDisconnect

from core.settings import settings

router = APIRouter(
    prefix=settings.api.v1.notification,
    tags=["Уведомления"]
)

# 🌐🔁 ──────────────── ROUTERS ──────────────── 🔁🌐

active_connections: list = []


@router.websocket("/ws")
async def websocket_router(websocket: WebSocket) -> None:
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Получено уведомление {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)


async def send_notification(message: str) -> None:
    for connection in active_connections:
        await connection.send_text(message)
