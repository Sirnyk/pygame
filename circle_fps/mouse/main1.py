import pygame
import random

width = 1300
height = 700
fps = 100
small_rad = 1
big_rad = 10
color = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.draw.circle(screen, color, (random.randint(small_rad, width - small_rad), random.randint(small_rad, width - small_rad)), small_rad)

    mouse_buttons = pygame.mouse.get_pressed(3)
    if mouse_buttons[0]:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, mouse_pos, big_rad)

    pygame.display.update()

    clock.tick(fps)

