import pygame

class Field:
    def __init__(self, x, y, side, block_side):
        self.x = x
        self.y = y
        self.side = side
        self.block_side = block_side
        self.color = (255, 255, 255)

    def draw(self, win):
        pygame.draw.lines(win, self.color, True, [(self.x, self.y), (self.x + self.side, self.y),
                                                  (self.x + self.side, self.y + self.side), (self.x, self.y + self.side), (self.x, self.y)])
        for i in range(1, 17):
            pygame.draw.line(win, self.color, (self.x + self.block_side * i, self.y), (self.x + self.block_side * i, self.y + self.side))
        for i in range(1, 17):
            pygame.draw.line(win, self.color, (self.x, self.y + self.block_side * i), (self.x + self.side, self.y + self.block_side * i))

