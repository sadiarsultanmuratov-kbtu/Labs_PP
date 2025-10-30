import pygame
import os
pygame.init()

screen=pygame.display.set_mode((800,600))

photo=pygame.transform.scale(pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_1\images\clock.png"),(400,300))


done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    
    screen.blit(photo,(200,100))
    
    pygame.display.flip()