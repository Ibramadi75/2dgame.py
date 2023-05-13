import pygame
from Tools import *
from Entity import Entity


class Player(Entity):
    def __init__(self, position):

        # list of default values, useful when entities need to respawn
        self._properties = {
            "_d_position": position.copy(),
            "_d_hp": 20,
            "_d_width": 30,
            "_d_height": 30,
            "_d_color": "red"
        }

        super().__init__(self._properties["_d_position"], self._properties["_d_hp"], self._properties["_d_width"], self._properties["_d_height"], self._properties["_d_color"])

    def movement(self, dt):
        """
        Allow player to move by clicking on w,s,a or d

        :param dt:
        :return: True if movement has been executed, else return False
        """
        if self.is_alive():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                self._position.y -= 300 * dt
            if keys[pygame.K_s]:
                self._position.y += 300 * dt
            if keys[pygame.K_q]:
                self._position.x -= 300 * dt
            if keys[pygame.K_d]:
                self._position.x += 300 * dt
            return True
        return False

    def get_d_position(self):
        return self._properties["_d_position"]

    def respawn(self, screen):
        for prop, default_value in self._properties.items():
            setattr(self, prop[2:], default_value)
        self._is_dead = False
        self._position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


