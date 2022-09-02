# Danny Radosevich
# Encrypt a message with AES

#imports 
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad 
from base64 import b64decode, b64encode 
import  os 
import json 

#first we need to generate and save our key 
def unpad(message):
    message = str(message).replace("*","")
    message = message[2:len(message)-1]
    return message

def gen_AES_key(kl):
    key_length = kl #set the key leng, can make this static
    secretkey = os.urandom(key_length)  # just get random bytes
    keyf = open("key","w") #open a file to write out to. Obviously you wouldn't normally do this 
    keyf.write(secretkey) # write out the key
    keyf.close() # close the file
    return secretkey #return the key!

#set up our encryption 
def decrypt_message(message,key):
    json_in = json.loads(message)
    iv = json_in["iv"]
    cipher_text = json_in["cipher"]
    #print(iv)
    iv = b64decode(iv)
    cipher_text = b64decode(cipher_text)
    print("cipher bytes",str(len(cipher_text)))
    #print(iv)
    
    cipher = AES.new(key, AES.MODE_CBC,iv ) #using AES create a new cipher, based on our 'secret' key
    decrypt_cipher = cipher.decrypt(cipher_text)
    decrypt_cipher = unpad(decrypt_cipher)
    print(decrypt_cipher)

key = open("key").read()
key = b64decode(key)
print(key)
cipher = open("cipher.out").read()
decrypt_message(cipher,key)