import pygame
import random
pygame.init()

white = [255, 255, 255]
black = [0, 0, 0]
size =  [800, 400]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kar Yağışı")

snowFall = []
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snowFall.append([x, y])

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    screen.fill(black)
    for i in range(len(snowFall)):
        pygame.draw.circle(screen, white, snowFall[i], 2)

        snowFall[i][1] += 1
        if snowFall[i][1] > 400:
            y = random.randrange(-50, -10)
            snowFall[i][1] = y

            x = random.randrange(0, 800)
            snowFall[i][0] = x
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
