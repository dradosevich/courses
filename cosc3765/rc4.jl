# Danny Radosevich
# Julia example of RC4 generation
using  Pkg
#Pkg.add("CryptoUtils")
#Pkg.add("Random")
#Pkg.add("OffsetArrays")
using CryptoUtils
using Random
#using OffsetArrays


#crypto.init()
s = []
t = []
k = []
randstring = bytes2hex(rand(UInt8,256))

function popS()
    for i in 1:256
        append!(k, randstring[i]*randstring[i+1])
        append!(t,k[i])
        i+=1
    end
    for i in 0:255
        append!(s,i) 
    end
 end

 function firstPermutate()
    j = 1
    for i in 1:256
        #print(i,j)
        j = (j + s[i] + convert(UInt8, t[i]))%256
        i+=1
        j+=1
        s[i],s[j] = s[j],s[i]
    end
 end
popS()
firstPermutate()
#print(randstring)