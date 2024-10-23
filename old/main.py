import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def get_key():
    # Recuperar la llave de cifrado desde una variable de ambiente
    #key = os.getenv('ENCRYPTION_KEY')
    key = "PALABRA MUY SECRETA NADIE LA DEBE SABER"
    if key is None:
        raise ValueError("No encryption key found in environment variables.")
    return key.encode()[:32]  # Asegurarse de que la llave tenga 32 bytes para AES-256

def encrypt(data):
    key = get_key()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv + ct

def decrypt(enc_data):
    key = get_key()
    iv = base64.b64decode(enc_data[:24])
    ct = base64.b64decode(enc_data[24:])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# Ejemplo de uso
if __name__ == "__main__":
    #original_data = "sftp://despat0a:Ripley.,2024$@192.168.83.76:22"
    original_data = "/tmp/test/"
    other_encrypted_data = "t14zhsN1UfNWapax0or9tg==h/wd/2QDDztFuAc9Lu342w=="
    print(f"Original Data: {original_data}")

    encrypted_data = encrypt(original_data)
    print(f"Encrypted Data: {encrypted_data}")

    decrypted_data = decrypt(other_encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")
