import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

image = pygame.image.load('ball.png')


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill((255, 255, 255))
        screen.blit(image, (120, 120))
        pygame.display.flip()
    
        # will block execution until 1/60 seconds have passed
        # since the previous time clock.tick was called.
        clock.tick(60)