import pygame
import random
import time
#pygame.draw.rect(screen, blue, (300, 750, 150, 250))
#pygame.draw.circle(screen,blue,(500,150),125)
#pygame.draw.polygon(screen, blue, ((300, 250), (0,650), (0, 750), (300, 350)))
#pygame.draw.line(surface, blue, start_pos, end_pos, width)
pygame.init()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Blue Bicycle")
blue = (0,0,255)
colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (25, 25, 25)]
def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
pygame.draw.circle(screen,blue,(200,350),50, 3)
pygame.draw.line(screen,blue,(355,255),(335,255),3)
pygame.draw.line(screen,blue,(400,350),(355,255), 3)
pygame.draw.line(screen,blue,(200,350),(250,290), 3)
pygame.draw.circle(screen,blue,(400,350),50, 3)
pygame.draw.line(screen,blue,(315,350),(365,275), 3)
pygame.draw.line(screen,blue,(280,350), (242.5,275), 3)
pygame.draw.line(screen,blue,(230,275),(255,275),3)
pygame.draw.line(screen,blue,(200,350), (315,350), 3)
while True:
    print()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
