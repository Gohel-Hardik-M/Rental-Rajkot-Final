from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from routers.home import router

app = FastAPI()


app.add_middleware(
    SessionMiddleware,
    secret_key="hardik_123456789_secret_key"
)

# CSS, JS, Images
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)