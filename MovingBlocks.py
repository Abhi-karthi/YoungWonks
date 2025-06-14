import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Python Advertisement")

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))

i = 750

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    show_text("YoungWonks Hackathon coming next month!", i, 400, (255, 255, 255), 50)
    pygame.display.update()

    if i < 1500:
        i += 1
    elif i == 1500:
        i = 0
