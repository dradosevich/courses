# Danny Radosevich
# RC4 Example
import os 

s = []
t = []
k = []
key = os.urandom(256)
'''
To begin the entries of S are set equal to the values from 0 - 255 in ascending order
s[0] = 0, s[1] = 1 ...
A tempory vector, t, is also created. 
If the length of the key K is 256 bytes, then k is transferred to T. 
Otherwise for a key of length keylen the first keylen elements of t are filled with K
Then K is repeated however many times is needed
'''
for b in key:
    k.append(b)
for i in range(255):
    s.append(i)
    t.append(k[i]) 
'''
Next, we use T to produce the initial permutation of S. 
This involves starting with S[0] and going through to S[255],
and for each s[i] swap it with another byte in S according to
a scheme dictated by T[i]
'''
# initial permutation 
j = 0
for i in range(255):
    j = (j+s[i]+t[i])%256
    s[i],s[j] = s[j],s[i]
#not that s is only being swapped, no other changes
'''
Stream generation:
Once the S vector is initialized, the input key is no longer used.
Stream generation involves cycling through all elements of s[i], and,
for each s[i] swapping s[i] with another byte in S according to a 
scheme dictated by the current configuration of s. After S[255] is
reached, the process continues starting over at s[0]
'''
#stream generation 
i,j = 0
cant_stop_wont_stop = True
while cant_stop_wont_stop:
    i = (i+1)%256
    j = (j+s[i])%256
    s[i],s[j] = s[j],s[i]
    tt = 
