import hash

a = '/getMedalTally/Rome'
a_hash = hash.encode(a)
b = '/getMedalTally/Gual'
b_hash = hash.encode(b)
c = '/getScore/Stone Throwing'
c_hash= hash.encode(c)
d = '/getScore/Stone Curling'
d_hash= hash.encode(d)

hash_dic = {}
for i in range(0,3):
    hash_dic[a_hash] = a
    hash_dic[b_hash] = b
    hash_dic[b_hash] = c
    hash_dic[b_hash] = d
    
print hash_dic[a_hash]




    
    
    