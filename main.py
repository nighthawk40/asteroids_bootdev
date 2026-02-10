import pygame 
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Get new instance of GUI window with SCREEN_HEIGHT and SCREEN_WIDTH
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create game clock object and initialize dt
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # create asteroid field
    asteroid_field = AsteroidField()

    # Create Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create game loop
    while True:
        # Call log_state function
        log_state()

        # start processing game events
        for event in pygame.event.get():
            # If window is closed stop the game loop
            if event.type == pygame.QUIT:
                return 
        
        # update player
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        # Fill screen to be black
        screen.fill("black")

        # draw 
        for obj in drawable:
            obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Pause loop for 1/60th a second before continuing
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
