import pygame
import random

width = 1300
height = 700
fps = 100
min_size = 10
max_size = 100
size = min_size
screen_color = (255, 255, 255)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


figure = 'circle'
direction = 'up'

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(screen_color)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(screen_color)
            if event.key == pygame.K_w:
                figure = 'circle'
            if event.key == pygame.K_q:
                figure = 'rect'

    mouse_pos = pygame.mouse.get_pos()

    if direction == 'up':
        size += 1
        if size == max_size:
            direction = 'down'
    if direction == 'down':
        size -= 1
        if size == min_size:
            direction = 'up'

    if figure == 'circle':
        pygame.draw.circle(screen, random_color(), mouse_pos, size)
    if figure == 'rect':
        pygame.draw.rect(screen, random_color(), (mouse_pos[0] - size, mouse_pos[1] - size, 2 * size, 2 * size))

    pygame.display.update()

    clock.tick(fps)
