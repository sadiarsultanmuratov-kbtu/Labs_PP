import pygame
pygame.init()


screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

x=25
y=25

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and x<765:
        x += 20
    if pressed[pygame.K_LEFT] and x>25: 
        x -= 20
    if pressed[pygame.K_UP]and y>25: 
        y -= 20
    if pressed[pygame.K_DOWN] and y<565: 
        y += 20


    screen.fill(("white"))
    
    pygame.draw.circle(screen, ("red"), (x, y), 25)
    
    pygame.display.flip()
    clock.tick(60)