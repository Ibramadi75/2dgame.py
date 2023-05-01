from Entity import Entity
from Player import Player


class Mob(Entity):
    __power_attack = 3

    def __init__(self, position):
        super().__init__(position, 10, 30, 30, "red")

    def is_contact(self, player: Player):
        rayon = self._width * 2

        x = int(self._position.x)
        player_pos_x = int(player.get_position().x)

        if player_pos_x in range(x-rayon, x) or player_pos_x in range(x, x+rayon):

            y = int(self._position.y)
            player_pos_y = int(player.get_position().y)

            if player_pos_y in range(y-rayon, y) or player_pos_y in range(y, y + rayon):
                return True

        return False

    def attack(self, player: Player):
        player.get_damage(self.__power_attack)

    def get_power(self):
        return self._hp
