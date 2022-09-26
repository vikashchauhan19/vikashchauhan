from turtle import *
speed('fastest')
pencolor('green')
pensize(1)

i = 1
while True:
    fd(10+i)

    for j in range(6):
        fd(100)
        lt(360/6)


    lt(90)
    i+=2
    write(i)

    if i > 300:
        break
mainloop()