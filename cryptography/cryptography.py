def encrypt(text, key):
    """
    Encrypts the input text using a Caesar cipher.
    :param text: The string to encrypt.
    :param key: The shift value for encryption.
    :return: The encrypted string.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord(char) + key
            if char.islower():
                if shift > ord('z'):
                    shift -= 26
            elif char.isupper():
                if shift > ord('Z'):
                    shift -= 26
            encrypted_text += chr(shift)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    """
    Decrypts the input cipher text using a Caesar cipher.
    :param cipher_text: The string to decrypt.
    :param key: The shift value for decryption.
    :return: The decrypted string.
    """
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = ord(char) - key
            if char.islower():
                if shift < ord('a'):
                    shift += 26
            elif char.isupper():
                if shift < ord('A'):
                    shift += 26
            decrypted_text += chr(shift)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
original_text = "Python"
key = -2
encrypted_result = encrypt(original_text, key)
decrypted_result = decrypt(encrypted_result, key)

print(f"Original text: {original_text}")
print(f"Encrypted text: {encrypted_result}")
print(f"Decrypted text: {decrypted_result}")
