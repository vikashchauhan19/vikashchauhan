# cleean list of all dublicate values

x = [ 1,1,2,2,3,3,4,4,5,5,6,6,7,8,]
print(x,'dublicated vAlues')
x = list(set(x)) # remove dublicates
print(x, 'clean list')


#data-structutre conversion

x = [1,2,3,4,5,6]
print(x,'list')


x = tuple(x) #convert list to tuple 
print(x,'tuple')

x = set(x) # convert Tuple to set 
print(x, 'set')

x = list(x) # convert set to list
print(x,'list')