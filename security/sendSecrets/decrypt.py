def decrypt(key, encrypted_message):
    # Extract the IV and ciphertext
    iv = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    
    # Create a Cipher object using the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plaintext.decode()

# # Example usage
# decrypted_message = decrypt(key, encrypted_message)
# print(decrypted_message)
