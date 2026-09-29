from rsa_util import generate_keys, encrypt_key, decrypt_key

# Generate RSA keys
private_key, public_key = generate_keys()

# For testing, we'll use a small AES-style key
test_key = b"12345678901234567890123456789012"

print("Original key:")
print(test_key)

# Encrypt the key using RSA public key
encrypted_key = encrypt_key(test_key, public_key)

print("\nEncrypted key:")
print(encrypted_key.hex())

# Decrypt the key using RSA private key
decrypted_key = decrypt_key(encrypted_key, private_key)

print("\nDecrypted key:")
print(decrypted_key)

# Verify
if test_key == decrypted_key:
    print("\nRSA encryption/decryption successful!")
else:
    print("\nRSA encryption/decryption failed!")