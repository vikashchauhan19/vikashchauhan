from turtle import *

pencolor('red')
pensize(3)
speed('slowest')
side=4
for i in range(side):
    fd(100)
    lt(90)
    pencolor('light blue')
    dot( side*4)
    circle(side*12.5)
    


mainloop()