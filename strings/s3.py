m = "This is an massage"
print(len(m))
for i,v in enumerate(m):
    print(f'{i} --> {v}')

    #slice
    print(m[5:7])# is
    print(m[8:10])
    print(m[11:18])

    s = 'digipodium'
    slice1 = s[0:4]
    slice2= s[1:4]
    slice8= s[-1:]
    slice3 = s[:-1]
    slice4 = s[4:]
    slice5 = s[4:len(s)]
    print(slice1)
    print(slice8)
    print(slice2)
    print(slice3)
    print(slice4)
    print(slice5)


    amt = '$3000'
    print(int(amt[1:]))

    rr = '1,143 ratings | 347 answer question ' 
    print("total number", rr[15:])
    print("no of string ",rr[:12])
    print(len(rr))
    for i in enumerate(rr):
        print(f'{i}')