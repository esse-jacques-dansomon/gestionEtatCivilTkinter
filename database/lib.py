from cryptography.fernet import Fernet

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)


def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)


def encoder():
    # S92TslgmoG9Y-CAS1-bjruabjI3wmpkdjsKSH_zpN3o=
    key = Fernet.generate_key()

    print(key)
    password = "duCalmeZebi"

    token = encrypt(password.encode(), key)

    print(token)


def decoder(token):
    key = b'1VxKAq5tXhilOeJUzgeEQL7xQ_2Idgx4FW_EpBngEPE='

