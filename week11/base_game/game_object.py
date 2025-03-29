import pygame

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        
class GameObject:
    def __init__(self, points, color, tile_width):
        self.points = points
        self.color = color
        self.tile_width = tile_width

    def draw(self, screen):
        for point in self.points:
            pygame.draw.rect(screen, self.color, pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width), 1)

