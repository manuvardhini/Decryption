from cryptography.fernet import Fernet

def aes_decrypt(ciphertext, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(ciphertext)
    return decrypted_message.decode()

# Example usage
ciphertext = b'gAAAAABf8MqLHehxP5I5YvWgA4kMvGUpYbtxI4XZbtD5RJ9RsC4rYYzM_PpUahxGQ6Xv0s1HdH2AdEz7Kl5ChEksddWV1wrl_A=='
key = b'rH7XiK6BrW0HsKxg1AhtVTLIasI3X6VN_hnZaE-Z2bQ='

decrypted_text = aes_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
