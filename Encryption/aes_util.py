from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


def generate_key():
    return AESGCM.generate_key(bit_length=256)


def generate_nonce():
    return os.urandom(12)


def encrypt(message, key, nonce):
    aes = AESGCM(key)
    return aes.encrypt(nonce, message.encode(), None)


def decrypt(encrypted_message, key, nonce):
    aes = AESGCM(key)
    decrypted = aes.decrypt(nonce, encrypted_message, None)
    return decrypted.decode()