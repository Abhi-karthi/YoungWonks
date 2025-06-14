import pygame
jump = False
import random
import time
#pygame.draw.rect(screen, blue, (300, 750, 150, 250))
#pygame.draw.circle(screen,blue,(500,150)) )))))
#pygame.draw.polygon(screen, blue, ((300, 250), (0,650), (0, 750), (300, 350)))
#pygame.draw.line(surface, blue, start_pos, end_pos, width)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1500, 750))
pygame.display.set_caption("Blue Bicycle")
colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (25, 25, 25)]
def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
x = 200
y = 720
right = False
left = False
up = False
down = False
level = 0
color = 0


while True:
    if x in range(702, 1051) and y == 620:
        level = 2
    fps = int(clock.get_fps())
    screen.fill((0,0,0))
    pygame.draw.rect(screen, colors[8], (500, 680, 200, 25)) #1st platform
    pygame.draw.rect(screen, colors[8], (702, 620, 400, 25)) #2nd platform
    pygame.draw.circle(screen, colors[color], (x, y), 30)
    if color == 9:
        color = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_SPACE:
                color += 1
            if event.key == pygame.K_DOWN:
                down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
    if x in range(500, 701) and y == 650:
        level = 1
    if left:
        x -= 2
    if right:
        x += 2


    if level == 0:

        if y == 720:
            jump = True
        if y == 620:
            jump = False


        if up:
            if jump:
                y -= 2
        else:
            jump = False


        if jump == False:
            if y != 720:
                y += 2


    if level == 1:
        if x in range(500, 701) and y <= 650:
            if y == 650:
                jump = True
            if y == 550:
                jump = False

            else:
                if y == 550:
                    jump = False

            if up:
                if jump:
                    y -= 2
            else:
                jump = False

            if jump == False:
                if y != 650:
                    y += 2
        else:
            if jump == False:
                level = 0
            else:
                if y == 650:
                    jump = True
                if y == 550:
                    jump = False

                else:
                    if y == 550:
                        jump = False

                if up:
                    if jump:
                        y -= 2
                else:
                    jump = False

                if jump == False:
                    if y != 650:
                        y += 2
    if level == 2:
        if x in range(702, 1102) and y <= 650:
            if y == 750:
                jump = True
            if y == 650:
                jump = False

            else:
                if y == 650:
                    jump = False

            if up:
                if jump:
                    y -= 2
            else:
                jump = False

            if jump == False:
                y += 2
        else:
            if jump == False:
                level = 0
            else:
                if y == 750:
                    jump = True
                if y == 650:
                    jump = False

                else:
                    if y == 650:
                        jump = False

                if up:
                    if jump:
                        y -= 2
                else:
                    jump = False

                if jump == False:
                    y += 2
    pygame.display.update()
    clock.tick(200)