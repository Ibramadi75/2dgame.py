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

player1 = Player(self, pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2))
mob1 = Mob(pygame.Vector2(screen.get_width() / 6, screen.get_height() / 6))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    player_pos = player1.getPosition()
    mob_pos = mob1.getPosition()

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "green", mob_pos, 10)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()