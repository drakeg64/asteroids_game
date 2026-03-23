from multiprocessing.util import info

import pygame
import sys

from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot
from particle import Particle

def main():
    pygame.init()
    info = pygame.display.Info()

    real_width = info.current_w
    real_height = info.current_h
    screen = pygame.display.set_mode((real_width, real_height))
    game_clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Particle.containers = (updatable, drawable)

    
    player_1 = Player(real_width / 2, real_height / 2)
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    score = 0
    dt = 0
    

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        updatable.update(dt)


        for asteroid in asteroids:
            if asteroid.collides_with(player_1):
                if player_1.invulnerable_timer <= 0:
                    log_event("player_hit")
                    if player_1.lives < 1:
                        print("Game over!")
                        sys.exit()
                    else: 
                        player_1.lives -= 1
                        player_1.respawn()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    score += 100
                    asteroid.split()
                    shot.kill()
        
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        if player_1.lives < 1:
            lives_text = font.render(f"Lives: {player_1.lives}", True, (255, 0, 0))
        else:
            lives_text = font.render(f"Lives: {player_1.lives}", True, (255, 255, 255))
        wave_count = asteroid_field.wave_count
        wave_text = font.render(f"Wave: {wave_count}", True, (255, 255, 255))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10,10))
        screen.blit(lives_text, (10, 40))
        screen.blit(wave_text, (10, 70))
        pygame.display.flip()
        
        # limit the framerate to 60fps
        dt = game_clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()
