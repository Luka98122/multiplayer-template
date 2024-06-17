import pygame
import json
pygame.init()

SIZE = 16

BLOCKS = 50

window = pygame.display.set_mode((BLOCKS*SIZE,BLOCKS*SIZE))

selected = []
for i in range(50):
    selected.append([])
    for j in range(50):
        selected[-1].append(0)

overlay = pygame.image.load("Pictures\\map-roofs.png")
overlay = pygame.transform.scale(overlay,(800,800))

while True:
    window.blit(overlay,(0,0))
    
    for i in range(BLOCKS):
        for j in range(BLOCKS):
            if selected[i][j]:
                pygame.draw.rect(window,(255,0,0,220),pygame.Rect(j*SIZE,i*SIZE,SIZE,SIZE))
    
    events = pygame.event.get()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
    
    pressed = pygame.mouse.get_pressed()
    x,y = pygame.mouse.get_pos()
    if pressed[0]:
        x//=SIZE
        y//=SIZE
        
        selected[y][x] = 1
    if pressed[2]:
        x//=SIZE
        y//=SIZE
        
        selected[y][x] = 0
    
    
    pygame.display.update()

f = open("mapstate.json","w")
f.write(json.dumps(selected))
f.close()