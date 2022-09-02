# Danny Radosevich
# Encrypt a message with AES

#imports 
from Crypto.Cipher import AES  
from base64 import b64encode 
from Crypto.Random import get_random_bytes
import os 
import json 

#AES needs messages to be properly papped so
def pad(mess):
    return mess + ('*'*((16-len(mess))%16))

#first we need to generate and save our key 

def gen_AES_key():
    secretkey = os.urandom(16)  # just get random bytes
    keyf = open("key","w") #open a file to write out to. Obviously you wouldn't normally do this 
    print("key",secretkey)
    keyf.write(b64encode(secretkey).decode("utf-8")) # write out the key
    keyf.close() # close the file
    return secretkey #return the key!

#set up our encryption 
def encrypt_message(message, key):
    iv = os.urandom(16)
    #print(iv)
    cipher = AES.new(key, AES.MODE_CBC,iv ) #using AES create a new cipher, based on our 'secret' key 
    #AES requires block lengths that are multiples of 16, so must pad
    # our message needs to be as bytes
    cipher_bytes = cipher.encrypt(message)
    print("cipher bytes",cipher_bytes)
    #encode the bytes for output
    cipher_text = b64encode(cipher_bytes).decode("utf-8")
    #open our file
    cipher_out = open("cipher.out","w")
    #write out the file
    #print(iv)
    iv = b64encode(iv).decode("utf-8")
    #cipher_text = b64encode(cipher_text).decode("utf-8")
    #print(iv)
    #cipher_text = b64encode(cipher_text).decode("utf-8")
    json_out = json.dumps({'iv':iv,'cipher':cipher_text})
    cipher_out.write(json_out)
    #close it
    cipher_out.close() 

message = input("Please input a message:\n")
secretkey = gen_AES_key()
encrypt_message(pad(message),secretkey)