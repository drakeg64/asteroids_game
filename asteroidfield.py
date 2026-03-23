import pygame
import random
from asteroid import Asteroid
from constants import *
from logger import log_event


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.wave_count = 0
        self.asteroid_count = 0
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        if len(Asteroid.containers[2]) < 1:
            print("Spawning wave", self.wave_count)
            self.wave_count += 1

            # spawn a new asteroid at a random edge
            for i in range(self.wave_count):
                edge = random.choice(self.edges)
                speed = random.randint(40, 100)
                velocity = edge[0] * speed
                velocity = velocity.rotate(random.randint(-30, 30))
                position = edge[1](random.uniform(0, 1))
                kind = random.randint(1, ASTEROID_KINDS)
                i += 1
                if self.wave_count % 5 == 0:
                    log_event("boss_wave")
               
                    self.spawn((ASTEROID_MIN_RADIUS * kind) + ((self.wave_count / 5) * 25) + 25, position, velocity)
                    break
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
                
        
        
           
            

        