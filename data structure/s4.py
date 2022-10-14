a = {'Ram','Shyam','Hari','Gita','Sita'}
b = {'Alex', 'Mark','Eliza','Benny','Sunny'}
c ={'Ram','Alex','Gita','teanya','Sergei'}

#union
ab = a|b 
print("union =>", ab)
 #or
ab = a .union(b)
print("union=>",ab)


#intersection
ac = a & c # a.intersection (c) also works
print('intersection=>', ac) # nothing is common in this set

abi = a & b 
print('intersection=>', abi) # nothing is common in this set

# difference 
ac = a-c # a.difference (c) also Works
print('differrence=>', ac)

ca = c-a 
print('difference=>',ca)

#symmetriuc difference
ac = a^c #a .symmtric_fiffernce (c) also Works
print('symmetric differnce =>', ac)