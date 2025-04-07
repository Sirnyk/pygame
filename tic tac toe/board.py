import pygame


class Board:
    def __init__(self, side, x, y, block_side):
        self.side = side
        self.x = x
        self.y = y
        self.block_side = block_side
        self.color = (0, 0, 0)
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.move = 1

    def click(self, mouse_pos):
        print('click')

    def draw(self, screen):
        pygame.draw.lines(screen, (0, 0, 0), True,
                          [(self.x, self.y), (self.side + self.x, self.y), (self.side + self.x, self.side + self.y),
                           (self.x, self.side + self.y)])

        pygame.draw.line(screen, self.color , (self.x + self.block_side, self.y), (self.x + self.block_side, self.y + self.side))
        pygame.draw.line(screen, self.color , (self.x + self.block_side*2, self.y), (self.x + self.block_side*2, self.y + self.side))
        pygame.draw.line(screen, self.color , (self.x, self.y + self.block_side), (self.x + self.side, self.y + self.block_side))
        pygame.draw.line(screen, self.color , (self.x, self.y + self.block_side*2),(self.x + self.side, self.y + self.block_side*2))
