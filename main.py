import pygame 
from constants import * 
from player import Player

def main():
    # Intialize Pygame
    pygame.init()
    # Set up GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0 # delta time between frames

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Create player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    # Create game loop 
    running = True 
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        # Update game state
        updatable.update(dt)

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