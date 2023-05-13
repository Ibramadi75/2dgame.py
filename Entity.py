import pygame


class Entity:
    last_damage = 0
    damage_delay = 600 # delay between two taken damage in ms

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

    def get_damage(self, power: int):
        if self.can_get_damage(pygame.time.get_ticks()):
            if self.is_alive():
                self._hp -= power

    def can_get_damage(self, current):
        delay = self.damage_delay
        if current >= self.last_damage + delay:
            self.last_damage = pygame.time.get_ticks()
            return True
        return False

    def is_alive(self):
        if self._hp > 0 and not self._is_dead :
            return True
        self._is_dead = True
        return False
