import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("evaluation")
colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
x = 300
y = 300
up = False
left = False
down = False
right = False
spaceship = pygame.image.load("/Users/aaavi/Downloads/Spaceship_use.png")
run = []
for i in range(10):
    image = pygame.image.load(f"/Users/aaavi/Zombie/png-3 less/Run__00{i}.png")
    image = pygame.transform.scale(image, (150, 150))
    run.append(image)
image_number = 0
pygame.transform.scale(spaceship, (50, 50))
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))
    # pygame.draw.circle(screen, (255, 255, 255), (x, y), 25)
    # screen.blit(spaceship, (x - 15, y - 10))
    # pygame.draw.rect(screen, (125, 125, 125), (150, 150, 300, 300))
    # pygame.draw.circle(screen, colors[l_color], (225, circle_l), 35)
    # pygame.draw.circle(screen, colors[r_color], (375, circle_r), 35)
    # pygame.draw.rect(screen, (0, 0, 0), (mouth, 350, 150, 50))
    # pygame.draw.rect(screen, (140, 140, 140), (130, 200, 20, 75))
    # pygame.draw.rect(screen, (140, 140, 140), (450, 200, 20, 75))
    # pygame.draw.line(screen, (255, 0, 0), (130, 237), (80, 237), 5)
    # pygame.draw.line(screen, (255, 0, 0), (470, 237), (520, 237), 5)
    # mouth -= 2
    # circle_l += l_speed
    # circle_r += r_speed
    # if circle_l >= 565:
    #     l_speed *= -1
    #     l_color += 1
    #     if l_color == 5:
    #         l_color = 0
    # if circle_l <= 35:
    #     l_speed *= -1
    #     l_color += 1
    #     if l_color == 5:
    #         l_color = 0
    #
    # if circle_r >= 565:
    #     r_color += 1
    #     r_speed *= -1
    #     if r_color == 5:
    #         r_color = 0
    # if circle_r <= 35:
    #     r_speed *= -1
    #     r_color += 1
    #     if r_color == 5:
    #         r_color = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_s:
                down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_s:
                down = False
    if up:
        y -= 3
    if down:
        y += 3
    if right:
        x += 15
        screen.blit(run[image_number], (x, y))
        image_number += 1
        if image_number == 10:
            image_number = 0
    elif left:
        x -= 15
        run[image_number] = pygame.transform.flip(run[image_number], True, False)
        screen.blit(run[image_number], (x, y))
        run[image_number] = pygame.transform.flip(run[image_number], True, False)
        image_number += 1
        if image_number == 10:
            image_number = 0
    clock.tick(20)
    pygame.display.update()
