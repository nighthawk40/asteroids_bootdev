import pygame
import sys  
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Intialize Pygame
    pygame.init()
    # Set up GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0 # delta time between frames

    # Create sprite groups for updatable and drawable objects
    # This allows us to manage game objects more easily
    # updatable group will contain objects that need to be updated each frame
    # drawable group will contain objects that need to be drawn each frame
    # We will use these groups to manage the player and other game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Create player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Create game loop 
    running = True 
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        # Update game state
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
                
            
        # fill screen with black
        screen.fill((0, 0, 0))


        # Draw objects
        for obj in drawable:
            obj.draw(screen)

        # refresh the display
        pygame.display.flip()

        # Cap the frame rate
        dt = clock.tick(60) / 1000  # dt is in seconds
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()