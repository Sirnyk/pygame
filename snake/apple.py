import pygame

class Apple:
    def __init__(self, x_apple, y_apple):
        self.x_apple = x_apple
        self.y.apple = y_apple
        self.apple_color = (255, 255, 255)

    def draw(self, win):
        pygame.draw.rect(win, self.apple_color, )