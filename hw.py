import pgzrun
import random

WIDTH = 750
HEIGHT = 400
TITLE = "Game Secreen"

score = 0

player1 = Actor("player")
player2 = Actor("aim")
enemy1 = Actor("zombie1")
enemy2 = Actor("zombie2")

isgameover = False

player1.pos = (325,350)
player2.pos = (325,200)
enemy1.pos = (100,200)
enemy2.pos = (300,200)

def Zombie1Move():
    enemy1.x = random.randint(100,WIDTH-200)
    enemy1.y = random.randint(100,HEIGHT-100)

def Zombie2Move():
    enemy2.x = random.randint(100,WIDTH-200)
    enemy2.y = random.randint(100,HEIGHT-100)

def on_mouse_down(pos):
    global score
    x,y=pos
    player2.pos = (x,y)
    player1.pos = (x,HEIGHT-100)

    if enemy1.collidepoint(pos):
        score += 1
        Zombie1Move()
    elif enemy2.collidepoint(pos):
        score += 1
        Zombie2Move()
    else:
        score -= 1

def gameover():
    global isgameover
    isgameover = True

def draw():
    screen.clear()
    if not isgameover:
        screen.blit("bg1",(-100,-100))
        player1.draw()
        player2.draw()
        enemy1.draw()
        enemy2.draw()
        screen.draw.text("Score : " + str(score),(600,50),fontsize=25,color="White")
    else:
        screen.blit("bg2",(-50,-100))

clock.schedule(gameover,30.0)

pgzrun.go()