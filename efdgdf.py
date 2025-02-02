import pygame


win = pygame.display.set_mode((500, 500))

win.fill((192, 232, 112))

pygame.draw.circle(win, (0,0,0), (100,100), (500,500), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()