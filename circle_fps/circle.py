import pygame
import rand_color


class Circle:
    circle_dir = 1

    def __init__(self, color, pos, rad, speed):
        self.color = color
        self.pos = list(pos)
        self.rad = rad
        self.speed = speed

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos, self.rad)

    def move(self, width):
        if self.circle_dir == 1:
            self.pos[0] += self.speed
        elif self.circle_dir == -1:
            self.pos[0] -= self.speed
        if self.pos[0] >= width:
            self.circle_dir *= -1
            self.color = rand_color.rand_color()
        elif self.pos[0] <= 0:
            self.circle_dir *= -1
            self.color = rand_color.rand_color()