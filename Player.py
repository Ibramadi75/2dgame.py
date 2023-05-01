import pygame
from Entity import Entity


class Player(Entity):
    def __init__(self, position):
        super().__init__(position, 20, 30, 30, "red")

    def movement(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self._position.y -= 300 * dt
        if keys[pygame.K_s]:
            self._position.y += 300 * dt
        if keys[pygame.K_a]:
            self._position.x -= 300 * dt
        if keys[pygame.K_d]:
            self._position.x += 300 * dt

    def get_damage(self, power: int):
        self._hp -= power

    def is_alive(self):
        return self._hp > 0
