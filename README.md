# Python Criptor #

## Comandos para lanzarlo manualmente ##

uvicorn src.app.main:app --host 0.0.0.0 --port 8080

## Se puede lanzar con Docker ##

```shell
docker run -d --name python-criptor ggchavezhotmail/python-cryptor:v1 -p 8080:8080
```

## Ejecutar Metodo Encriptar ##

```shell
curl --location 'http://127.0.0.1:8080/encrypt' \
--data '{
    "words" : [
        "texto a encriptar",
        "otro texto a encriptar",
        "algun otro texto a encriptar"
        ],
    "password" : "llave-ultra-secreta"
}'
```

## Ejecutar Metodo Desencriptar ##

```shell
curl --location 'http://127.0.0.1:8080/decrypt' \
--data '{
    "words" : [
        "texto encriptado",
        "otro texto a encriptado",
        "algun otro texto encriptado"
        ],
    "password" : "llave-ultra-secreta"
}'
```

## Ejecutar Metodo Encriptar AES##

```shell
curl --location 'http://127.0.0.1:8080/encrypt_aes' \
--data '{
    "words" : [
        "texto a encriptar",
        "otro texto a encriptar",
        "algun otro texto a encriptar"
        ],
    "key" : "llave-ultra-secreta",
    "iv" : "llave-ultra-secreta"
}'
```

## Ejecutar Metodo Desencriptar AES##

```shell
curl --location 'http://127.0.0.1:8080/decrypt_aes' \
--data '{
    "words" : [
        "texto encriptado",
        "otro texto a encriptado",
        "algun otro texto encriptado"
        ],
    "key" : "llave-ultra-secreta",
    "iv" : "llave-ultra-secreta"
}'
```
