import pygame
import random
import time

def show_text(msg, x, y, color, size):
    font_object = pygame.font.SysFont("Comic Sans", size)
    msgobj = font_object.render(msg, False, color)
    screen.blit(msgobj, (x, y))

pygame.init()
score_1 = 0
score_2 = 0
ball = [375, 250]
paddleL = 210
movementL = 0
paddleR = 210
movementR = 0
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
grey = (127, 127, 127)
black = (0, 0, 0)
clock = pygame.time.Clock()
colors = [white, red, green, blue, purple]
screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Pong")
y1 = 250
y2 = 250
counter = 1
angle1 = 0
angle2 = 1
negative = 0
difficulty = 1
g_and_b = 255
slow = [78, 255, 173]
normal = [255, 255, 255]
fast = [255, 255, 255]
single_player = [78, 255, 173]
multi_player = [255, 255, 255]
start = False
player = 0
graphicsL = 0
graphicsR = 0
paddle_lg = 0
paddle_rg = 0
while True:
    screen.fill((120, 206, 255))
    fps = int(clock.get_fps())
    if player == 0:
        if ball[1] < paddleR + 40:
            movementR = 1
        else:
            movementR = 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movementL = 1
            if event.key == pygame.K_s:
                movementL = 2
            if player == 1:
                if event.key == pygame.K_UP:
                    movementR = 1
                if event.key == pygame.K_DOWN:
                    movementR = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movementL = 0
            if event.key == pygame.K_s:
                movementL = 0
            if player == 1:
                if event.key == pygame.K_UP:
                    movementR = 0
                if event.key == pygame.K_DOWN:
                    movementR = 0
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                pygame.mouse.get_pos()[1] in range(100, 150):
            slow = [78, 255, 173]
            normal = [255, 255, 255]
            fast = [255, 255, 255]
            difficulty = 1
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                pygame.mouse.get_pos()[1] in range(175, 225):
            slow = [255, 255, 255]
            normal = [78, 255, 173]
            fast = [255, 255, 255]
            difficulty = 2
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                pygame.mouse.get_pos()[1] in range(250, 300):
            slow = [255, 255, 255]
            normal = [255, 255, 255]
            fast = [78, 255, 173]
            difficulty = 3
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(450, 650) and \
                pygame.mouse.get_pos()[1] in range(150, 200):
            player = 0
            single_player = [78, 255, 173]
            multi_player = [255, 255, 255]
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(450, 650) and \
                pygame.mouse.get_pos()[1] in range(225, 275):
            player = 1
            single_player = [255, 255, 255]
            multi_player = [78, 255, 173]
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(325, 425) and \
                pygame.mouse.get_pos()[1] in range(425, 475):
            start = True
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(0, 200) and \
                pygame.mouse.get_pos()[1] in range(450, 500):
            if start:
                score_1 = 0
                score_2 = 0
                counter = 1
                start = False
    if not start:
        pygame.draw.rect(screen, tuple(slow), (100, 100, 100, 50))
        show_text("Easy", 100, 100, black, 25)
        pygame.draw.rect(screen, tuple(normal), (100, 175, 100, 50))
        show_text("Normal", 100, 175, black, 25)
        pygame.draw.rect(screen, tuple(fast), (100, 250, 100, 50))
        show_text("Hard", 100, 250, black, 25)
        pygame.draw.rect(screen, tuple(single_player), (450, 150, 200, 50))
        show_text("Single Player", 450, 150, black, 25)
        pygame.draw.rect(screen, tuple(multi_player), (450, 225, 200, 50))
        show_text("Multiplayer", 450, 225, black, 25)
        pygame.draw.rect(screen, (78, 255, 173), (325, 425, 100, 50))
        show_text("Start", 345, 425, black, 25)
        show_text("Difficulty", 110, 60, white, 20)
        show_text("Player Number", 475, 115, white, 20)
        show_text("Pong!", 325, 25, white, 50)
    else:
        show_text("Quit to Menu", 0, 450, black, 25)
        if counter == 1:
            pygame.draw.circle(screen, color=(120, 206, 255), center=(375, 250), radius=25)
            pygame.draw.circle(screen, color=white, center=(375, 250), radius=25)
            pygame.display.update()
            time.sleep(.5)
            pygame.draw.circle(screen, color=(120, 206, 255), center=(375, 250), radius=25)
            pygame.display.update()
            time.sleep(.5)
            pygame.draw.circle(screen, color=white, center=(375, 250), radius=25)
            pygame.display.update()
            time.sleep(.5)
            pygame.draw.circle(screen, color=white, center=(375, 250), radius=25)
            pygame.display.update()
            pygame.draw.circle(screen, color=(120, 206, 255), center=(375, 250), radius=25)
            angle1 = random.randint(1, 3)

            angle2 = random.randint(1, 3)

            negative = random.randint(0, 1)
            if negative == 1:
                angle1 = angle1 * -1
            negative = random.randint(0, 1)
            if negative == 1:
                angle2 = angle2 * -1
            ball = [375, 250]
            g_and_b = 255
            counter = -1
        elif counter == 2:
            angle1 = random.randint(1, 3)

            angle2 = random.randint(1, 3)

            negative = random.randint(0, 1)
            if negative == 1:
                angle1 = angle1 * -1
            negative = random.randint(0, 1)
            if negative == 1:
                angle2 = angle2 * -1
            ball = [375, 250]
            g_and_b = 255
            counter = -2
        elif counter == 3:
            angle1 = random.randint(1, 3)

            angle2 = random.randint(1, 3)

            negative = random.randint(0, 1)
            if negative == 1:
                angle1 = angle1 * -1
            negative = random.randint(0, 1)
            if negative == 1:
                angle2 = angle2 * -1
            ball = [375, 250]
            g_and_b = 255
            counter = -3
        elif counter == 4:
            angle1 = random.randint(1, 3)

            angle2 = random.randint(1, 3)

            negative = random.randint(0, 1)
            if negative == 1:
                angle1 = angle1 * -1
            negative = random.randint(0, 1)
            if negative == 1:
                angle2 = angle2 * -1
            ball = [375, 250]
            g_and_b = 255
            counter = -4
        elif counter == 5:
            angle1 = random.randint(1, 3)

            angle2 = random.randint(1, 3)

            negative = random.randint(0, 1)
            if negative == 1:
                angle1 = angle1 * -1
            negative = random.randint(0, 1)
            if negative == 1:
                angle2 = angle2 * -1
            ball = [375, 250]
            g_and_b = 255
            counter = -5
        elif counter == 6:
            screen.fill((120, 206, 255))
            show_text("Quit to Menu", 0, 450, black, 25)
            if score_1 > score_2:
                show_text(f"Left wins!", x=325, y=10, color=white, size=50)
            elif score_1 < score_2:
                show_text(f"Right wins!", x=325, y=10, color=white, size=50)
            pygame.display.update()

        if counter != 6:
            ball[0] += angle1
            ball[1] += angle2

            pygame.draw.rect(screen, black, (0, paddleL, 8, 80), 2)
            pygame.draw.rect(screen, black, (740, paddleR, 10, 80), 2)
            pygame.draw.circle(screen, black, center=tuple(ball), radius=25, width=3)
            pygame.draw.circle(screen, (255, g_and_b, g_and_b), ball, 22)

            if movementL == 1:
                if paddleL > 0:
                    paddleL -= 5
            if movementR == 1:
                if paddleR > 0:
                    paddleR -= 5

            if movementL == 2:
                if paddleL < 420:
                    paddleL += 5
            if movementR == 2:
                if paddleR < 420:
                    paddleR += 5


            if ball[1] - 25 < 0:
                angle2 = angle2 * -1
            if ball[1] + 25 > 500:
                angle2 = angle2 * -1
            if ball[1] in range(paddleL - 7, paddleL + 94) and ball[0] < 35:
                angle1 = angle1 * -1
                graphicsL = 1
                if difficulty == 2:
                    if angle2 > 0:
                        angle2 += 1
                    else:
                        angle2 -= 1
                    if angle1 > 0:
                        angle1 += 1
                    else:
                        angle1 -= 1
                    g_and_b -= 5
                if difficulty == 3:
                    if angle2 > 0:
                        angle2 += 2
                    else:
                        angle2 -= 2
                    if angle1 > 0:
                        angle1 += 2
                    else:
                        angle1 -= 2
                    g_and_b -= 10
            if ball[1] in range(paddleR - 7, paddleR + 94) and ball[0] > 715:
                angle1 = angle1 * -1
                graphicsR = 1
                if difficulty == 2:
                    if angle2 > 0:
                        angle2 += 1
                    else:
                        angle2 -= 1
                    if angle1 > 0:
                        angle1 += 1
                    else:
                        angle1 -= 1
                    g_and_b -= 5
                if difficulty == 3:
                    if angle2 > 0:
                        angle2 += 2
                    else:
                        angle2 -= 2
                    if angle1 > 0:
                        angle1 += 2
                    else:
                        angle1 -= 2
                    g_and_b -= 10

            if ball[0] - 25 < 0:
                if ball[0] + 25 not in range(paddleL - 7, paddleL + 94):
                    counter = counter * -1
                    counter += 1
                    score_2 += 1
            if ball[0] + 25 > 750:
                if ball[0] + 25 not in range(paddleR - 7, paddleR + 94):
                    counter = counter * -1
                    counter += 1
                    score_1 += 1
            show_text(f"{score_1} - {score_2}", x=350, y=10, color=black, size=50)
            if graphicsL > 0:
                if graphicsL == 1:
                    paddle_lg = ball[1]
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (10 + graphicsL/3 * 2, paddle_lg + graphicsL * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (10 + graphicsL / 2.5 * 2, paddle_lg + graphicsL/1.25 * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (10 + graphicsL/2 * 2, paddle_lg + graphicsL/2 * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (10 + graphicsL/1.5 * 2, paddle_lg, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (10 + graphicsL/2 * 2, paddle_lg - graphicsL/2 * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (10 + graphicsL / 2.5 * 2, paddle_lg - graphicsL/1.25 * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (10 + graphicsL/3 * 2, paddle_lg - graphicsL * 2, 5, 5))
                graphicsL += 1
                if graphicsL > 50:
                    graphicsL = 0
            if graphicsR > 0:
                if graphicsR == 1:
                    paddle_rg = ball[1]
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (740 - graphicsR/3 * 2, paddle_rg + graphicsR * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (740 - graphicsR/2.5 * 2, paddle_rg + graphicsR/1.25 * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (740 - graphicsR/2 * 2, paddle_rg + graphicsR/2 * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (740 - graphicsR/1.5 * 2, paddle_rg, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (740 - graphicsR/2 * 2, paddle_rg - graphicsR/2 * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (740 - graphicsR/2.5 * 2, paddle_rg - graphicsR/1.25 * 2, 5, 5))
                pygame.draw.rect(screen, (255, g_and_b, g_and_b), (740 - graphicsR/3 * 2, paddle_rg - graphicsR * 2, 5, 5))
                graphicsR += 1
                if graphicsR > 50:
                    graphicsR = 0
    clock.tick(60)
    pygame.display.update()
