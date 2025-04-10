import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def invoke_aes_encrypt(data: str, key_bytes_: str, iv_bytes_: str) -> str:
    """
    Encrypts data using AES with CBC mode and PKCS#5 padding.

    Args:
        data: The string data to encrypt.
        key_bytes_: The encryption key as a string.
        iv_bytes_: The initialization vector as a string.

    Returns:
        A tuple containing the base64-encoded ciphertext and any error that occurred.
    """
    key_bytes = key_bytes_.encode('utf-8')
    iv_bytes = iv_bytes_.encode('utf-8')
    data_bytes = data.encode('utf-8')
    block_size = AES.block_size

    padded_plaintext = pad(data_bytes, block_size)
    try:
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        ciphertext = cipher.encrypt(padded_plaintext)
        resp = base64.b64encode(ciphertext).decode('utf-8')
        return resp
    except Exception as e:
        raise ValueError(f"invoke_aes_encrypt block :: {e}")

def invoke_aes_decrypt(data: str, key_bytes_: str, iv_bytes_: str) -> str:
    """
    Decrypts base64-encoded ciphertext using AES with CBC mode and PKCS#5 padding.

    Args:
        data: The base64-encoded ciphertext string.
        key_bytes_: The decryption key as a string.
        iv_bytes_: The initialization vector as a string.

    Returns:
        A tuple containing the decrypted string and any error that occurred.
    """
    key_bytes = key_bytes_.encode('utf-8')
    iv_bytes = iv_bytes_.encode('utf-8')

    try:
        crypt = base64.b64decode(data)
        if not crypt:
            raise ValueError("plain content empty")
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        decrypted = cipher.decrypt(crypt)
        resp = unpad(decrypted, AES.block_size).decode('utf-8')
        return resp
    except Exception as e:
        raise ValueError(f"key error1 {e}")