import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

is_color = True
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            done = True
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_color = not is_color
             
    screen.fill((0, 0, 0))
    
    if is_color:
        color = (48, 26, 26)   
    else:
        color = (20, 25, 55)    
    
    pygame.draw.rect(screen, color, pygame.Rect(50, 50, 150, 150))
    
    pygame.display.flip()
    
pygame.quit()

            