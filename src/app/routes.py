from src.controller.decrypt_controller import handle_decrypt
from src.controller.encrypt_controller import handle_encrypt
from fastapi import APIRouter, Request
import sys
sys.path.append('src')

router = APIRouter()


@router.post("/encrypt")
async def home(request_body: Request):
    return await handle_encrypt(request_body)


@router.post("/decrypt")
async def home(request_body: Request):
    return await handle_decrypt(request_body)
