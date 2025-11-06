import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 5
    mode = 'blue'  
    drawing = False
    last_pos = None
    drow = []       # рисованный линии
    shapes = []     # все прямоугольник
    circles = []    #все круги
    rect_start = None  #начало риктенгла
    circle_start = None  # начала серкл 
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # инструменты доступ  клавиши 
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_t:
                    mode = 'rectangle'
                elif event.key == pygame.K_y:
                    mode = 'circle'
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mode == 'rectangle':
                        rect_start = event.pos
                    elif mode == 'circle':
                        circle_start = event.pos
                    else:
                        drawing = True
                        last_pos = event.pos
                
                elif event.button == 4:  #верх
                    radius = min(200, radius + 1)
                elif event.button == 5:  #вниз
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if mode == 'rectangle' and rect_start is not None:
                        rect_end = event.pos
                        shapes.append((rect_start, rect_end))
                        rect_start = None
                    elif mode == 'circle' and circle_start is not None:
                        circle_end = event.pos
                        circles.append((circle_start, circle_end))
                        circle_start = None
                    drawing = False
                    last_pos = None

            if event.type == pygame.MOUSEMOTION and drawing and mode not in ('rectangle', 'circle'):
                pos = event.pos
                if last_pos is not None:
                    drow.append((last_pos, pos, radius, mode))
                last_pos = pos

        screen.fill((0, 0, 0))
        
        # линии
        for start, end, width, color_mode in drow:
            drawLineBetween(screen, start, end, width, color_mode)
        
        # квадрат
        for start, end in shapes:
            drawRectangle(screen, start, end)
        
        # серкл
        for start, end in circles:
            drawCircle(screen, start, end)
        
        # рисунок прямоугольника
        if rect_start is not None and mode == 'rectangle':
            mouse_pos = pygame.mouse.get_pos()
            drawRectangle(screen, rect_start, mouse_pos, preview=True)
        
        # рисунок круга
        if circle_start is not None and mode == 'circle':
            mouse_pos = pygame.mouse.get_pos()
            drawCircle(screen, circle_start, mouse_pos, preview=True)
        
        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, start, end, width, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    elif color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        color = (255, 255, 255)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] * (1 - progress) + end[0] * progress)
        y = int(start[1] * (1 - progress) + end[1] * progress)
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, start, end, preview=False):
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2),
                       abs(x2 - x1), abs(y2 - y1))
    if preview:
        pygame.draw.rect(screen, color, rect, 1)
    else:
        pygame.draw.rect(screen, color, rect, 2)

def drawCircle(screen, start, end, preview=False):
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end
    radius = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    if preview:
        pygame.draw.circle(screen, color, start, radius, 1)
    else:
        pygame.draw.circle(screen, color, start, radius, 2)

main()
