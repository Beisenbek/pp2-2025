import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()


is_blue = True
x = 30
y = 30

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        elif pressed[pygame.K_DOWN]: y += 3
        elif pressed[pygame.K_LEFT]: x -= 3
        elif pressed[pygame.K_RIGHT]: x += 3

        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)     
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        pygame.display.flip()
    
        # will block execution until 1/60 seconds have passed
        # since the previous time clock.tick was called.
        clock.tick(60)