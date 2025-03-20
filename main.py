import pygame 
from constants import *
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print ("Starting Asteroids!")
    print ("Screen width: 1280")
    print ("Screen height: 720")

    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
        dt = clock.tick(60) / 1000  
        updatable.update(dt)
        shot = player.update(dt)
        
        if shot:
         shots.add(shot)
         drawable.add(shot)
         updatable.add(shot)

        for asteroid in asteroids:
         if player.collision(asteroid):
          print("Game over!")
          import sys
          sys.exit()

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()