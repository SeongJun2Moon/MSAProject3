import os
import sys
import logging
from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware

from .database import init_db
from .admin.utils import current_time
from app.env import DB_URL
from app.routers.user import router as user_router
from app.routers.article import router as article_router
from fastapi.middleware.cors import CORSMiddleware

print(f" ################ app.main Started At {current_time()} ################# ")
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(article_router, prefix="/articles", tags=["articles"])

app = FastAPI()
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.router.redirect_slashes = False
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message ": " Welcome Fastapi"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}