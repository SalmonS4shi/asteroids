import circleshape
import pygame
import constants
import random
from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,constants.LINE_WIDTH)

    def update(self,dt: float,):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return None
        else:
            log_event("asteroid_split")
            randomly = random.uniform(20,50)
            new_vector1 = self.velocity.rotate(randomly)
            new_vector2 = self.velocity.rotate(-randomly)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = new_vector1 * 1.2
            asteroid_2.velocity = new_vector2 * 1.2