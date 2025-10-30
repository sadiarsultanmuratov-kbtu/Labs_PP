import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill((255,58,35))       
    pygame.draw.rect(screen,(255,96,68),pygame.Rect(50,50,200,300))    
    
    pygame.display.flip()


