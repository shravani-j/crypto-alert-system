from aes_util import generate_key, generate_nonce, encrypt, decrypt
from rsa_util import generate_keys, encrypt_key, decrypt_key


def hybrid_encrypt(message):

    # Generate AES key
    aes_key = generate_key()

    # Generate AES nonce
    nonce = generate_nonce()

    # Encrypt message using AES-GCM
    encrypted_message = encrypt(message, aes_key, nonce)

    # Generate RSA keys
    private_key, public_key = generate_keys()

    # Encrypt AES key using RSA public key
    encrypted_aes_key = encrypt_key(aes_key, public_key)

    return encrypted_message, encrypted_aes_key, nonce, private_key


def hybrid_decrypt(encrypted_message, encrypted_aes_key, nonce, private_key):

    # Decrypt AES key using RSA private key
    aes_key = decrypt_key(encrypted_aes_key, private_key)

    # Decrypt message using AES-GCM
    decrypted_message = decrypt(
        encrypted_message,
        aes_key,
        nonce
    )

    return decrypted_message