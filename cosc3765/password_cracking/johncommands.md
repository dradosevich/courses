unshadow passwd shadow > ./unshadow
john --wordlist=abridged_rockyou.txt --format=RAW-MD5  unshadow
