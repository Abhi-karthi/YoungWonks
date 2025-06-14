import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1000, 1000))

colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (5, 5, 5)]

#pygame.draw.rect(screen, orange, (300, 750, 150, 250))
#pygame.draw.circle(screen,orange,(500,150),125)
#pygame.draw.polygon(screen, orange, ((300, 250), (0,650), (0, 750), (300, 350)))

pygame.display.set_caption("Moving Squares")
i = 0
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if i < 500:
        color = i//100
        pygame.draw.rect(screen, colors[color-1], (0+i, 0+i, 100, 100))
        pygame.draw.rect(screen, colors[color-1], (900-i, 0+i, 100, 100))
    if i == 500:
        color = i // 100
        pygame.draw.rect(screen, colors[color - 1], (0+400, 0 + i, 200, 100))
        pygame.draw.rect(screen, colors[color - 1], (900+500, 0 + i, 100, 100))
    if i > 500:
        color = i // 100
        print(color)
        pygame.draw.rect(screen, colors[color - 1], (900-i, 0 + i, 100, 100))
        pygame.draw.rect(screen, colors[color - 1], (i, 0 + i, 100, 100))
    i +=100
    pygame.display.update()
    time.sleep(1)