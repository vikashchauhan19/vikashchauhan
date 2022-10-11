# wap to find the sum , mean , max and min in a list of numbers
import math , statistics
x = [12,22,3,4,5,4,5,6,2,1,5,1,2,4,494,45,4,5,10]

total = sum(x)
mean = sum(x)/len(x)
x_max = max(x)
x_min = min(x)

print(f'sum: {total}, Mean : {mean},Max : {x_max}, Min :{x_min} ')

median