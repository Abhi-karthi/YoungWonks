import pygame
import random
import time


def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Comic Sans", size)
    msgobj = fontobj.render(msg, False, color)
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
pygame.display.set_caption("CPS Test")
clicks = 0
highscore = 0
newscore = False
cpstime = 1
start = 0
timer = 0
onesec = [78, 255, 173]
fivesec = [255, 255, 255]
tensec = [255, 255, 255]
go = False
while True:
    screen.fill((120, 206, 255))
    if not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                    pygame.mouse.get_pos()[1] in range(100, 150):
                onesec = [78, 255, 173]
                fivesec = [255, 255, 255]
                tensec = [255, 255, 255]
                cpstime = 1
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                    pygame.mouse.get_pos()[1] in range(175, 225):
                onesec = [255, 255, 255]
                fivesec = [78, 255, 173]
                tensec = [255, 255, 255]
                cpstime = 5
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(100, 200) and \
                    pygame.mouse.get_pos()[1] in range(250, 300):
                onesec = [255, 255, 255]
                fivesec = [255, 255, 255]
                tensec = [78, 255, 173]
                cpstime = 10
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(325, 425) and \
                    pygame.mouse.get_pos()[1] in range(425, 475):
                clicks = -1
                newscore = False
                start = True
        pygame.draw.rect(screen, tuple(onesec), (100, 100, 100, 50))
        show_text("1", 100, 100, black, 25)
        pygame.draw.rect(screen, tuple(fivesec), (100, 175, 100, 50))
        show_text("5", 100, 175, black, 25)
        pygame.draw.rect(screen, tuple(tensec), (100, 250, 100, 50))
        show_text("10", 100, 250, black, 25)
        pygame.draw.rect(screen, (78, 255, 173), (325, 425, 100, 50))
        show_text("Start", 345, 425, black, 25)
        show_text("Time", 110, 60, white, 20)
        show_text("Prev. Score", 475, 115, white, 20)
        show_text(f"{clicks}", 515, 160, black, 50)
        show_text("Highscore", 475, 210, white, 20)
        show_text(f"{highscore}", 515, 265, black, 50)
        if newscore:
            show_text("New high score!", 250, 80, black, 35)
        show_text("CPS Test!", 250, 15, white, 50)
    else:
        if go:
            if time.time() - timer <= cpstime:
                show_text(f"{time.time()-timer}", 0, 0, black, 50)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clicks += 1
            else:
                clicks = clicks/cpstime
                if clicks > newscore:
                    newscore = clicks
                go = False
                start = False
        else:
            show_text("Click to start", 250, 225, black, 25)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    timer = time.time()
                    go = True

    clock.tick(60)
    pygame.display.update()