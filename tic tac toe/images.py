from lib2to3.pytree import convert

import pygame


height = 700
width = 1000
screen_color = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((width, height))

'''img = pygame.image.load('maple-leaf.png')
img = img.convert()

color_key = img.get_at((0, 0))
img.set_colorkey(color_key)'''

'''img1 = pygame.transform.scale(img, (100,100))
img2 = pygame.transform.scale(img, (200,300))
img3 = pygame.transform.rotate(img, 90)'''

all_sprites = pygame.sprite.Group()

for i in range(5):
    sprite = pygame.sprite.Sprite(all_sprites)
    sprite.image = pygame.image.load('maple-leaf.png')

    sprite.image = pygame.transform.scale(sprite.image, (100, 100))
    sprite.rect = sprite.image.get_rect()

    sprite.rect.x = i * 100

    all_sprites.add(sprite)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        '''screen.blit(img1, (0, 0))
        screen.blit(img2, (100, 100))
        screen.blit(img3, (300, 300))'''
        pygame.display.update()