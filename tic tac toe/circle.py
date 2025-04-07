import pygame

class Circle:
    def __init__(self, x, y, block_side):
        self.x = x
        self.y = y
        self.block_side = block_side
        self.color = (255, 0, 0)
        self.thickness = 5

    def draw_circle(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + self.block_side//2, self.y + self.block_side*1.5), self.block_side//2, self.thickness)
