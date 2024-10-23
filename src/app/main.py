from fastapi import FastAPI
from src.modules.logging.logging_default import logger
from src.app.routes import router

import sys
sys.path.append('src')

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    logger("INFO", "Application startup")


@app.on_event("shutdown")
async def shutdown_event():
    logger("INFO", "Application shutdown")
