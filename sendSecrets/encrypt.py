from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt(key, plaintext):
    # Generate a random 16-byte IV
    iv = os.urandom(16)
    
    # Create a Cipher object using the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Pad the plaintext to be a multiple of the block size (16 bytes for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()
    
    # Encrypt the padded plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    # Return the IV and ciphertext concatenated
    return iv + ciphertext

# Example usage
key = os.urandom(32)  # AES-256 key
plaintext = "This is a secret message."
encrypted_message = encrypt(key, plaintext)
print(encrypted_message)
