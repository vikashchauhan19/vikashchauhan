
import pgzrun

HEIGHT = 800
WIDTH = 800

p = Actor ('ironman',(200,200))

def draw():
    screen.fill('white')
    p.draw()

def update():
    if keyboard.left:
        p.x -= 5
        p.angle = 10
    elif keyboard.right:
        p.x += 5
        p.angle = -10
    elif keyboard.up:
        p.y -= 5
    elif keyboard.down:
        p.y += 5
    else:
        p.angle = 0


pgzrun.go()   
