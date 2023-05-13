import pygame

# Classes
from Player import Player
from Mob import Mob
from Map import Map

# pygame setup
pygame.init()

map_width = 1220
map_height = 720
screen = pygame.display.set_mode((map_width, map_height))
map1 = Map(screen)

screen = map1.screen

clock = pygame.time.Clock()
running = True
dt = 0

start_time = pygame.time.get_ticks()

player1 = Player(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2))
mob1 = Mob(pygame.Vector2(screen.get_width() / 6, screen.get_height() / 6))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    if not player1.is_alive():
        player1.respawn(screen)

    player_pos = player1.get_position()

#    print("player pos : ", player_pos)
#    print("default pos : ", player1.get_d_position())

    mob_pos = mob1.get_position()

    mob1.draw(screen)
    player1.draw(screen)

    if mob1.is_contact(player1):
        player1.get_damage(mob1.get_power())
    player1.movement(dt)
    player_hp = player1.get_hp()

    # Définir les dimensions et la position du texte
    font_size = 32
    text_x = 50
    text_y = 50

    # Créer un objet font
    font = pygame.font.Font(None, font_size)

    text_surface = font.render(str(player_hp), True, (0, 0, 0), (255, 255, 255))
    screen.blit(text_surface, (text_x, text_y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
