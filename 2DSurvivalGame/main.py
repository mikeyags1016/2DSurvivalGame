import pygame

# Initiates module
pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption('2DSurvival v0')

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
