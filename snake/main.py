import field
import pygame

win_size = 1000
win_color = (0, 0, 0)
x = 100
y = 100
side = 800
block_side = side/16

win = pygame.display.set_mode((win_size, win_size))
field = field.Field(x, y, side, block_side)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(win_color)
    field.draw(win)
    pygame.display.update()