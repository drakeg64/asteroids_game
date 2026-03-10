import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player_1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        # limit the framerate to 60fps
        dt = game_clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()
