# Danny Radosevich
# pip3 install cryptography
# RSA example
# https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/

import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

#generate our private key
private_key = rsa.generate_private_key(public_exponent=7457,key_size=2048,backend=default_backend())
public_key = private_key.public_key()

#now we can store the private  key
pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                    format=serialization.PrivateFormat.PKCS8,
                                    encryption_algorithm=serialization.NoEncryption())
with open("private_key.pem","wb") as f:
    f.write(pem)
    f.close()
#now we can do thee public key
pub_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
with open("public_key.pem","wb") as f:
    f.write(pub_pem)
    f.close()