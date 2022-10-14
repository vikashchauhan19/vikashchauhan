my_tuple = (1,2,3,4,5,6,7,8,9,10)
print(my_tuple)
print(type(my_tuple))
print(f'size => {len(my_tuple)}')

#indexing
print(f'index 0 =>{my_tuple[0]}')
print(f'index 1 =>{my_tuple[1]}')
print(f'last index =>{my_tuple[-1]}')

#slicing
print(f'First 3=> {my_tuple[:3]}')
print(f'Last 3 => {my_tuple[-3:]}')

#tuple is imutable , given error when trying to change
#my_tuple[0] = 100
