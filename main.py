from fastapi import FastAPI

from api.authentication import router as api_router


app = FastAPI(
    title="Chat Messages"
)

app.include_router(api_router)