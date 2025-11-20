#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
TOTAL_COINS = 0
LAST_SPEED_INCREASE = 0  # Track when we last increased speed

# Coin types with different weight and size
COIN_TYPES = [
    {"weight": 1, "size": 20, "speed": 3, "spawn_rate": 0.6},
    {"weight": 2, "size": 30, "speed": 4, "spawn_rate": 0.3},
    {"weight": 3, "size": 35, "speed": 5, "spawn_rate": 0.1}
]
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_8\project_1\images\AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")
 
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_8\project_1\images\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Randomly select coin type based on spawn rates
        rand_val = random.random()  # генерируем случайное чило от 0 до 1
        cumulative_rate = 0
        for coin_type in COIN_TYPES:
            cumulative_rate += coin_type["spawn_rate"]
            if rand_val <= cumulative_rate:
                self.type = coin_type
                break
        
        # Load and scale the coin image to the appropriate size
        original_image = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_8\project_1\images\coin.png")
        self.image = pygame.transform.scale(original_image, (self.type["size"], self.type["size"]))
        
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(-100, 0))
        self.speed = self.type["speed"]
        self.weight = self.type["weight"]
 
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()
    
    def respawn(self):
        # Respawn coin with new random type
        rand_val = random.random()
        cumulative_rate = 0
        for coin_type in COIN_TYPES:
            cumulative_rate += coin_type["spawn_rate"]
            if rand_val <= cumulative_rate:
                self.type = coin_type
                break
        
        # Update coin appearance with new size
        original_image = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_8\project_1\images\coin.png")
        self.image = pygame.transform.scale(original_image, (self.type["size"], self.type["size"]))
        
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(-100, 0))
        self.speed = self.type["speed"]
        self.weight = self.type["weight"]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\Админ\Documents\PP2\LABS\lab_8\project_1\images\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                   
                              
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()  


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()  # Group for coins
coins.add(C1)

# Keep all_sprites as a sprite Group
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 



while True:
       
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    
    # показать очки игрока
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    
    # показать сколько монет у игрока
    coins_text = font_small.render(f"Coins: {TOTAL_COINS}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))
    
    # показать в экран скорость врага
    speed_text = font_small.render(f"Speed: {SPEED}", True, BLACK)
    DISPLAYSURF.blit(speed_text, (SCREEN_WIDTH - 100, 40))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # проверяем сколько монет собралось и зависимости этого будет ускоряться враги на 1 скорость больше чем тогда
    coins_collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coins_collected:
        TOTAL_COINS += coin.weight
        
        # если мы собрали 10 монет враги ускоряться
        if TOTAL_COINS >= (LAST_SPEED_INCREASE + 1) * 10:
            SPEED += 1  
            LAST_SPEED_INCREASE = TOTAL_COINS // 10
            
        
        # показываем на экран столкновение с монетом но выводим сколько очков она дала
        value_text = font_small.render(f"+{coin.weight}", True, BLACK)
        DISPLAYSURF.blit(value_text, (coin.rect.x, coin.rect.y))
        pygame.display.update()
        
        
        # создаем новую монету 
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    #столкновение с врагом игрока 
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\Админ\Documents\PP2\LABS\lab_8\project_1\images\crash.wav").play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        final_score = font_small.render(f"Final Score: {SCORE}", True, WHITE)
        final_coins = font_small.render(f"Total Coins: {TOTAL_COINS}", True, WHITE)
        final_speed = font_small.render(f"Final Speed: {SPEED}", True, WHITE)
        DISPLAYSURF.blit(final_score, (120, 350))
        DISPLAYSURF.blit(final_coins, (120, 380))
        DISPLAYSURF.blit(final_speed, (120, 410))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)