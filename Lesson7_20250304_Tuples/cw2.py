import pgzrun
import random

HEIGHT = 800
WIDTH = 1200

astroide_no = 10
astroides = []
lines = []
current_index = 0

def creat_astroides():
    for i in range(astroide_no):
        astroid = Actor("saterites")
        astroid.x = random.randint(50,WIDTH-50)
        astroid.y = random.randint(50,HEIGHT-50)
        astroides.append(astroid)

def draw():
    screen.blit("background3",(0,0))
    number = 1
    for astroid in astroides:
        astroid.draw()
        screen.draw.text(str(number),(astroid.x-10,astroid.y-10),fontsize = 50, color="white")
        number += 1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

def update():
    pass

def on_mouse_down(pos):
    global lines,current_index
    if current_index < astroide_no:
        if astroides[current_index].collidepoint(pos):
            print(astroides[current_index])
            if current_index:
                print("Debug")
                lines.append((astroides[current_index-1].pos,astroides[current_index].pos))
                print(lines)
            current_index += 1
        else:
            lines = []
            current_index = 0

creat_astroides()
pgzrun.go()