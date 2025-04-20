import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.image.load('maple-leaf.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move = 3

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.rect.y -= self.move
        elif key[pygame.K_s]:
            self.rect.y += self.move
        elif key[pygame.K_d]:
            self.rect.x += self.move
        elif key[pygame.K_a]:
            self.rect.x -= self.move
