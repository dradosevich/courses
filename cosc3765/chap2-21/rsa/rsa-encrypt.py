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

#open up our key file
with open("public_key.pem","rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read(),backend=default_backend())
    key_file.close()

message = b'go pokes'
encrypted = public_key.encrypt(message, 
                                padding.OAEP(
                                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                algorithm=hashes.SHA256(), 
                                label=None))
print(encrypted)
with open("cipher","wb") as ciph:
    ciph.write(encrypted)
    ciph.close()