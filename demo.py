# simple hashing function

def hash(text):
    return sum(ord(c) for c in text)

# print(hash("Hello"))

def hash2(text):
    return sum(ord(c) for c in text) % 10

# print(hash2("Hello"))

def salt(text, salt='salt'):
    return hash(text + salt)

# print(salt("Hello"))

####################################################################

# symmetric encryption

def caesar(text, shift=3):
    return ''.join(chr(ord(c) + 3) for c in text)

# print(caesar("ABC"))

def uncaesar(cipher, shift=3):
    return ''.join(chr(ord(c) - 3) for c in cipher)

# print(uncaesar("DEF"))

#################################################################

# Assymmetric encryption (RSA)


# Import the RSA module from the Crypto.PublicKey package which contains all
# the functions and classes for working with RSA keys.
from Crypto.PublicKey import RSA

# Import the PKCS1_OAEP module from the Crypto.Cipher package which contains
# all the functions and classes for performing the PKCS#1 OAEP encryption
# scheme.
#
# PKCS#1 OAEP encryption is a method of encrypting data using an RSA
# public key. It provides secure encryption for data of any size.
from Crypto.Cipher import PKCS1_OAEP
 

def generate_key_pair():
    """
    This function generates a new RSA key pair with a modulus length of 1024 bits.
    The key pair is used for asymmetric encryption and decryption.
    
    Returns:
        key (RSA.RsaKey): The key pair object containing the public and private keys.
    """
    
    # Generate a new RSA key pair with a modulus length of 1024 bits
    key = RSA.generate(1024) 
    
    # Return the key pair object containing the public and private keys
    return key

key_pair = generate_key_pair()

# print("public key : ", str(key_pair.publickey().exportKey()))
# print("private key : ", str(key_pair.exportKey()))

public_key = key_pair.publickey().exportKey()

def encrypt_message(msg, public_key):
    """
    Encrypts a message using the provided public key.

    Args:
        msg (bytes): The message to be encrypted.
        public_key (RSA.RsaKey): The public key used for encryption.

    Returns:
        bytes: The encrypted message.
    """
    cipher = PKCS1_OAEP.new(public_key)

    # Padding the message before encryption
    padded_msg = PKCS1_OAEP.new(public_key).encrypt(msg)
    
    enc_msg = cipher.encrypt(padded_msg)
    return enc_msg

print(encrypt_msg(b"Hello", key_pair.publickey()))
enc_text = encrypt_msg(b"Hello", key_pair.publickey())

def decrypt_msg(cipher_text, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    plain_text = cipher.decrypt(cipher_text)

    return plain_text

print(decrypt_msg(enc_text,key_pair))

