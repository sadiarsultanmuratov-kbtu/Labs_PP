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
        head_rect = pygame.Rect(self.history[0][0], self.history[0][1], self.w, self.h)
        food_rect = pygame.Rect(food_x, food_y, scale, scale)
        return head_rect.colliderect(food_rect)

    def grow(self, amount=1):
        for _ in range(amount):
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


################ создаем класс еды с разными очками и ставим таймер на них #########################################
class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.weight = 1  # Вес по умолчанию
        self.color = "red"  # Цвет по умолчанию
        self.lifetime = 0  # Время жизни в кадрах
        self.max_lifetime = 0  # Максимальное время жизни
        self.new_location([])

    def new_location(self, snake_body):
        while True:
            self.x = random.randrange(0, (WIDTH // scale)) * scale
            self.y = random.randrange(0, (HEIGHT // scale)) * scale
            
            # случайная вес еды
            self.weight = random.choice([1, 2, 3])
            
            # Устанавливаем цвет в зависимости от веса
            if self.weight == 1:
                self.color = "red"
                self.max_lifetime = 100  # 30 секунд при 10 FPS
            elif self.weight == 2:
                self.color = "orange"
                self.max_lifetime = 80  # 20 секунд при 10 FPS
            else:
                self.color = "gold"
                self.max_lifetime = 50  # 10 секунд при 10 FPS
            
            # Сбрасываем таймер
            self.lifetime = self.max_lifetime
            
            # Проверяем, чтобы еда не появилась на змейке
            if [self.x, self.y] not in snake_body:
                break

    def update(self):
        # Уменьшаем время жизни
        self.lifetime -= 1
        return self.lifetime <= 0  # Возвращает True, если время истекло

    def show(self):
        # Вычисляем прозрачность в зависимости от оставшегося времени
        alpha = int(255 * (self.lifetime / self.max_lifetime))
        
        # Создаем поверхность с прозрачностью
        food_surface = pygame.Surface((scale, scale), pygame.SRCALPHA)
        
        # Рисуем еду с учетом прозрачности
        if self.weight == 1:
            pygame.draw.rect(food_surface, (255, 0, 0, alpha), (0, 0, scale, scale))
        elif self.weight == 2:
            pygame.draw.rect(food_surface, (255, 165, 0, alpha), (0, 0, scale, scale))
        else:
            pygame.draw.rect(food_surface, (255, 215, 0, alpha), (0, 0, scale, scale))
        
        # Отображаем еду
        display.blit(food_surface, (self.x, self.y))
        
        # Отображаем вес еды и оставшееся время
        font = pygame.font.SysFont(None, 15)
        text = font.render(str(self.weight), True, "WHITE")
        display.blit(text, (self.x + scale//2 - 5, self.y + scale//2 - 5))
        
        # Рисуем полоска под едой играет роль показаетль таймера
        time_width = scale * (self.lifetime / self.max_lifetime)
        pygame.draw.rect(display, "WHITE", (self.x, self.y + scale, time_width, 2))


# ИНТЕРФЕЙС
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, "WHITE")
    display.blit(text, (10, 10))

def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, "WHITE")
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

        display.fill("black")

        snake.update()
        
        # Обновляем еду и проверяем, не истекло ли время
        if food.update():
            food.new_location(snake.history)
        
        snake.show()
        food.show()
        show_score()
        show_level()

        # Проверка съедения еды
        if snake.check_eaten(food.x, food.y):
            # Увеличиваем счет на вес еды
            score += food.weight
            # Увеличиваем длину змейки на вес еды
            snake.grow(food.weight)
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
        clock.tick(SPEED)


gameLoop()