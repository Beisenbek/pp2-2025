import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 40
y = 40
w = 20
h = 20
m_w = 400
m_h = 300
step = 20
clock = pygame.time.Clock()
color = (12, 237, 211)
color_grid = (207, 203, 192)
dx = 1
dy = 0

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    dx = 0
                    dy = -1
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    dx = 0
                    dy = 1

                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    dx = -1
                    dy = 0

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    dx = 1
                    dy = 0
        
        screen.fill((0, 0, 0))
       
        x += dx * step
        y += dy * step

        if x > m_w:
            x = 0
        if y > m_h:
            y = 0
        if x < 0:
            x = m_w
        if y < 0:
            y = m_h

        pygame.draw.rect(screen, color, pygame.Rect(x, y, 20, 20))

        for l_y in range(0, m_h, step):
            pygame.draw.line(screen, color_grid, (0,l_y), (m_w, l_y))
        
        for l_x in range(0, m_w, step):
            pygame.draw.line(screen, color_grid, (l_x,0), (l_x, m_h))

        pygame.display.flip()
        clock.tick(5)