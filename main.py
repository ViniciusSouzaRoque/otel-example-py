from typing import Union

from fastapi import FastAPI

from contextlib import asynccontextmanager
import logging

@asynccontextmanager
async def lifespan(app):
    logger.info('Iniciando app')
    yield
    logger.info('Finalizando app')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    
