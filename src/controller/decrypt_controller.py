from fastapi import Request
from fastapi.responses import JSONResponse
from src.services.decrypt_service import handle_decrypt_service
import logging

async def handle_decrypt(request: Request):
    try:
        print("[Controller]-[handle_decrypt] Decrypt")
        body = await request.json()
        print(f"[Controller]-[handle_decrypt] Decrypt {body}")
        response = handle_decrypt_service(body)
        return JSONResponse(content=response)
    except Exception as e:
        logging.error(f"Error en handle_decrypt: {e}")
        return JSONResponse(content={"error": "Ocurrió un error"}, status_code=500)