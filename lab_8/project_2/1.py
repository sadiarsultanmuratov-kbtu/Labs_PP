import pygame
import sys
import copy
import random
import time

pygame.init()

# параметры 
scale = 15
score = 0
level = 0
SPEED = 10

WIDTH, HEIGHT = 500, 500
display = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


# класс змейка
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = scale
        self.h = scale
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def reset(self):
        self.__init__(WIDTH / 2, HEIGHT / 2)

    def show(self):
        for i in range(self.length):
            color = "green" if i == 0 else "green"
            pygame.draw.rect(display, color, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self, food_x, food_y):
        #проверяем столкновение по прямоугольникам
        head_rect = pygame.Rect(self.history[0][0], self.history[0][1], self.w, self.h)
        food_rect = pygame.Rect(food_x, food_y, scale, scale)
        return head_rect.colliderect(food_rect)

    def grow(self):
        self.length += 1
        self.history.append(self.history[-1][:])

    def death(self):
        for i in range(1, self.length):
            if self.history[0] == self.history[i]:
                return True
        return False

    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale


#КЛАСС ЕДЫ
class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.new_location([])

    def new_location(self, snake_body):
        while True:
            self.x = random.randrange(0, (WIDTH // scale)) * scale
            self.y = random.randrange(0, (HEIGHT // scale)) * scale
            # Проверяем, чтобы еда не появилась на змейке
            if [self.x, self.y] not in snake_body:
                break

    def show(self):
        pygame.draw.rect(display, "RED", (self.x, self.y, scale, scale))


# ИНТЕРФЕЙС
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, "WHITE")
    display.blit(text, (10, 10))

def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True," WHITE")
    display.blit(text, (100, 10))

def game_over_screen(snake):
    global score, level, SPEED
    font = pygame.font.SysFont(None, 80)
    text = font.render("Game Over!", True, 'red')
    display.blit(text, (70, 200))
    pygame.display.update()
    time.sleep(2)
    score = 0
    level = 0
    SPEED = 10
    snake.reset()


#ОСНОВНОЙ ЦИКЛ 
def gameLoop():
    global score, level, SPEED

    snake = Snake(WIDTH / 2, HEIGHT / 2)
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir, snake.y_dir = 0, -1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir, snake.y_dir = 0, 1
                if snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir, snake.y_dir = -1, 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir, snake.y_dir = 1, 0

        display.fill("BLACK")

        snake.update()
        
        snake.show()
        food.show()
        show_score()
        show_level()

        # Проверка съедения еды
        if snake.check_eaten(food.x, food.y):
            score += 1
            snake.grow()
            food.new_location(snake.history)

            # Повышение уровня каждые 3 очка
            if score % 3 == 0:
                level += 1
                SPEED += 1

        # Проверка выхода за границы
        head_x, head_y = snake.history[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over_screen(snake)


        pygame.display.update()
        clock.tick(10)


gameLoop()
