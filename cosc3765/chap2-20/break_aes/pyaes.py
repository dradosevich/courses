# Danny Radosevich
# example from: https://ahsmart.com/pub/hacking_aes_ecb_mode_cipher/

#imports
from Crypto.Cipher import AES
import os 
import numpy as np
#pad our message to be an appropriate size
def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16-len(message)%16)
    return message 
def encrypt(key, plain):
    cipher = AES.new(key.decode(),AES.MODE_ECB)
    return cipher.encrypt(plain)

mess = input("Please input your message\n")
key = b"0123456789abcdef0123456789abcdef"
#print(key)
output = open("ecrypted.out","w")
encrypted_message = encrypt(key,pad(mess))
print(encrypted_message)
output.write(str(encrypted_message))
output.close()