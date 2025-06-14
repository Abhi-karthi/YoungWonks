import pygame
import random


class Obstacle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        self.direction = 1
        self.visibility = True
        self.key = chr(random.randint(97, 122))


pygame.init()
screen = pygame.display.set_mode((1000, 750))

colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (5, 5, 5)]
circles = []
objects = 536870912
for i in range(objects):
    circles.append(Circle(random.randint(5, 25), random.randint(25, 975), random.randint(25, 725), (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))))
    print(len(circles))
# pygame.draw.rect(screen, orange, (300, 750, 150, 250))
# pygame.draw.circle(screen,orange,(500,150),125)
# pygame.draw.polygon(screen, orange, ((300, 250), (0,650), (0, 750), (300, 350)))
clock = pygame.time.Clock()
pygame.display.set_caption("Circles")
while True:
    screen.fill((0, 0, 0))
    for i in circles:
        if i.visibility:
            pygame.draw.circle(screen, i.color, (i.x, i.y), i.radius)
        i.move()
        i.bounce_back()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            for i in circles:
                if chr(event.key) == i.key:
                    if not i.visibility:
                        i.visibility = True
                    else:
                        i.visibility = False
                if event.key == pygame.K_SPACE:
                    if i.visibility:
                        i.visibility = False
                    else:
                        i.visibility = True

    clock.tick(60)
    pygame.display.update()