import random
import pygame
from constants import LINE_WIDTH

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) * random.uniform(50, 150)
        self.radius = radius
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.radius -= 0.1
        if self.radius <= 0:
            self.kill()
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, self.radius, LINE_WIDTH)