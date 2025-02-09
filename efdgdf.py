from winreg import KEY_READ
import math
import pygame

width = 1000
height = 700
center = (width//2, height//2)
win = pygame.display.set_mode((width, height))



start_circle_pos = (width//2, height//2)
move = 3
color_slow = (139, 48, 201)
color_fast = (255, 0, 0)
current_color = color_slow
current_circle_pos = list(start_circle_pos)

def find_dist():
    dist = math.sqrt(math.pow(current_circle_pos[0] - start_circle_pos[0], 2) + math.pow(current_circle_pos[1] - start_circle_pos[1], 2))
    return dist


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()




    if key[pygame.K_w]:
        current_circle_pos[1] -= move
    elif key[pygame.K_s]:
        current_circle_pos[1] += move
    elif key[pygame.K_d]:
        current_circle_pos[0] += move
    elif key[pygame.K_a]:
        current_circle_pos[0] -= move
    else:
       if current_circle_pos[1] < start_circle_pos[1]:
            current_circle_pos[1] += move
       if current_circle_pos[1] > start_circle_pos[1]:
           current_circle_pos[1] -= move
       if current_circle_pos[0] < start_circle_pos[0]:
           current_circle_pos[0] += move
       if current_circle_pos[0] > start_circle_pos[0]:
           current_circle_pos[0] -= move

    if find_dist() > 150:
        current_color = color_fast
        move = 1
    else:
        current_color = color_slow
        move = 3


    win.fill((178, 255, 206))
    pygame.draw.circle(win, current_color, current_circle_pos, 30)

    pygame.display.update()
    pygame.time.delay(5)

