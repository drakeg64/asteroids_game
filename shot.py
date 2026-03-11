from circleshape import CircleShape
import pygame
from constants import *
import random

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        color_green = pygame.Color(0, 255, 0)
        color_dark_green = pygame.Color(0, 100, 0)

        mix_amount = random.random()

        self.color = color_green.lerp(color_dark_green, mix_amount)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        