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
    drow = []       # рисованные линии
    shapes = []     # все прямоугольники
    circles = []    # все круги
    squares = []    # все квадраты
    right_triangles = []  # все прямоугольные треугольники
    equilateral_triangles = []  # все равносторонние треугольники
    rhombuses = []  # все ромбы
    
    rect_start = None  # начало прямоугольника
    circle_start = None  # начало круга
    square_start = None  # начало квадрата
    right_triangle_start = None  # начало прямоугольного треугольника
    equilateral_triangle_start = None  # начало равностороннего треугольника
    rhombus_start = None  # начало ромба
    
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
                
                # инструменты доступ по клавишам 
                if event.key == pygame.K_r:     # красный карандаш
                    mode = 'red'
                elif event.key == pygame.K_g:   # зеленый
                    mode = 'green'
                elif event.key == pygame.K_b:   # синий
                    mode = 'blue'
                elif event.key == pygame.K_e:   # черный цвет как ластик
                    mode = 'eraser'
                elif event.key == pygame.K_t:  #  прямоуголник
                    mode = 'rectangle'
                elif event.key == pygame.K_y:  #круг
                    mode = 'circle'
                elif event.key == pygame.K_s:  # квадрат
                    mode = 'square'
                elif event.key == pygame.K_u:  #прямоугольный треугольник
                    mode = 'right_triangle'
                elif event.key == pygame.K_i:  # равносторонний треугольник
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_o:  # ромб
                    mode = 'rhombus'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mode == 'rectangle':
                        rect_start = event.pos
                    elif mode == 'circle':
                        circle_start = event.pos
                    elif mode == 'square':
                        square_start = event.pos
                    elif mode == 'right_triangle':
                        right_triangle_start = event.pos
                    elif mode == 'equilateral_triangle':
                        equilateral_triangle_start = event.pos
                    elif mode == 'rhombus':
                        rhombus_start = event.pos
                    else:
                        drawing = True
                        last_pos = event.pos
                
                elif event.button == 4:  # верх
                    radius = min(200, radius + 1)
                elif event.button == 5:  # вниз
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
                    elif mode == 'square' and square_start is not None:
                        square_end = event.pos
                        squares.append((square_start, square_end))
                        square_start = None
                    elif mode == 'right_triangle' and right_triangle_start is not None:
                        right_triangle_end = event.pos
                        right_triangles.append((right_triangle_start, right_triangle_end))
                        right_triangle_start = None
                    elif mode == 'equilateral_triangle' and equilateral_triangle_start is not None:
                        equilateral_triangle_end = event.pos
                        equilateral_triangles.append((equilateral_triangle_start, equilateral_triangle_end))
                        equilateral_triangle_start = None
                    elif mode == 'rhombus' and rhombus_start is not None:
                        rhombus_end = event.pos
                        rhombuses.append((rhombus_start, rhombus_end))
                        rhombus_start = None
                    drawing = False
                    last_pos = None

            if event.type == pygame.MOUSEMOTION and drawing and mode not in ('rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'):
                pos = event.pos
                if last_pos is not None:
                    drow.append((last_pos, pos, radius, mode))
                last_pos = pos

        screen.fill((0, 0, 0))
        
        # линии
        for start, end, width, color_mode in drow:
            drawLineBetween(screen, start, end, width, color_mode)
        
        # прямоугольники
        for start, end in shapes:
            drawRectangle(screen, start, end)
        
        # круги
        for start, end in circles:
            drawCircle(screen, start, end)
        
        # квадраты
        for start, end in squares:
            drawSquare(screen, start, end)
        
        # прямоугольные треугольники
        for start, end in right_triangles:
            drawRightTriangle(screen, start, end)
        
        # равносторонние треугольники
        for start, end in equilateral_triangles:
            drawEquilateralTriangle(screen, start, end)
        
        # ромбы
        for start, end in rhombuses:
            drawRhombus(screen, start, end)
        
        # предпросмотр прямоугольника
        if rect_start is not None and mode == 'rectangle':
            mouse_pos = pygame.mouse.get_pos()
            drawRectangle(screen, rect_start, mouse_pos, preview=True)
        
        # предпросмотр круга
        if circle_start is not None and mode == 'circle':
            mouse_pos = pygame.mouse.get_pos()
            drawCircle(screen, circle_start, mouse_pos, preview=True)
        
        # предпросмотр квадрата
        if square_start is not None and mode == 'square':
            mouse_pos = pygame.mouse.get_pos()
            drawSquare(screen, square_start, mouse_pos, preview=True)
        
        # предпросмотр прямоугольного треугольника
        if right_triangle_start is not None and mode == 'right_triangle':
            mouse_pos = pygame.mouse.get_pos()
            drawRightTriangle(screen, right_triangle_start, mouse_pos, preview=True)
        
        # предпросмотр равностороннего треугольника
        if equilateral_triangle_start is not None and mode == 'equilateral_triangle':
            mouse_pos = pygame.mouse.get_pos()
            drawEquilateralTriangle(screen, equilateral_triangle_start, mouse_pos, preview=True)
        
        # предпросмотр ромба
        if rhombus_start is not None and mode == 'rhombus':
            mouse_pos = pygame.mouse.get_pos()
            drawRhombus(screen, rhombus_start, mouse_pos, preview=True)
        
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

def drawSquare(screen, start, end, preview=False):
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end
    
    # Вычисляем сторону квадрата как минимальную из разностей по x и y
    side = min(abs(x2 - x1), abs(y2 - y1))
    
    # Сохраняем направление рисования
    if x2 < x1:
        x1 = x1 - side
    if y2 < y1:
        y1 = y1 - side
        
    rect = pygame.Rect(x1, y1, side, side)
    if preview:
        pygame.draw.rect(screen, color, rect, 1)
    else:
        pygame.draw.rect(screen, color, rect, 2)

def drawRightTriangle(screen, start, end, preview=False):
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end
    
    # Вершины прямоугольного треугольника
    points = [(x1, y1), (x2, y2), (x1, y2)]
    
    if preview:
        pygame.draw.polygon(screen, color, points, 1)
    else:
        pygame.draw.polygon(screen, color, points, 2)

def drawEquilateralTriangle(screen, start, end, preview=False):
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end
    
    # Вычисляем длину стороны
    side_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Вычисляем высоту равностороннего треугольника
    height = (math.sqrt(3) / 2) * side_length
    
    # Вычисляем третью вершину
    # Вектор направления от начальной точки к конечной
    dx = x2 - x1
    dy = y2 - y1
    
    # Нормализуем вектор
    length = math.sqrt(dx*dx + dy*dy)
    if length > 0:
        dx = dx / length
        dy = dy / length
    
    # Перпендикулярный вектор (повернутый на 90 градусов)
    perp_dx = -dy
    perp_dy = dx
    
    # Третья вершина
    x3 = x1 + dx * side_length / 2 + perp_dx * height
    y3 = y1 + dy * side_length / 2 + perp_dy * height
    
    points = [(x1, y1), (x2, y2), (x3, y3)]
    
    if preview:
        pygame.draw.polygon(screen, color, points, 1)
    else:
        pygame.draw.polygon(screen, color, points, 2)

def drawRhombus(screen, start, end, preview=False):
    color = (255, 255, 255)
    x1, y1 = start
    x2, y2 = end
    
    # Центр ромба
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    # Полудиагонали
    half_diag_x = abs(x2 - x1) / 2
    half_diag_y = abs(y2 - y1) / 2
    
    # Вершины ромба
    points = [
        (center_x, center_y - half_diag_y),  # верхняя
        (center_x + half_diag_x, center_y),  # правая
        (center_x, center_y + half_diag_y),  # нижняя
        (center_x - half_diag_x, center_y)   # левая
    ]
    
    if preview:
        pygame.draw.polygon(screen, color, points, 1)
    else:
        pygame.draw.polygon(screen, color, points, 2)

main()