#Danny Radosevich
#An example of AES in julia

#Package adds, only need to uncommited on first run/update
using Pkg
#Pkg.add("AES")

#Using statments for all added packages 
using AES
using Random 
function stripAES(to_strip)
    re = r"(\[([\S\s]+?)\])"
    to_strip = join(to_strip)
    #println(to_strip)
    #println(typeof(to_strip))
    m = match(re,to_strip)
    if length(m) >=2
        return m[1],m[2]
    end
end

#need tor ead in the key
key = open("key.txt","r")
key = read(key,String)
k = []
for i in 1:16
    append!(k,hex2bytes(key[i]*key[i+1]))
    i+=1
end
#println(k)
k = AES128Key(k)
#key = Vector{UInt8}(key)
#println(length(k))

cipher = AESCipher(;key_length=128, mode = AES.CBC, key=k)
cipher_file = open("cipher.out","r")
cipher_file = read(cipher_file,String)
#print(cipher_file)

cipher_text, cipher_iv = stripAES(cipher_file)
#println(cipher_text)

cipher_vector = Vector{AES.CipherText}[]
#append!(cipher_vector,cipher_iv)
#append!(cipher_vector,cipher_text)
#println(typeof(AES.CipherText))
#println()
println(AESDecrypt(hex2bytes(cipher_text),k))
#print(String(decrypt(cipher_vector,cipher)))