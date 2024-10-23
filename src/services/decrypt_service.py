from src.utils.utils import decrypt_word


def handle_decrypt_service(body: dict):
    try:
        encrypted_words = body.get("words")
        password = body.get("password")
        if not encrypted_words or not password:
            raise ValueError(
                "Las palabras encriptadas y la contraseña son necesarias")

        # print("[handle_decrypt_service] key: %s" % key.hex())
        decrypted_words = [decrypt_word(encrypted_word, password)
                           for encrypted_word in encrypted_words]
        return {"decrypted_words": decrypted_words}
    except Exception as e:
        print(f"Error en handle_decrypt_service: {e}")
        raise
