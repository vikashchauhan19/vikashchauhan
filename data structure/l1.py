from xml.dom.minidom import Element


Elements = ["hydrogrn","helium","lithium"]

print(Elements)
print('individual element:')
print(Elements[2])
print(Elements[1])
print(Elements[0])

# changing a list element (mutability)
Elements[1]= "Carbon"
Elements.insert(1,'chemical')
Elements.insert(100,'nitrogen')
nobal_metals = ['gold','silver','platinum']
Elements.append(nobal_metals)
print(Elements)
Elements.extend(nobal_metals)  # add multiple elements to the end of the list
print(Elements)



print(Elements)





list1 =['rahul','deepak','abhishek','shivam']
list2 =[1,2,3,4,5,6,9,7,8]
list3 =['rahul',90,111,214,22, "b",False,5.265]
list4 = [[1,2,3,],[3,4,5,6],[2,1]]
msg =[list1,list2,list3,list4]
for sublist in msg:
    print(sublist)


# getting a list slice
l= [10,20,30,40,50,60,7,0,80,90]
slice1 = l[3:-2]
print(slice1)




# Append Fiunction

fruits =[]
fruits.append('apple')
fruits.append('mango')
fruits.append('banana')
fruits.append('bluebary')
fruits.append('grapes')
fruits.append('langur')
fruits.append('pagal')
print(fruits)


#insert func
fruits=['apple','banana','mango']
dry_fruits = ['Almond','cashew','walnut']
fruits.extend(dry_fruits)
fruits.insert(1,'cherry')
print(fruits)