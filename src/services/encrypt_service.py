import os
from fastapi import HTTPException
from src.utils.utils import generate_key, encrypt_word


def handle_encrypt_service(body: dict):
    try:
        print(f"[Service]-[handle_encrypt_service] init {body}")
        words = body.get("words")
        password = body.get("password")
        if not words or not password:
            raise HTTPException(
                status_code=400, detail="Words and password are required")

        salt = os.urandom(32)
        key = generate_key(password, salt)
        encrypted_words = [encrypt_word(word, key, salt) for word in words]
        return {"encrypted_words": encrypted_words, "salt": salt.hex()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
