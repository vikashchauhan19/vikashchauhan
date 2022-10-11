# wap to take 10 float number from user and store them in a lsit 

x = []

for i in range(10):
    data = input ('Enter a float value:')
    if '.' in data and data .count('.') == 1:
        p1,p2 =data.split('.')
        if p1.isnumeric() and p2.isnumeric():
            x.append(float(data))
    if data.isnumeric():
        x.append(float(data))
print(x)        
