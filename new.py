import pygame

width = 1000
height = 700
start_pos_circle = (50, 50)
start_pos_rect = (500, 50)
start_pos_circle1 = (100, 100)
rad = 50
rad1 = 25
rect_width = 300
rect_height = 200
move_circle = 1
move_rect = 1
move1 = 1
move2 = 1
win = pygame.display.set_mode((width, height))

circle_pos = list(start_pos_circle)
rect_pos = list(start_pos_rect)
circle1_pos = list(start_pos_circle1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    circle_pos[0] += move_circle
    rect_pos[1] += move_rect
    circle1_pos[0] += move1
    circle1_pos[1] += move2

    if circle_pos[0] > width or circle_pos[0] < 0:
        move_circle *= -1
    if rect_pos[1] > height or rect_pos[1] < 0:
        move_rect *= -1
    if circle1_pos[0] > width or circle1_pos[0] < 0:
        move1 *= -1
    if circle1_pos[1] > height or circle1_pos[1] < 0:
        move2 *= -1

    win.fill((192, 232, 112))
    pygame.draw.circle(win, (0,0,0), circle_pos, rad)
    pygame.draw.rect(win, (0,0,0), (rect_pos[0], rect_pos[1], rect_width, rect_height))
    pygame.draw.circle(win, (100,100,100), circle1_pos, rad1)


    pygame.display.update()
    pygame.time.delay(10)
