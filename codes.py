import pgzrun
import pygame
import random
import time
WIDTH = 600
HEIGHT = 600
count = 0
health = 300

TITLE = "Soguk kalpli kralice"
FPS = 30
# Nesneler
background=Actor('background_castel')
char=Actor('main_char',(150,380))
enemy=Actor('queen_l1',(450,360))
enemy_l2=Actor('queen_l2')
ice=Actor('ice',(150,100))
start_button=Actor('start_button',(300,300))
ices= []
#leve
ice_speed_l1= 1
ice_speed_l2= 3
game_over=Actor('you_lose')
mode="start_menu"
restart_button=Actor('restart_button')

    
#kontroller
def on_key_down(key):
    if keyboard.left:
        char.x -= 35
        char.image='main_char_left' 
    if keyboard.right:
        char.x += 35
        char.image='main_char_right'
    char.x = max(0, min(WIDTH, char.x))


def update():
    global health, mode
    if mode != 'game':
        return
    

    if random.randint(1,40) == 1:
        ice =Actor('ice')
        ice.x = random.randint(0, WIDTH)
        ice.y = 0
        ices.append(ice)


    for ice in ices[:]:
        ice.y += 3

        if ice.y > HEIGHT:
            ices.remove(ice)
        
        if ice.colliderect(char):
            health -= 2
            ices.remove(ice)
            
            if health <= 0:
                mode = 'game_over'
            

               

def draw():
    screen.clear()

    if mode == 'game':
        background.draw()
        char.draw()
        enemy.draw()
        screen.draw.text('health ='+ str(health), (20,20), fontsize=24, color='black')
        for ice in ices:
            ice.draw()
        screen.draw.text('Sag ve Sol tuslari ile hareket et',(80,60),fontsize=24,color='black')
    elif mode == 'start_menu':
        background.draw()
        start_button.draw()
    elif mode == 'game_over':
        game_over.draw()
        restart_button.draw()


def on_mouse_down(pos):
    global mode, health, ices
    if start_button.collidepoint(pos):
        mode='game'
        ices = []
        health = 50
        sounds.game_music.play(loops=-1)
    
    elif mode == 'game_over' and restart_button.collidepoint(pos):
        mode = 'game'
        health = 50
        ices = []
        


    



        
        

    


pgzrun.go()