import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidTag

def generate_key(password: str, salt: bytes) -> bytes:
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return key

def encrypt_word(word: str, key: bytes, salt: bytes) -> str:
    iv = os.urandom(12)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_word = encryptor.update(word.encode()) + encryptor.finalize()
    return (iv + salt + encryptor.tag + encrypted_word).hex()

def decrypt_word(encrypted_word: str, password: str) -> str:
    encrypted_word_bytes = bytes.fromhex(encrypted_word)
    
    if len(encrypted_word_bytes) < 44:
        raise ValueError("Encrypted word is too short to contain required components (IV, salt, tag, ciphertext)")

    iv = encrypted_word_bytes[:12]
    salt = encrypted_word_bytes[12:44]
    tag = encrypted_word_bytes[44:60]
    ciphertext = encrypted_word_bytes[60:]
    if len(ciphertext) == 0:
        raise ValueError("Ciphertext is empty")
    
    key = generate_key(password, salt)  # Usar el mismo salt que se utilizó para encriptar
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=backend)
    decryptor = cipher.decryptor()
    try:
        decrypted_word = decryptor.update(ciphertext) + decryptor.finalize()
    except InvalidTag:
        raise ValueError("Invalid authentication tag")
    return decrypted_word.decode('utf-8')