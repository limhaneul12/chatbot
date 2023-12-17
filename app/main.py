from fastapi import FastAPI, Body, Request
from pydantic import HttpUrl

from app import models
from app.config import settings
from telegram_lib.telegram import Telegram
from telegram_lib import schema
from devtools import debug


app = FastAPI()
telegram = Telegram(settings.TELEGRAM_BOT_TOKEN)


@app.on_event("startup")
def on_startup():
    from app.database import engine

    models.Base.metadata.create_all(bind=engine)


@app.post("/")
async def webhook(request: Request):
    try:
        r = await request.json()
        print(r)
        debug(r)
        r = schema.Update.parse_obj(r)
        debug(r)
        return 'OK'
    except:
        print("sdfsdf")


@app.get("/me")
async def get_me():
    return await telegram.get_bot_info()


@app.get("/wb")
async def get_webhook():
    return await telegram.get_webhook()


@app.post("/wb")
async def set_webhook(url: HttpUrl = Body(..., embed=True)):
    return await telegram.set_webhook(url)
