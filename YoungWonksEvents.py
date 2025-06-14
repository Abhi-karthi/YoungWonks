import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("YoungWonks events")
colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (25, 25, 25)]
def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))


while True:
    time.sleep(1)
    randomint1 = random.randint(0,9)
    print(randomint1)
    randomint2 = random.randint(0, 9)
    print(randomint2)
    randomint3 = random.randint(0, 9)
    print(randomint3)
    randomint4 = random.randint(0, 9)
    print(randomint4)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    show_text("YoungWonks Hackathon", 400, 0, colors[randomint1], 30)
    show_text("CCI Fair", 400, 50, colors[randomint2], 30)
    show_text("RoboRave", 400, 100, colors[randomint3], 30)
    show_text("Makers Day", 400, 150, colors[randomint4], 30)
    pygame.display.update()
