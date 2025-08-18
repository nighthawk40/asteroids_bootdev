import pygame 
from constants import * 

def main():
    # Intialize Pygame
    pygame.init()
    # Set up GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create game loop 
    running = True 
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        # fill screen with black
        screen.fill((0, 0, 0))
        # refresh the display
        pygame.display.flip()

    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()