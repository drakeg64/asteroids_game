import random
from logger import log_event
from constants import *
from circleshape import CircleShape
import pygame
from particle import Particle
import math


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.points = []
        num_points = 8
        for i in range(num_points):
            angle = (i / num_points) * (2 * math.pi)
            dist = self.radius * random.uniform(0.7, 1.2)
            self.points.append(pygame.Vector2(
                math.cos(angle) * dist,
                math.sin(angle) * dist
            ))
    def draw(self, screen):
        actual_points = []
        for p in self.points:
            actual_points.append(self.position + p)
        pygame.draw.polygon(screen, "white", actual_points, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt  
        self.wrap() 

    def split(self):
        self.kill()
        
        for _ in range(20):
            new_particle = Particle(self.position.x, self.position.y, random.uniform(1, 4))
            


        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        
        random_angle = random.uniform(20, 50)
        
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
       
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
