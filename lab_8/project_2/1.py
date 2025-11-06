import pygame  
import sys  
import copy  
import random  
import time  

pygame.init() 


WIDTH, HEIGHT = 500, 500
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()  


scale = 15  
score = 0  
level = 1  
SPEED = 10  


snake_colour = (0, 200, 0)
font_colour = (255, 255, 255)
defeat_colour = (255, 0, 0)


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
        self.x = WIDTH // 2 - scale
        self.y = HEIGHT // 2 - scale
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def show(self):
        for pos in self.history:
            pygame.draw.rect(display, snake_colour, (pos[0], pos[1], self.w, self.h))

    def check_eaten(self, food_x, food_y):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True
        return False

    def grow(self):
        self.length += 1
        self.history.append(copy.deepcopy(self.history[-1]))

    def death(self):
        # Проверка столкновения с телом
        for i in range(1, self.length):
            if self.history[0] == self.history[i]:
                return True
        return False

    def update(self):
        # обновляем позиции тела
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = (random.randint(100, 255), random.randint(50, 255), random.randint(50, 255))
        self.new_location([])

    def new_location(self, snake_body):
        while True:
            self.x = random.randrange(1, WIDTH // scale - 1) * scale
            self.y = random.randrange(1, HEIGHT // scale - 1) * scale
            # Проверяем, чтобы еда не появлялась на теле змейки
            if [self.x, self.y] not in snake_body:
                break

    def show(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, scale, scale))


def show_info(score, level):
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {score}", True, font_colour)
    level_text = font.render(f"Level: {level}", True, font_colour)
    display.blit(score_text, (10, 10))
    display.blit(level_text, (120, 10))

# игровой цикл
def gameLoop():
    global score, level, SPEED

    snake = Snake(WIDTH // 2, HEIGHT // 2)
    food = Food()

    foods_eaten = 0  #  для перехода уровня

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                # Управление
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    elif event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = 1
                elif snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    elif event.key == pygame.K_RIGHT:
                        snake.x_dir = 1
                        snake.y_dir = 0

        #Обновление
        snake.update()

        # Проверка поедания еды
        if snake.check_eaten(food.x, food.y):
            snake.grow()
            score += random.randint(1, 5)
            foods_eaten += 1
            food.new_location(snake.history)

            # Повышение уровня
            if foods_eaten % 4 == 0:
                level += 1
                SPEED += 2
                food.new_location(snake.history)

        # Проверка столкновения со стенами
        head_x, head_y = snake.history[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or snake.death():
            font = pygame.font.SysFont(None, 80)
            text = font.render("Game Over!", True, defeat_colour)
            display.blit(text, (60, 200))
            pygame.display.update()
            time.sleep(3)
            # Сброс
            snake.reset()
            food.new_location([])
            score = 0
            level = 1
            SPEED = 10
            foods_eaten = 0

        # Отрисовка
        display.fill((0, 0, 0))
        snake.show()
        food.show()
        show_info(score, level)

        pygame.display.update()
        clock.tick(SPEED)


gameLoop()
