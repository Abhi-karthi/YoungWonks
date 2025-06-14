import pygame
import random
import time
pygame.init()
def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
screen = pygame.display.set_mode((750, 750))

colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (5, 5, 5)]

#pygame.draw.rect(screen, orange, (300, 750, 150, 250))
#pygame.draw.circle(screen,orange,(500,150),125)
#pygame.draw.polygon(screen, orange, ((300, 250), (0,650), (0, 750), (300, 350)))

pygame.display.set_caption("100 random circles")
z = 1
x = []
y = []
color = colors[0]
text = input()
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    show_text("Enter some text", 10, 10, (0,0,255), 32)
    pygame.display.update()

    show_text(text, 10, 50, (0, 0, 255), 32)
    pygame.display.update()

