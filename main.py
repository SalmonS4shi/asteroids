import pygame
import sys
import constants
import player
import asteroid
import asteroidfield
from shot import Shot
from circleshape import CircleShape
from logger import log_event
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    Shot.containers = (shots,drawable,updatable)

    player1 = player.Player(constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT / 2)
    asteroid_object = asteroidfield.AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for object in asteroids:
            if CircleShape.collides_with(player1,object):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for object in asteroids:
            for bullet in shots:
                if CircleShape.collides_with(bullet,object):
                    log_event("asteroid_shot")
                    object.split()
                    bullet.kill()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
