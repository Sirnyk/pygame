import rand_color
import pygame
from circle import Circle

width = 1000
height = 700
win_color = (255, 255, 255)
circles = []
rad = 30
circles_cnt = 100
speed = 5
FPS = 50
clock = pygame.time.Clock()

win = pygame.display.set_mode((width, height))

for i in range(circles_cnt):
    circles.append(Circle(rand_color.rand_color(), (i * (width / circles_cnt), i * (height / circles_cnt)), rad, speed))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for i in range(len(circles)):
        circles[i].move(width)

    win.fill(win_color)

    for a in range(len(circles)):
        circles[a].draw(win)

    pygame.display.update()

    clock.tick(FPS)
