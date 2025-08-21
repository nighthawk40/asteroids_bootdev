import pygame 
import random 
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            self.radius, 
            width=2
        )
    

    def update(self, dt):
        self.position += self.velocity * dt
    

    def split(self):
        self.kill() # Remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        # Create two smaller asteroids based on asteroid size 
        angle = random.uniform(20, 50)
        # Rotate the velocity by a random angle to create two new asteroids
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        # Create new asteroids with the same position but smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        # Set the velocities for the new asteroids 
        asteroid1.velocity = v1 * 1.2 # Increase speed slightly
        asteroid2.velocity = v2 * 1.2
        

        


