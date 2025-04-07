import pygame

class Cross:
    def __init__(self, x, y, block_side):
        self.x = x
        self.y = y
        self.block_side = block_side
        self.color = (0, 0, 255)
        self.thickness = 5

    def draw_cross(self, screen):
        pygame.draw.line(screen, self.color, (self.x,self.y), (self.x + self.block_side, self.y + self.block_side), self.thickness)
        pygame.draw.line(screen, self.color, (self.x + self.block_side, self.y), (self.x, self.y + self.block_side), self.thickness)