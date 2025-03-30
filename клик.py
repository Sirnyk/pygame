import pygame
import random

width = 1000
height = 700
win = pygame.display.set_mode((width, height))

start_circle_pos = (width // 2, height // 2)
color_circle = (236, 28, 76)
color_background = (246, 215, 161)
current_pos = list(start_circle_pos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                current_pos[0] = random.randint(1, width) - 1
                for a in range(1, random.randint(1, height)):
                    current_pos[1] = a

    win.fill(color_background)
    pygame.draw.circle(win, color_circle, current_pos, 30)

    pygame.display.update()
