import pygame 
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Get new instance of GUI window with SCREEN_HEIGHT and SCREEN_WIDTH
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create game loop
    while True:
        # Call log_state function
        log_state()

        # start processing game events
        for event in pygame.event.get():
            # If window is closed stop the game loop
            if event.type == pygame.QUIT:
                return 
        
        # Fill screen to be black
        screen.fill("black")

        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
