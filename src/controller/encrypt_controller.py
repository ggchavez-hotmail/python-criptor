from fastapi import Request
from fastapi.responses import JSONResponse
from src.services.encrypt_service import handle_encrypt_service
import logging

async def handle_encrypt(request: Request):
    try:
        print("[Controller]-[handle_encrypt] Encrypt")
        body = await request.json()
        print(f"[Controller]-[handle_encrypt] Encrypt {body}")
        response = handle_encrypt_service(body)
        return JSONResponse(content=response)
    except Exception as e:
        logging.error(f"Error en handle_encrypt: {e}")
        return JSONResponse(content={"error": "Ocurrió un error"}, status_code=500)
