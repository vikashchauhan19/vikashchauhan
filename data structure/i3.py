x = [1,2,3,4,5,6,8,9,7,9,5,5,1,21,221,1]

print (x.count(1))
print(x.count(9))
print(x.count(21))# count func use to find the number of same element in list
print(x.count(99))

print(x.index(1))
print(x.index(5))
#print(x.index(65)) # value error show 

z = x
y  = x.copy()
print(x is y)# flase because value are same but address are diff
print(x is z)
z.append(10)
y.append(20)
print(x)
print(y)
print(z)