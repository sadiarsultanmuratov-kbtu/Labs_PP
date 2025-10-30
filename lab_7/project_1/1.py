import pygame 
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))


leftarm= pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_1\images\leftarm.png")
rightarm = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_1\images\rightarm.png")
clock =pygame.transform.scale(pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_1\images\clock.png"), (800, 600))


done=False
while not done:
    for event in pygame.event.get():  ## принимает все события ,нажатия клавиш, движение мыши и закрытие окна
        if event.type == pygame.QUIT:
            done = True
    
    screen.blit(clock, (0,0))
    
    now_time = time.localtime()
    minut = now_time.tm_min
    secund = now_time.tm_sec   
    
    minut_angle = minut * 6
    secund_angle = secund * 6  
    
    
    moverightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minut_angle)
    rightarmrect = moverightarm.get_rect(center=(800 // 2, 600 // 2 + 15)) 
    ## get_rict() Создает прямоугольник с такими же размерами как изображения
    screen.blit(moverightarm, rightarmrect)
    
    moveleftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -secund_angle)
    leftarmrect = moveleftarm.get_rect(center=(800 // 2, 600 // 2 + 13)) 
    screen.blit(moveleftarm, leftarmrect)
    
    pygame.display.flip()   ## Обновляет весь экран, Показывает на экране всё, что я нарисовал
pygame.quit()