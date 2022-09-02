#Danny Radosevich
#An example of AES in julia

#Package adds, only need to uncommited on first run/update
using Pkg
#Pkg.add("AES")

#Using statments for all added packages 
using AES
using Random 

#get the random bytes for our key
k = []
key_out = open("key.txt","w")
for i in 1:16
    # add a random byte 16 times to our array
    k_in = (bytes2hex(rand(UInt8,1)))
    write(key_out,k_in)
    append!(k,k_in)
end
#print(k)
#(bytes2hex(rand(UInt8,16)))

# Now we make our AES-128 key
key = AES128Key(k)

#create our cipher object 
cipher = AESCipher(;key_length=128,mode=AES.CBC, key = key)
#print(cipher)

#get our text to be encrypted, in this case the sorcerer stone script
plaintext = open("ragtime.txt","r")
plaintext = read(plaintext, String) 

#print(hp_one)
#encrypt the text 
ct = encrypt(plaintext,cipher)
#print(ct)
#ciphertext = open("cipher.txt","w")
#write(ciphertext,ct)
println(String(decrypt(ct,cipher)))