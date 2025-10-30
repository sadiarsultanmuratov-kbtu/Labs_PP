import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    
    rectengle=pygame.Surface( (100,100))
    rectengle.fill((15,26,36,5))
    screen.blit(rectengle,(10,10))
    
    pygame.display.flip()