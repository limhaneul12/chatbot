from fastapi import FastAPI

import models
from app.config import settings
from lib.telegram import Telegram


app = FastAPI()
telegram = None


# fastapi 가 실행되면 해당 함수를 실행하겠다 
@app.on_event("startup")
def on_startup():
    from app.database import engine
    
    models.Base.metadata.create_all(bind=engine)

@app.get("/me")
async def get_me():
    return await telegram.get_bot_info()