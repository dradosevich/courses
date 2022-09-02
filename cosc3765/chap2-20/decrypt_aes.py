#Danny Radosevich
#Decrypt the AES encoding done in Julia

#imports
from Crypto.Cipher import AES
import binascii, os
#read in our key, remember normally this should be secured
key = open("key.txt")
key = bytes(key.read(),"utf-8")
print(key)
cipher = AES.new(key,AES.MODE_CBC)
#print(cipher.decrypt(open("cipher.txt").read()))