import pygame
import board
import cross
import circle

screen_size = 700
screen_color = (255, 255, 255)
side = 600
x = 50
y = 50
block_side = side/3

screen = pygame.display.set_mode((screen_size, screen_size))
board = board.Board(side, x, y, block_side)
cross = cross.Cross(x,y,block_side)
circle = circle.Circle(x,y,block_side)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(list(event.pos))

    screen.fill(screen_color)
    board.draw(screen)
    pygame.display.update()