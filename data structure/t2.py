x = 1,2,3,4,5,6,7,9,78,5,4,5
print(x)
print(type(x))

#assignment in python
a,b= 10,20 #2 value are store in 2 variable
print(a,b)
a = 10,20 # 2 values are packed in one variable
print(a , type(a))

#special case
x , *y = 1,2,3,4,5,6,7,8,9 # 1 value is store in x and rest y as a list
print(x,y)
print(type(x),type(y))