import pygame
import os
pygame.init()

screen=pygame.display.set_mode((800,600))

mus=False
pygame.mixer.music.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_2\music\So Easy (To Fall In Love).mp3")
pygame.mixer.music.play(-1)
    

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            mus=not mus
            
    if mus:
        pygame.mixer.music.pause()
    else:
       pygame.mixer.music.unpause() 
    
    pygame.display.flip()