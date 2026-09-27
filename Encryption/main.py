from hybrid_e import hybrid_encrypt, hybrid_decrypt


print("===================================")
print("      SECURE MESSAGE SYSTEM")
print("===================================")

# User enters message
message = input("\nEnter your message: ")

# Hybrid encryption
encrypted_message, encrypted_aes_key, nonce, private_key = hybrid_encrypt(message)

print("\nMessage encrypted successfully!")

print("\nEncrypted Message:")
print(encrypted_message.hex())

print("\nEncrypted AES Key:")
print(encrypted_aes_key.hex())

# Hybrid decryption
decrypted_message = hybrid_decrypt(
    encrypted_message,
    encrypted_aes_key,
    nonce,
    private_key
)

print("\nDecrypted Message:")
print(decrypted_message)

print("\n===================================")
print("        PROCESS COMPLETED")
print("===================================")