import pygame
import circle


width = 1000
height = 700
color_win = (255, 255, 255)

win = pygame.display.set_mode((width, height))

circle = circle.Circle((0, 255, 255), [width // 2, height // 2], 30, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                circle.jump()

    circle.move_by_keys()

    win.fill(color_win)
    circle.draw(win)
    pygame.display.update()

    pygame.time.delay(20)
