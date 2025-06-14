import pygame
import random


def show_text(msg, x, y, color, size, font):
    fontobj = pygame.font.SysFont(font, size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))


class Circle:
    radius = 5
    def __init__(self, x: int, y: int, color: tuple[int, int, int]):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = random.randint(1, 5)
        self.speed_y = 0
        self.direction = 100
        self.visibility = True
        self.key = chr(random.randint(97, 122))
        self.lap = 0
        self.finish = False

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce_back(self):
        if self.x >= 1000 - self.radius or self.x <= self.radius:
            self.speed_x *= -1
            self.lap += 1
            if self.lap > 3:
                self.speed_x = 0
                self.finish = True
        if self.y >= 750 - self.radius or self.y <= self.radius:
            self.speed_y *= -1


pygame.init()
screen = pygame.display.set_mode((1000, 750))
circle_display = []
colors = [(255, 255, 255), (255, 229, 180), (128, 0, 128), (0, 255, 0), (0, 0, 255), (240, 100, 0), (235, 225, 0), (125, 125, 125), (255, 0, 0), (5, 5, 5)]
circles = []
objects = 200
x = 0
for i in range(objects):
    circles.append(Circle( 25, random.randint(25, 725), (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))))

# pygame.draw.rect(screen, orange, (300, 750, 150, 250))
# pygame.draw.circle(screen,orange,(500,150),125)
# pygame.draw.polygon(screen, orange, ((300, 250), (0,650), (0, 750), (300, 350)))
clock = pygame.time.Clock()
pygame.display.set_caption("Circles")
finishers = 0
for i in circles:
    circle_display.append(pygame.Rect(pygame.draw.circle(screen, i.color, (i.x, i.y), i.radius)))
while True:
    screen.fill((0, 0, 0))
    finishers = 0
    circles_display = []
    for i in circles:
        circles_display.append(pygame.Rect(pygame.draw.circle(screen, i.color, (i.x, i.y), i.radius)))
    for i in range(len(circles)):
        if circles[i].finish:
            finishers += 1
        if circles[i].visibility:
            pygame.draw.circle(screen, circles[i].color, (circles[i].x, circles[i].y), circles[i].radius)
        circles[i].move()
        circles[i].bounce_back()
    show_text(f"Finishers: {finishers}", 0, 0, (255, 255, 255), 50, "freesans")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Circle.radius += 5
            elif event.key == pygame.K_DOWN:
                Circle.radius -= 5
            else:
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in circles_display:
                    if i.collidepoint(event.pos):
                        circles[circles_display.index(i)].radius += 2
                        print("hi")
            if event.button == 2:
                for i in circles_display:
                    if i.collidepoint(event.pos):
                        circles[circles_display.index(i)].radius -= 2




    #print(len(circles), len(circles_display))
    clock.tick(60)
    pygame.display.update()
