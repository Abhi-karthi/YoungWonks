import pygame
import random


def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Comic Sans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))


white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
pygame.init()
colors = [white, red, green, blue, purple]
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Collide Rect")
x = 0
change = 1
balls = []
for i in range(5):
    balls.append(pygame.draw.circle(screen, red, (random.randint(30, 470), 30), 20))
while True:
    for i in balls:
        pygame.draw.circle(screen, red, i.center, 30)
        i.centery += 1
        if i.centery == 500:
            i.centery = 30
    # ball2 = pygame.draw.circle(screen, blue, (500 - x, 250), 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    # show_text(f"Clicked at ball at {pygame.mouse.get_pos()}.", 0, 0, white, 25)
    pygame.display.update()