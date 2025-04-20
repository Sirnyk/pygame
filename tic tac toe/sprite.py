import pygame
import class_sprite

height = 700
width = 1000
screen_color = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((width, height))
move = 10
x = width//2
y = height//2

all_sprites = pygame.sprite.Group()
class_sprite.Sprite(x, y, all_sprites)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        all_sprites.update()
        screen.fill((0,0,0))
        all_sprites.draw(screen)
        pygame.display.update()
