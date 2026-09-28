from aes_util import generate_key, generate_nonce, encrypt, decrypt


message = input("Enter message: ")

key = generate_key()
nonce = generate_nonce()

encrypted = encrypt(message, key, nonce)

print("\nEncrypted message:")
print(encrypted.hex())

decrypted = decrypt(encrypted, key, nonce)

print("\nDecrypted message:")
print(decrypted)