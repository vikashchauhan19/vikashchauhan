from turtle import *
bgcolor ('black')
speed('fastest')

colors=['red','green','purple', 'blue','yellow','orange']
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    fd(x)
    lt(90)
mainloop()