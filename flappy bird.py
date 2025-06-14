import pygame
import random
import time


def show_text(msg, x, y, color, size):
    font_obj = pygame.font.SysFont("Comic Sans", size)
    msgobj = font_obj.render(msg, False, color)
    screen.blit(msgobj, (x, y))


white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
grey = (127, 127, 127)
black = (0, 0, 0)
clock = pygame.time.Clock()
pygame.init()
colors = [white, red, green, blue, purple]
screen = pygame.display.set_mode((750,500))
pygame.display.set_caption("Flappy Bird")
bird_display = pygame.image.load("/Users/aaavi/Downloads/Bird_Image.png")
bird_display = pygame.transform.scale(bird_display, (40, 40))
clicks = 0
bird = 0
passed = True
jump = False
rect1 = [700, 0]
rect2 = [0, 0]
score = 0
highscore = 0
newscore = False
jumptime = 0
start = 0
easy = [78, 255, 173] 
normal = [255, 255, 255]
hard = [255, 255, 255]
abhikarthi = [255, 255, 255]
aura = False
while True:
    screen.fill((120, 206, 255))
    if start == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                    pygame.mouse.get_pos()[1] in range(100, 150):
                easy = [78, 255, 173]
                normal = [255, 255, 255]
                hard = [255, 255, 255]
                abhikarthi = [255, 255, 255]
                difficulty = 1
                aura = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                    pygame.mouse.get_pos()[1] in range(175, 225):
                easy = [255, 255, 255]
                normal = [78, 255, 173]
                hard = [255, 255, 255]
                abhikarthi = [255, 255, 255]
                difficulty = 2
                aura = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                    pygame.mouse.get_pos()[1] in range(250, 300):
                easy = [255, 255, 255]
                normal = [255, 255, 255]
                hard = [78, 255, 173]
                abhikarthi = [255, 255, 255]
                difficulty = 3
                aura = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(325, 425) and \
                    pygame.mouse.get_pos()[1] in range(425, 475):
                score = -1
                newscore = False
                if easy == [78, 255, 173]:
                    start = 150
                elif normal == [78, 255, 173]:
                    start = 130
                elif hard == [78, 255, 173]:
                    start = 100
                else:
                    start = 9999999999
                aura = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(0, 75) and \
                    pygame.mouse.get_pos()[1] in range(450, 500):
                score = 0
                easy = [255, 255, 255]
                normal = [255, 255, 255]
                hard = [255, 255, 255]
                abhikarthi = [78, 255, 173]
                aura = True

        pygame.draw.rect(screen, tuple(easy), (100, 100, 100, 50))
        show_text("Easy", 100, 100, black, 25)
        pygame.draw.rect(screen, tuple(normal), (100, 175, 100, 50))
        show_text("Normal", 100, 175, black, 25)
        pygame.draw.rect(screen, tuple(hard), (100, 250, 100, 50))
        show_text("Hard", 100, 250, black, 25)
        pygame.draw.rect(screen, (78, 255, 173), (325, 425, 100, 50))
        show_text("Start", 345, 425, black, 25)
        show_text("Difficulty", 110, 60, white, 20)
        show_text("Prev. Score", 475, 115, white, 20)
        show_text(f"{score}", 515, 160, black, 50)
        show_text("Abhikarthi Mode", 0, 450, black, 25)
        show_text("Highscore", 475, 210, white, 20)
        show_text(f"{highscore}", 515, 265, black, 50)
        if newscore:
            show_text("New high score!", 250, 80, black, 35)
        show_text("Flappy Bird!", 250, 15, white, 50)
    else:
        if passed:
            score += 1
            if score > highscore:
                highscore = score
                newscore = True
            rect1[0] = 700
            rect1[1] = random.randint(0, 350)
            rect2[0] = rect1[1] + start
            rect2[1] = 500 - rect2[0]
            passed = False
        fps = int(clock.get_fps())
        # ball = pygame.Rect(pygame.draw.circle(screen, white, (20, bird), 20, 4))
        ball = pygame.Rect((0, bird-20, 40, 40))
        screen.blit(bird_display, (0, bird-20))
        upper_block = pygame.draw.rect(screen, green, (rect1[0], 0, 50, rect1[1]))
        lower_block = pygame.draw.rect(screen, green, (rect1[0], rect2[0], 50, rect2[1]))
        if not aura:
            if ball.colliderect(upper_block):
                bird = 250
                passed = True
                start = False
            if ball.colliderect(lower_block):
                bird = 250
                passed = True
                start = False
            rect1[0] -= 5
            if rect1[0] < -20:
                passed = True
        else:
            passed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = True
                    jumptime = time.time()
                if event.key == pygame.K_ESCAPE:
                    bird = 250
                    passed = True
                    start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                jump = True
                jumptime = time.time()
        if jump:
            if bird > 20:
                bird -= 11 - ((time.time() - jumptime) * 10)
            if time.time() - jumptime > 1.1:
                jumptime = time.time()
                jump = False

        show_text(str(score), 350, 0, black, 50)
        if bird < 480:
            bird += 5
        show_text("esc. to quit", 0, 0, black, 25)
    clock.tick(60)
    pygame.display.update()
