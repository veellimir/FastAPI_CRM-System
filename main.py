import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from actions.create_superuser import create_superuser
from api import router as api_router

from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    # await create_superuser()
    yield
    # shutdown


app = FastAPI(
    title="CRM System",
    description="🧠 CRM система —  управления клиентами и сотрудниками. ",
    lifespan=lifespan,
)

app.include_router(api_router)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-type", "Set-Cookie", "Access-Control-Allow-Headers", "Authorization"]
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
