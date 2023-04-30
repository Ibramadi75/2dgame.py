import pygame

# Classes
from Player import Player
from Mob import Mob

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

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

    player_pos = player1.get_position()
    mob_pos = mob1.get_position()

    player1.draw(screen)
    mob1.draw(screen)

    if(mob1.is_contact(player1)):
        print("player x : ", player1.get_position().x)
        print("mob : ", mob1.get_position().x)

    player1.movement(dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()