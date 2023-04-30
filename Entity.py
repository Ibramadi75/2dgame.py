import pygame


class Entity:
    def __init__(self, position, hp, width, height, color):
        self._position = position
        self._hp = hp
        self._width = width
        self._height = height
        self._color = color

    def get_position(self):
        return self._position

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, self._position, self._width)
