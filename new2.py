from turtle import *
pencolor('green')
pensize(5)
speed('slowest')
 
side = 5
for i in range(side):
    fd(100)
    lt(360/side)
    pencolor('red')
    pensize(2)
    pencolor('blue')
    circle(side*10.5)

mainloop()