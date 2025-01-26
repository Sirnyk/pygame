import pygame


def check_input(num):
    if len(num) != 2:
        return False
    if not num[0].isdigit() or not num[1].isdigit():
        return False
    if not int(num[0]) % int(num[1]) == 2:
        return False
    return True


num = input().split(' ')

if not check_input(num):
    print('Неправильный формат ввода')
    exit()

print(num)
width = int(num[0])
height = int(num[1])
pygame.init()

win = pygame.display.set_mode((width, height))

win.fill((192, 232, 112))

pygame.draw.line(win, (0, 0, 0), (0, 0), (width, height), 5)
pygame.draw.line(win, (0, 0, 0), (width, 0), (0, height), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
