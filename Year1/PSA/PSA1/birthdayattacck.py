import os
import hashlib
import binascii
collisions = 0
hash = {}
strn_table = {}
n = 5
while n:
    strn = binascii.b2a_hex(os.urandom (16))
    hash_strn = hashlib.md5(strn).hexdigest()
    sliced_hash = hash_strn[:10]
    if sliced_hash in hash:
        collisions += 1
        x = "---------------------------------------------------------------------------------------------------"
        z = "Collision number:" + str(collisions) + " " * 18 + "Collision: " + str(sliced_hash)
        a = "Hashes: " + " " * 10 + str(hash [sliced_hash]) + " " + str (hash_strn)
        b = "Texts: " + " " * 10 + strn.decode() + " " + strn_table [sliced_hash].decode ()
        print(x + "\n" + z + "\n" + a + "\n" + b + "\n")
        n -= 1
    else:
        hash[sliced_hash] = hash_strn
        strn_table[sliced_hash] = strn







