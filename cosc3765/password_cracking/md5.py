#Danny Radosevich
# md5 password "cracker"

import hashlib

pass_file = open("pass").read()
pass_file = pass_file.replace("\n","")
pass_list = open("abridged_rockyou.txt").read()
pass_list = pass_list.split("\n")
print(pass_file)
for p in pass_list:
    p_hash = hashlib.md5(p.encode()).hexdigest()
    if p_hash == pass_file:
        print("password found: ",p)
