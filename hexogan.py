
from turtle import *

outside = 6 
inside = 6 
pencolor('green')
fillcolor('blue')
begin_fill()
for i in range (outside):
    fd(100)
    for j in range(inside):
        fd(50)
        lt(360/inside)  
    lt(360/outside)
end_fill()
mainloop()