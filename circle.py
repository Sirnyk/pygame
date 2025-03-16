import pygame


class Circle:
    is_jumping = False
    CIRCLE_JUMP_HEIGHT = 100
    CIRCLE_JUMP_SPEED = 10
    current_jump = 0
    jump_dir = 1

    def __init__(self, color, pos, rad, speed):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.speed = speed

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos, self.rad)

    def move_by_keys(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.pos[1] -= self.speed
        elif key[pygame.K_s]:
            self.pos[1] += self.speed
        elif key[pygame.K_a]:
            self.pos[0] -= self.speed
        elif key[pygame.K_d]:
            self.pos[0] += self.speed

        if self.is_jumping:
            if self.current_jump < self.CIRCLE_JUMP_HEIGHT:
                self.pos[1] -= self.CIRCLE_JUMP_SPEED * self.jump_dir
                self.current_jump += self.CIRCLE_JUMP_SPEED * self.jump_dir
            elif self.current_jump == self.CIRCLE_JUMP_HEIGHT:
                self.jump_dir *= -1
                self.pos[1] -= self.CIRCLE_JUMP_SPEED * self.jump_dir
                self.current_jump += self.CIRCLE_JUMP_SPEED * self.jump_dir
            if self.current_jump < 0:
                self.is_jumping = False
                print("here")

    def jump(self):
        self.is_jumping = True
        self.current_jump = 0
        self.jump_dir = 1
