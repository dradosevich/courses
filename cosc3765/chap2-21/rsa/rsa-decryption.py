# Danny Radosevich
# pip3 install cryptography
# RSA example
# https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/

import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

#open out our private key
with open("private_key.pem","rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
#open up our cipher file
with open("cipher","rb") as encrypted:
    encrypted = encrypted.read()

#decrypt the message 
original_message = private_key.decrypt(encrypted,
                                        padding.OAEP(
                                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(),
                                            label=None))

#print out the message
print(original_message)