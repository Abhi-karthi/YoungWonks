import pygame
import random
import time
pygame.init()

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
screen = pygame.display.set_mode((750, 750))
#fontobj = pygame.font.SysFont(font_name, font_size, bold=False, italic=False)
colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (5, 5, 5)]

#pygame.draw.rect(screen, orange, (300, 750, 150, 250))
#pygame.draw.circle(screen,orange,(500,150),125)
#pygame.draw.polygon(screen, orange, ((300, 250), (0,650), (0, 750), (300, 350)))

pygame.display.set_caption("100 random circles")
z = 1
x = []
y = []
color = colors[0]
for i in range(1, 100):
    xx = random.randint(1, 750)
    yy = random.randint(1, 750)
    x.append(xx)
    y.append(yy)
while True:
    time.sleep(.05)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for i in range(len(x)):
        if y[i] == 750:
            y[i] = 0
        else:
            y[i] = y[i] + 1
        pygame.draw.circle(screen, color,(x[i], y[i]), 3)
        color = random.choice(colors)
    z += 1
    pygame.display.update()
