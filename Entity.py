import pygame


class Entity:
    def __init__(self, position, hp, width, height, color):
        self._position = position
        self._hp = hp
        self._width = width
        self._height = height
        self._color = color
        self._is_dead = False

    def get_position(self):
        return self._position

    def get_hp(self):
        return self._hp

    def draw(self, screen):
        if self.is_alive():
            pygame.draw.circle(screen, self._color, self._position, self._width)

    def is_alive(self):
        if self._hp > 0:
            return True
        self._is_dead = True
        return False
