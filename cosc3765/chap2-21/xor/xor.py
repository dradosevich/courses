#Danny Radosevich
#An example of XOR for HW2 problem 3

import random
import base64

def byte_xor(one,two):
    b_xor = bytes(a^b for a,b in zip(one,two))
    return b_xor

key = b"thisisakey"
rand = b"samelength"
gen_string = byte_xor(key,rand)
print("The string partner A generated is ",gen_string)
returned_string = byte_xor(gen_string,key)
print("The string the partner returned is ", returned_string)
print("The returned string with the sent string is ",byte_xor(gen_string,returned_string))