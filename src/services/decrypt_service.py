from src.utils.utils import decrypt_word
from src.utils.aes import invoke_aes_decrypt


def handle_decrypt_service(body: dict):
    try:
        print(f"[Service]-[handle_decrypt_service] init {body}")
        encrypted_words = body.get("words")
        password = body.get("password")
        if not encrypted_words or not password:
            raise ValueError(
                "Las palabras encriptadas y la contraseña son necesarias")

        # print("[handle_decrypt_service] key: %s" % key.hex())
        decrypted_words = [decrypt_word(encrypted_word, password) for encrypted_word in encrypted_words]
        return {"decrypted_words": decrypted_words}
    except Exception as e:
        print(f"Error en handle_decrypt_service: {e}")
        raise


def handle_decrypt_aes_service(body: dict):
    try:
        print(f"[Service]-[handle_decrypt_aes_service] init {body}")
        encrypted_words = body.get("words")
        key = body.get("key")
        iv = body.get("iv")
        if not encrypted_words or not key or not iv:
            raise ValueError(
                "Las palabras encriptadas, key y la iv son necesarias")
        
        decrypted_words = [invoke_aes_decrypt(encrypted_word, key, iv) for encrypted_word in encrypted_words]
        return {"decrypted_words": decrypted_words}
    except Exception as e:
        print(f"Error en handle_decrypt_service: {e}")
        raise