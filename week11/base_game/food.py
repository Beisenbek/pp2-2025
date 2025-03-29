import pygame
from game_object import GameObject 
from game_object import Point 

class Food(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(120, 20)],(0,255,0), tile_width)
    
    def can_eat(self, head_location):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result
