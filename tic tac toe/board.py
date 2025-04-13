import pygame


class Board:
    def __init__(self, side, x, y, block_side):
        self.side = side
        self.x = x
        self.y = y
        self.block_side = block_side
        self.color = (0, 0, 0)
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.move = 1

    def click(self, mouse_pos):
        if (mouse_pos[0] < self.x or mouse_pos[0] >= self.x + self.side or
                mouse_pos[1] < self.y or mouse_pos[1] >= self.y + self.side):
            return
        mouse_pos[0] -= self.x
        mouse_pos[1] -= self.y
        index = [int(mouse_pos[0] // self.block_side), int(mouse_pos[1] // self.block_side)]

        if self.board[index[0]][index[1]] == 0:
            self.board[index[0]][index[1]] = self.move
            self.move *= -1

    def draw(self, screen):
        pygame.draw.lines(screen, (0, 0, 0), True,
                          [(self.x, self.y), (self.side + self.x, self.y), (self.side + self.x, self.side + self.y),
                           (self.x, self.side + self.y)])

        pygame.draw.line(screen, self.color, (self.x + self.block_side, self.y),
                         (self.x + self.block_side, self.y + self.side))
        pygame.draw.line(screen, self.color, (self.x + self.block_side * 2, self.y),
                         (self.x + self.block_side * 2, self.y + self.side))
        pygame.draw.line(screen, self.color, (self.x, self.y + self.block_side),
                         (self.x + self.side, self.y + self.block_side))
        pygame.draw.line(screen, self.color, (self.x, self.y + self.block_side * 2),
                         (self.x + self.side, self.y + self.block_side * 2))

        for i in range(3):
            for j in range(3):
                index = [i, j]
                edge = [self.x + i * self.block_side, self.y + j * self.block_side]
                if self.board[i][j] == 1:
                    pygame.draw.circle(screen, self.color,
                                       (edge[0] + self.block_side // 2, edge[1] + self.block_side // 2),
                                       self.block_side // 2, 5)
                if self.board[i][j] == -1:
                    pygame.draw.line(screen, self.color, edge, (edge[0] + self.block_side, edge[1] + self.block_side),
                                     5)
                    pygame.draw.line(screen, self.color, (edge[0], edge[1] + self.block_side),
                                     (edge[0] + self.block_side, edge[1]), 5)
