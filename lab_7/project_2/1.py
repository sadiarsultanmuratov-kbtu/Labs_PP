import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800,800))


music_folder = r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_2\music"
allmusic = os.listdir(music_folder)

playlist = []
for song in allmusic:
    playlist.append(os.path.join(music_folder, song))


play = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_2\images\play_but.png")
paus= pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_2\images\pausa_but.png")
next = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_2\images\next_but.png")
prev = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_7\project_2\images\back_but.png")

index = 0
pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(0)

play_mus = True 

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                if play_mus:
                    play_mus = False
                    pygame.mixer.music.pause()
                else:
                    play_mus = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT: 
                index += 1 
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT: 
                index -=1
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    
    screen.fill((255,255,255))
    
    font= pygame.font.Font(None, 30)
    text= font.render(os.path.basename(playlist[index]), True, (255, 255, 255),(255, 0, 150))
    
    
    screen.blit(text, (310, 400))
    play = pygame.transform.scale(play, (75, 75))
    paus = pygame.transform.scale(paus, (75, 75))
    
    
    if play_mus:
        screen.blit(paus, (370, 590))
    else: 
        screen.blit(play, (370, 590))
        
        
    next = pygame.transform.scale(next, (75, 75))
    screen.blit(next, (450, 590))
    
    
    prev = pygame.transform.scale(prev, (75, 75))
    screen.blit(prev, (280, 590))

    pygame.display.flip()