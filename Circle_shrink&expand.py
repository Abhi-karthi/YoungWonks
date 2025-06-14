import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))

colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (5, 5, 5)]

#pygame.draw.rect(screen, orange, (300, 750, 150, 250))
#pygame.draw.circle(screen,orange,(500,150),125)
#pygame.draw.polygon(screen, orange, ((300, 250), (0,650), (0, 750), (300, 350)))

pygame.display.set_caption("Circle")
i = 10
a = 0
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.draw.circle(screen, colors[0], (500, 500), i)

    if i < 500:
        if a == 0:
            i += 1
        else:
            if i == 10:
                a = 0
            else:
                i -= 1
    elif i >= 500:
        i -= 1
        a = 1
    pygame.display.update()