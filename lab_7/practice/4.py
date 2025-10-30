import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


speed=1
x=50
y=50

done=False

is_color=True

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            is_color=not is_color
            
    screen.fill((255,255,255))
    
    if is_color:
        color=(12,15,36)
    else:
        color=(48,36,96)
        
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:y=y+speed
    if pressed[pygame.K_UP]:y=y-speed
    if pressed[pygame.K_LEFT]:x=x-speed
    if pressed[pygame.K_RIGHT]:x=x+speed
    
    pygame.draw.rect(screen,color,pygame.Rect(x,y,50,50))
    
    pygame.display.flip()
    clock.tick(60)
        
        
    