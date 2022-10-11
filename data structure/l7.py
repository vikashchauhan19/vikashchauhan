from distutils.command.build_scripts import first_line_re


names = ['Raymond','Cynthia','David','Jennifer','Clayton','Mike']
first_letters = []
last_letters = []
for name in names:
    first_letters.append(name[0])
    last_letters.append(name[-1])

print(names)
print(first_letters) 
print(last_letters)   

# task
# creat a list of short name from a list of names

names = ['Project Manager','Central Processing unit','Graphics Proceesing unit','Random Access Memory','input Output']

short_names =[]
for name in names:
    short_names.append(name[0:8])

print(names)
print(short_names)    


